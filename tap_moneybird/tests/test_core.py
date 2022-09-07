"""Tests standard tap features using the built-in SDK tests library."""

import os

import pendulum
from singer_sdk.testing import get_standard_tap_tests

from tap_moneybird.tap import TapMoneyBird

SAMPLE_CONFIG = {
    "auth_token": os.environ["MONEYBIRD_AUTH_TOKEN"], 
    "administration_id": os.environ["MONEYBIRD_ADMINSTRATION_ID"],
    "start_date": os.environ.get("START_DATE", pendulum.today().to_date_string()),
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapMoneyBird,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()
