from rito import errors
from rito.models import champion_mastery
from rito.extractors import champion_mastery_extractor, base_extractor
from tests.examples import champion_masteries_example, champion_mastery_example

import pytest


def test_championmasteryextractor():
    assert issubclass(
        champion_mastery_extractor.ChampionMasteryExtractor,
        base_extractor.BaseExtractor,
    )


def test_championmasteryextractor_get_champion_mastery_by_champion_id_GOOD():
    extractor = champion_mastery_extractor.ChampionMasteryExtractor()
    cm_dict = extractor._get_champion_mastery_by_champion_id(
        champion_masteries_list=champion_masteries_example.champion_masteries_example,
        champion_id="7",
    )

    assert cm_dict == {
        "puuid": "-kbxQ0spJBMGRZGy2fce97DBckHnpb5miceVkxbBP9HRhgevQhcuwNClRrGahgVKi3u-F3uOgX_RvA",
        "championId": 7,
        "championLevel": 1,
        "championPoints": 1110,
        "lastPlayTime": 1685034736000,
        "championPointsSinceLastLevel": 1110,
        "championPointsUntilNextLevel": 690,
        "chestGranted": False,
        "tokensEarned": 0,
        "summonerId": "fyIndSpsUZToLTx9m0svW1J7UrsglQyw_C_A7w9gl9gCod9u",
    }


def test_championmasteryextractor_get_champion_mastery_by_champion_id_NO_CHAMPION():
    extractor = champion_mastery_extractor.ChampionMasteryExtractor()

    with pytest.raises(errors.ExtractorError):
        extractor._get_champion_mastery_by_champion_id(
            champion_masteries_list=champion_masteries_example.champion_masteries_example,
            champion_id="1",
        )


def test_championmasteryextractor_extract_ERROR():
    with pytest.raises(errors.ExtractorError):
        champion_mastery_extractor.ChampionMasteryExtractor().extract(["kok", "lol"])


def test_championmasteryextractor_extract():
    extractor = champion_mastery_extractor.ChampionMasteryExtractor()
    cm = extractor.extract(champion_mastery_example.champion_mastery_example)

    assert type(cm) == champion_mastery.ChampionMastery
    assert cm == champion_mastery.ChampionMastery(
        puuid="-kbxQ0spJBMGRZGy2fce97DBckHnpb5miceVkxbBP9HRhgevQhcuwNClRrGahgVKi3u-F3uOgX_RvA",
        champion_id="7",
        champion_points=1110,
        champion_level=1,
        last_play_time=1685034736000,
        champion_points_since_last_level=1110,
        champion_points_until_next_level=690,
        chest_granted=False,
        tokens_earned=0,
        summoner_id="fyIndSpsUZToLTx9m0svW1J7UrsglQyw_C_A7w9gl9gCod9u",
    )


def test_championmasteryextractor_extract_from_list_ERROR():
    with pytest.raises(errors.ExtractorError):
        champion_mastery_extractor.ChampionMasteryExtractor().extract_from_list(
            {"lol": "xd"}, champion_id="1"
        )


def test_championmasteryextractor_extract_from_list_ERROR2():
    with pytest.raises(errors.ExtractorError):
        champion_mastery_extractor.ChampionMasteryExtractor().extract_from_list(
            ["lol", "xd"], champion_id=""
        )


def test_championmasteryextractor_extract_from_list_GOOD():
    extractor = champion_mastery_extractor.ChampionMasteryExtractor()
    cm = extractor.extract_from_list(
        champion_masteries_example.champion_masteries_example, champion_id="7"
    )

    assert type(cm) == champion_mastery.ChampionMastery
    assert cm == champion_mastery.ChampionMastery(
        puuid="-kbxQ0spJBMGRZGy2fce97DBckHnpb5miceVkxbBP9HRhgevQhcuwNClRrGahgVKi3u-F3uOgX_RvA",
        champion_id="7",
        champion_points=1110,
        champion_level=1,
        last_play_time=1685034736000,
        champion_points_since_last_level=1110,
        champion_points_until_next_level=690,
        chest_granted=False,
        tokens_earned=0,
        summoner_id="fyIndSpsUZToLTx9m0svW1J7UrsglQyw_C_A7w9gl9gCod9u",
    )


def test_championmasteryextractor_extract_from_list_NO_CHAMPION():
    extractor = champion_mastery_extractor.ChampionMasteryExtractor()

    with pytest.raises(errors.ExtractorError):
        extractor.extract_from_list(
            champion_masteries_example.champion_masteries_example, champion_id="1"
        )


def test_championmasteryextractor_extract_totals_from_list_ERROR():
    with pytest.raises(errors.ExtractorError):
        champion_mastery_extractor.ChampionMasteryExtractor().extract_totals_from_list(
            {"kok": "lol"}
        )


def test_championmasteryextractor_extract_totals_from_list():
    extractor = champion_mastery_extractor.ChampionMasteryExtractor()
    cm = extractor.extract_totals_from_list(
        champion_masteries_example.champion_masteries_example
    )

    assert type(cm) == champion_mastery.ChampionMasteryTotals
    assert cm == champion_mastery.ChampionMasteryTotals(
        total_champion_level=79, total_champion_points=427017
    )
