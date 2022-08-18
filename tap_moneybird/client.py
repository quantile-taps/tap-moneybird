"""REST client handling, including MoneyBirdStream base class."""

import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union
from urllib.parse import parse_qs, urlparse

import requests
from memoization import cached
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


class MoneyBirdStream(RESTStream):
    """MoneyBird stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return f"https://moneybird.com/api/v2/{self.config.get('administration_id')}"

    records_jsonpath = "$[*]"  # Or override `parse_response`.

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("auth_token")
        )

    def next_page_link_not_in_header(self, response: requests.Response) -> bool:
        """Return True if there is no `next page link` in the response header."""
        # The `Link` key does not exist in the response header object.
        if "Link" not in response.headers:
            return True
        else: 
            # The value of the `Link` response header does not contain a `next` link.
            return "next" not in response.headers["Link"]

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""

        # logging.info(response.headers['Link'])

        if self.next_page_link_not_in_header(response):
            return None
        else:
            # Grab the first occurring link URL from the header.
            link_next_page = response.headers["Link"].split(';')[0].strip('<>')

            # Parse the URL to get the page number.
            next_page_token = parse_qs(urlparse(link_next_page).query)["page"][0]

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

