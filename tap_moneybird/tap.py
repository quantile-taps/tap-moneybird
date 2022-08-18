"""MoneyBird tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_moneybird.streams import (
    ContactsStream,
    ExternalSalesInvoicesStream,
    LedgerAccountsStream,
    PurchaseInvoicesStream,
    ReceiptsStream,
    SalesInvoicesStream,
)

STREAM_TYPES = [
    # ContactsStream, 
    ExternalSalesInvoicesStream,
    # PurchaseInvoicesStream,
    # ReceiptsStream,
    # SalesInvoicesStream, 
    # LedgerAccountsStream,
]


class TapMoneyBird(Tap):
    """MoneyBird tap class."""
    name = "tap-moneybird"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the MoneyBird API service."
        ),
        th.Property(
            "administration_id",
            th.IntegerType,
            required=True,
            description="The ID of the MoneyBird administration to connect to."
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync."
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
