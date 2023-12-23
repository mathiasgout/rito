from rito import errors
from rito.models import Account
from rito.extractors import base_extractor, account_extractor
from tests.examples import account_example

import pytest


def test_accountextractor():
    assert issubclass(account_extractor.AccountExtractor, base_extractor.BaseExtractor)


def test_test_accountextractor_extract_ERROR():
    extractor = account_extractor.AccountExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract(["lol", "oui"])


def test_accountextractor_extract():
    extractor = account_extractor.AccountExtractor()
    a = extractor.extract(account_example.account_example)

    assert a == Account(
        puuid="eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g",
        game_name="davlaf",
        tag_line="EUW"
    )
