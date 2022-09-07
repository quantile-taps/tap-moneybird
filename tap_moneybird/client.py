"""REST client handling, including MoneyBirdStream base class."""
import re
from typing import Any, Dict, Optional
from urllib.parse import parse_qs, urlparse

import pendulum
import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.streams import RESTStream


class MoneyBirdStream(RESTStream):
    """MoneyBird stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return f"https://moneybird.com/api/v2/{self.config.get('administration_id')}"

    records_jsonpath = "$[*]"  # Or override `parse_response`.

    @property
    def start_date(self) -> str:
        start_date = pendulum.parse(self.config.get('start_date'))
        return start_date.format('YYYYMM')

    @property
    def today(self) -> str:
        return pendulum.today().format("YYYYMM")

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("auth_token")
        )

    def get_next_page_token(self, response: requests.Response, previous_token: Optional[Any]) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""

        # If there is no next page, return None.
        if self.no_next_page(response):
            return None

        # Get the next page number from the `Link` header.
        next_page_token = self.get_next_page_number(response.headers["Link"])
        
        return next_page_token

    def no_next_page(self, response: requests.Response) -> bool:
        """Returns True if there is no next page."""
        try:
            # If there is no next page, the `Link` header will not contain a `rel="next"` link.
            return "next" not in response.headers["Link"]

        # If the `Link` key does not exist, return True.
        except KeyError:
            return True

    def get_next_page_number(self, link_header: str) -> str:
        """Returns the next page number from the `Link` header."""
        # Use regex to extract the first URL from the link_header
        next_page_url = re.search(r"<(.*?)>", link_header).group(1)

        # Parse the URL to get the page number.
        parsed_url = urlparse(next_page_url)

        # Get the page number from the parsed URL.
        next_page_number = parse_qs(parsed_url.query)["page"][0]

        return next_page_number


    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""

        params: dict = {'filter': f'period:{self.start_date}..{self.today}'}
        
        if next_page_token:
            params["page"] = next_page_token
        
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key


        return params
