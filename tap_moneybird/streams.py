"""Stream type classes for tap-moneybird."""
from singer_sdk import typing as th

from tap_moneybird.client import MoneyBirdStream


class ContactsStream(MoneyBirdStream):
    """Extracts contacts from MoneyBird."""
    name = "contacts"
    path = "/contacts.json"

    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("administration_id", th.IntegerType),
        th.Property("company_name", th.StringType),
        th.Property("firstname", th.StringType),
        th.Property("lastname", th.StringType),
        th.Property("updated_at", th.DateTimeType),
    ).to_dict()

class LedgerAccountsStream(MoneyBirdStream):
    """Extracts ledger accounts from MoneyBird."""
    name = "ledger_accounts"
    path = "/ledger_accounts.json"

    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("administration_id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("account_type", th.StringType),
        th.Property("account_id", th.StringType),
        th.Property("parent_id", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
    ).to_dict()

class ReceiptsStream(MoneyBirdStream):
    """Extracts contacts from MoneyBird."""
    name = "receipts"
    path = "/documents/receipts.json"

    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("administration_id", th.IntegerType),
        th.Property("contact_id", th.StringType),
        th.Property("reference", th.StringType),
        th.Property("date", th.DateTimeType),
        th.Property("due_date", th.DateTimeType),
        th.Property("entry_number", th.IntegerType),
        th.Property("state", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("exchange_rate", th.StringType),
        th.Property("revenue_invoice", th.StringType),
        th.Property("prices_are_incl_tax", th.BooleanType),
        th.Property("origin", th.StringType),
        th.Property("paid_at", th.StringType),
        th.Property("tax_number", th.StringType),
        th.Property("total_price_excl_tax", th.StringType),
        th.Property("total_price_excl_tax_base", th.StringType),
        th.Property("total_price_incl_tax", th.StringType),
        th.Property("total_price_incl_tax_base", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("version", th.IntegerType),
    ).to_dict()

class PurchaseInvoicesStream(MoneyBirdStream):
    """Extracts purchase invoices from MoneyBird."""
    name = "purchase_invoices"
    path = "/documents/purchase_invoices.json"

    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("administration_id", th.IntegerType),
        th.Property("contact_id", th.StringType),
        th.Property("invoice_id", th.StringType),
        th.Property("reference", th.StringType),
        th.Property("date", th.DateTimeType),
        th.Property("due_date", th.StringType),
        th.Property("entry_number", th.IntegerType),
        th.Property("state", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("exchange_rate", th.StringType),
        th.Property("revenue_invoice", th.BooleanType),
        th.Property("prices_are_incl_tax", th.BooleanType),
        th.Property("origin", th.StringType),
        th.Property("paid_at", th.StringType),
        th.Property("total_price_excl_tax", th.StringType),
        th.Property("total_price_incl_tax", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
    ).to_dict()

class SalesInvoicesStream(MoneyBirdStream):
    """Extracts sales invoices from MoneyBird."""
    name = "sales_invoices"
    path = "/sales_invoices.json"

    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("administration_id", th.IntegerType),
        th.Property("contact_id", th.StringType),
        th.Property("invoice_id", th.StringType),
        th.Property("state", th.StringType),
        th.Property("invoice_date", th.StringType),
        th.Property("due_date", th.StringType),
        th.Property("payment_reference", th.StringType),
        th.Property("reference", th.StringType),
        th.Property("language", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("discount", th.StringType),
        th.Property("original_sales_invoice_id", th.StringType),
        th.Property("paused", th.StringType),
        th.Property("paid_at", th.StringType),
        th.Property("created_at", th.StringType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("total_paid", th.StringType),
        th.Property("total_unpaid", th.StringType),
        th.Property("prices_are_incl_tax", th.BooleanType),
        th.Property("total_price_excl_tax", th.StringType),
        th.Property("total_price_incl_tax", th.StringType),
        th.Property("total_discount", th.StringType),
        th.Property("marked_dubious_on", th.StringType),
        th.Property("marked_uncollectible_on", th.StringType),
    ).to_dict()

class ExternalSalesInvoicesStream(MoneyBirdStream):
    """Extracts external sales invoices from MoneyBird."""
    name = "external_sales_invoices"
    path = "/external_sales_invoices.json"

    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("administration_id", th.IntegerType),
        th.Property("contact_id", th.StringType),
        th.Property("contact", th.StringType),
        th.Property("state", th.StringType),
        th.Property("due_date", th.StringType),
        th.Property("reference", th.StringType),
        th.Property("entry_number", th.IntegerType),
        th.Property("origin", th.StringType),
        th.Property("source", th.StringType),
        th.Property("source_url", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("paid_at", th.StringType),
        th.Property("created_at", th.StringType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("total_paid", th.StringType),
        th.Property("total_unpaid", th.StringType),
        th.Property("prices_are_incl_tax", th.BooleanType),
        th.Property("total_price_excl_tax", th.StringType),
        th.Property("total_price_incl_tax", th.StringType),
        th.Property("total_discount", th.StringType),
        th.Property("marked_dubious_on", th.StringType),
        th.Property("marked_uncollectible_on", th.StringType),
    ).to_dict()
