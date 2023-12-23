from rito import errors
from rito.models import Entry
from rito.extractors import base_extractor, league_extractor
from tests.examples import entries_example, entry_miniseries_example

import pytest


def test_entriesextractor():
    assert issubclass(league_extractor.EntriesExtractor, base_extractor.BaseExtractor)


def test_entriesextractor_get_miniseries_progress_EXISTS():
    extractor = league_extractor.EntriesExtractor()
    e_dict = extractor._get_miniseries_progress(
        entry_dict=entry_miniseries_example.entry_miniseries_example
    )

    assert e_dict == "WLN"


def test_entriesextractor_get_miniseries_progress_DONT_EXISTS():
    extractor = league_extractor.EntriesExtractor()
    e_dict = extractor._get_miniseries_progress(
        entry_dict=entries_example.entries_example[0]
    )

    assert e_dict is None


def test_entriesextractor_get_entry_by_queue_type_GOOD():
    extractor = league_extractor.EntriesExtractor()
    e_dict = extractor._get_entry_by_queue_type(
        entries_list=entries_example.entries_example, queue_type="RANKED_SOLO_5x5"
    )

    assert e_dict == {
        "leagueId": "86cf4399-48fe-4ceb-898c-421320e42416",
        "queueType": "RANKED_SOLO_5x5",
        "tier": "DIAMOND",
        "rank": "I",
        "summonerId": "fyIndSpsUZToLTx9m0svW1J7UrsglQyw_C_A7w9gl9gCod9u",
        "summonerName": "GeneLL1",
        "leaguePoints": 0,
        "wins": 115,
        "losses": 105,
        "veteran": False,
        "inactive": False,
        "freshBlood": False,
        "hotStreak": False,
    }


def test_entriesextractor_get_entry_by_queue_type_NO_QUEUE_TYPE():
    extractor = league_extractor.EntriesExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_entry_by_queue_type(
            entries_list=entries_example.entries_example, queue_type="prout"
        )


def test_entriesextractor_get_total_lp_GOOD():
    extractor = league_extractor.EntriesExtractor()
    assert extractor._get_total_lp(tier="DIAMOND", rank="I", league_points=0) == 2700
    assert (
        extractor._get_total_lp(tier="CHALLENGER", rank="I", league_points=1002) == 3802
    )


def test_entriesextractor_get_total_lp_NONE():
    extractor = league_extractor.EntriesExtractor()
    assert extractor._get_total_lp(tier="DIAMOND", rank="I", league_points=None) is None


def test_entriesextractor_extract_ERROR():
    with pytest.raises(errors.ExtractorError):
        league_extractor.EntriesExtractor().extract({"kok": "lol"})


def test_entriesextractor_extract():
    extractor = league_extractor.EntriesExtractor()
    entries = extractor.extract(entries_list=entries_example.entries_example)

    assert len(entries) == 2
    assert type(entries[0]) == type(entries[1]) == Entry
    assert entries[0] == Entry(
        league_id="28807304-53bf-485e-9255-333bd57a9e83",
        queue_type="RANKED_FLEX_SR",
        tier="PLATINUM",
        rank="I",
        summoner_id="fyIndSpsUZToLTx9m0svW1J7UrsglQyw_C_A7w9gl9gCod9u",
        summoner_name="GeneLL1",
        league_points=3,
        wins=23,
        losses=17,
        veteran=False,
        inactive=False,
        fresh_blood=False,
        hot_streak=False,
        total_lp=1903,
    )


def test_entriesextractor_extract_from_entry_ERROR():
    with pytest.raises(errors.ExtractorError):
        league_extractor.EntriesExtractor().extract_from_entry(["kok", "lol"])


def test_entriesextractor_extract_from_entry():
    extractor = league_extractor.EntriesExtractor()
    ent = extractor.extract_from_entry(entry_dict=entries_example.entries_example[0])

    assert type(ent) == Entry
    assert ent == Entry(
        league_id="28807304-53bf-485e-9255-333bd57a9e83",
        queue_type="RANKED_FLEX_SR",
        tier="PLATINUM",
        rank="I",
        summoner_id="fyIndSpsUZToLTx9m0svW1J7UrsglQyw_C_A7w9gl9gCod9u",
        summoner_name="GeneLL1",
        league_points=3,
        wins=23,
        losses=17,
        veteran=False,
        inactive=False,
        fresh_blood=False,
        hot_streak=False,
        total_lp=1903,
    )


def test_entriesextractor_extract_from_entry_MINISERIE():
    extractor = league_extractor.EntriesExtractor()
    ent = extractor.extract_from_entry(
        entry_dict=entry_miniseries_example.entry_miniseries_example
    )

    assert type(ent) == Entry
    assert ent == Entry(
        league_id="31a5c2c9-bd43-4aab-9841-282a3431fe29",
        queue_type="RANKED_SOLO_5x5",
        tier="DIAMOND",
        rank="I",
        summoner_id="JTv9359swD19EdkNFONC9bKI6bJ4fh5J3UjbJs7Gz9NsJaCO",
        summoner_name="Vorxu",
        league_points=100,
        wins=326,
        losses=282,
        veteran=False,
        inactive=False,
        fresh_blood=True,
        hot_streak=False,
        miniseries_progress="WLN",
        total_lp=2800,
    )


def test_entriesextractor_extract_entry_ERROR():
    with pytest.raises(errors.ExtractorError):
        league_extractor.EntriesExtractor().extract_entry(
            {"kok": "lol"}, queue_type="RANKED_FLEX_SR"
        )


def test_entriesextractor_extract_entry_ERROR2():
    with pytest.raises(errors.ExtractorError):
        league_extractor.EntriesExtractor().extract_entry(["kok", "lol"], queue_type="")


def test_entriesextractor_extract_entry_NO_QUEUE_TYPE():
    with pytest.raises(errors.ExtractorError):
        league_extractor.EntriesExtractor().extract_entry(
            entries_example.entries_example, queue_type="TOTO"
        )


def test_entriesextractor_extract_entry():
    extractor = league_extractor.EntriesExtractor()
    ent = extractor.extract_entry(
        entries_list=entries_example.entries_example, queue_type="RANKED_FLEX_SR"
    )

    assert type(ent) == Entry
    assert ent == Entry(
        league_id="28807304-53bf-485e-9255-333bd57a9e83",
        queue_type="RANKED_FLEX_SR",
        tier="PLATINUM",
        rank="I",
        summoner_id="fyIndSpsUZToLTx9m0svW1J7UrsglQyw_C_A7w9gl9gCod9u",
        summoner_name="GeneLL1",
        league_points=3,
        wins=23,
        losses=17,
        veteran=False,
        inactive=False,
        fresh_blood=False,
        hot_streak=False,
        total_lp=1903,
    )


def test_leagueextractor():
    extractor = league_extractor.LeagueExtractor()
    assert type(extractor.entries) == league_extractor.EntriesExtractor
