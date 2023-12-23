from rito import errors
from rito.models import Summoner
from rito.extractors import base_extractor, summoner_extractor
from tests.examples import summoner_example

import pytest


def test_summonerextractor():
    assert issubclass(summoner_extractor.SummonerExtractor, base_extractor.BaseExtractor)


def test_summonerextractor_extract_ERROR():
    extractor = summoner_extractor.SummonerExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract(["lol", "oui"])


def test_summonerextractor_extract():
    extractor = summoner_extractor.SummonerExtractor()
    s = extractor.extract(summoner_example.summoner_example)

    assert s == Summoner(
        summoner_id="GmrzDazS_aYqMvEg8ExGWK79lco2sEY2wi_95O8iuZDXKcQ",
        account_id="bgkop09Cgl3c_jyiY6KAIf8bfZ45XXLymuDRfU1sygZWmA",
        puuid="eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g",
        name="davlaf",
        profile_icon_id="7",
        revision_date=1684179136000,
        summoner_level=82,
    )
