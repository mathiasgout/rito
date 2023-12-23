from rito import errors
from rito.models import ActiveGame, ActiveGameSummoner
from rito.extractors import base_extractor, spectator_extractor
from tests.examples import active_game_example

import pytest
from freezegun import freeze_time


def test_activegameextractor():
    assert issubclass(spectator_extractor.ActiveGameExtractor, base_extractor.BaseExtractor)


def test_activegameextractor_get_participants_GOOD():
    extractor = spectator_extractor.ActiveGameExtractor()
    participants_list = extractor._get_participants(
        active_game_example.active_game_example
    )

    assert type(participants_list) == list
    assert all(type(participant) == dict for participant in participants_list) is True
    assert participants_list[1]["summonerName"] == "Klaj"


def test_activegameextractor_get_participants_ERROR():
    extractor = spectator_extractor.ActiveGameExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_participants({})


def test_activegameextractor_get_participant_by_summoner_id_GOOD():
    extractor = spectator_extractor.ActiveGameExtractor()
    participant = extractor._get_participant_by_summoner_id(
        active_game_example.active_game_example["participants"],
        "Zf5pmqQ38shck40NEBXc5mrbH_aWTyrtAPhaBUTvrysYdzI",
    )

    assert participant == {
        "teamId": 100,
        "spell1Id": 12,
        "spell2Id": 4,
        "championId": 516,
        "profileIconId": 7,
        "summonerName": "Klaj",
        "bot": False,
        "summonerId": "Zf5pmqQ38shck40NEBXc5mrbH_aWTyrtAPhaBUTvrysYdzI",
        "gameCustomizationObjects": [],
        "perks": {
            "perkIds": [8360, 8304, 8345, 8347, 8451, 8444, 5007, 5002, 5002],
            "perkStyle": 8300,
            "perkSubStyle": 8400,
        },
    }


def test_activegameextractor_get_participant_by_summoner_id_ERROR():
    extractor = spectator_extractor.ActiveGameExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_participant_by_summoner_id(
            active_game_example.active_game_example["participants"], "dsds"
        )


def test_activegameextractor_get_participants_id():
    extractor = spectator_extractor.ActiveGameExtractor()
    participants_ids = extractor._get_participants_id(
        active_game_example.active_game_example["participants"]
    )

    assert participants_ids == [
        "OV8fhFOWjGmFeiR6YBfuDNwNWEVh-Y46JZHfu4cUeyEpp9g",
        "Zf5pmqQ38shck40NEBXc5mrbH_aWTyrtAPhaBUTvrysYdzI",
        "KGuWozs8wyS1ubjbs6KoNjJKvSCra_YNB7aDxN_ObZlSO3zp",
        "_kiNtRkhIpHr4KHrrBMk2-bCwyvrIdCuuU2UB8ah2FArkiE",
        "bzjgH0-K4cEJv6fF5E6vMrh1nz4miIObQ5OjW2OcEqA30Lg",
        "isiEDjqLGnvJrtEnNirwcV1ENDwAX7q6BO0-23JOYgZtBLY",
        "iwvafrjAT4YgTITgCDi25PP4_V3iqK-pVZaM7W_2k8oMc5TLshdXWf_-Jg",
        "-qRmCZ3870GVi42cS79fnKA1PTTkX0mVcr9WCMYYUuLzp4k",
        "0RLi02ZeUidlx6Zchv1M68eVYx3RMpp5yAksbULcuRpvvm-y",
        "q-KP_RWpS8wExEkNs-aqZ-E8aTGTgW5cNISHkTDKo0tzxuQ",
    ]


def test_activegameextractor_get_match_id_GOOD():
    extractor = spectator_extractor.ActiveGameExtractor()
    match_id = extractor._get_match_id(game_id="111", platform_id="EUW1")

    assert match_id == "EUW1_111"


def test_activegameextractor_get_match_id_NONE():
    extractor = spectator_extractor.ActiveGameExtractor()
    match_id = extractor._get_match_id(game_id=None, platform_id="EUW1")

    assert match_id is None


@freeze_time("2000-01-01 00:00:00")
def test_activegameextractor_get_ts_milli_utc():
    extractor = spectator_extractor.ActiveGameExtractor()
    ts_milli = extractor._get_ts_milli_utc()

    assert ts_milli == 946684800000


def test_activegameextractor_get_game_start_time_GOOD():
    extractor = spectator_extractor.ActiveGameExtractor()
    assert extractor._get_game_start_time(1000) == 1000


def test_activegameextractor_get_game_start_time_NO_VALUE(mocker):
    mocker.patch(
        "rito.extractors.spectator_extractor.ActiveGameExtractor._get_ts_milli_utc",
        return_value=1,
    )

    extractor = spectator_extractor.ActiveGameExtractor()
    assert extractor._get_game_start_time() == 1


def test_activegameextractor_extract_ERROR():
    extractor = spectator_extractor.ActiveGameExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract(["lol", "oui"])


def test_activegameextractor_extract():
    extractor = spectator_extractor.ActiveGameExtractor()
    ag = extractor.extract(active_game_example.active_game_example)

    assert ag == ActiveGame(
        match_id="EUW1_6462333479",
        queue_id=420,
        game_start_time=1687338155300,
        participants_id=[
            "OV8fhFOWjGmFeiR6YBfuDNwNWEVh-Y46JZHfu4cUeyEpp9g",
            "Zf5pmqQ38shck40NEBXc5mrbH_aWTyrtAPhaBUTvrysYdzI",
            "KGuWozs8wyS1ubjbs6KoNjJKvSCra_YNB7aDxN_ObZlSO3zp",
            "_kiNtRkhIpHr4KHrrBMk2-bCwyvrIdCuuU2UB8ah2FArkiE",
            "bzjgH0-K4cEJv6fF5E6vMrh1nz4miIObQ5OjW2OcEqA30Lg",
            "isiEDjqLGnvJrtEnNirwcV1ENDwAX7q6BO0-23JOYgZtBLY",
            "iwvafrjAT4YgTITgCDi25PP4_V3iqK-pVZaM7W_2k8oMc5TLshdXWf_-Jg",
            "-qRmCZ3870GVi42cS79fnKA1PTTkX0mVcr9WCMYYUuLzp4k",
            "0RLi02ZeUidlx6Zchv1M68eVYx3RMpp5yAksbULcuRpvvm-y",
            "q-KP_RWpS8wExEkNs-aqZ-E8aTGTgW5cNISHkTDKo0tzxuQ",
        ],
    )


def test_activegameextractor_extract_summoner_ERROR():
    extractor = spectator_extractor.ActiveGameExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_summoner(
            ["lol", "oui"], "OV8fhFOWjGmFeiR6YBfuDNwNWEVh-Y46JZHfu4cUeyEpp9g"
        )


def test_activegameextractor_extract_summoner_ERROR2():
    extractor = spectator_extractor.ActiveGameExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_summoner({"lol": "oui"}, "")


def test_activegameextractor_extract_summoner():
    extractor = spectator_extractor.ActiveGameExtractor()
    ag = extractor.extract_summoner(
        active_game_example.active_game_example,
        summoner_id="OV8fhFOWjGmFeiR6YBfuDNwNWEVh-Y46JZHfu4cUeyEpp9g",
    )

    assert ag == ActiveGameSummoner(
        team_id="100",
        champion_id="246",
        summoner_name="KTRSmeb442",
        summoner_id="OV8fhFOWjGmFeiR6YBfuDNwNWEVh-Y46JZHfu4cUeyEpp9g",
        bot=False,
        spell_id1="4",
        spell_id2="14",
    )


def test_spectatorextractor():
    extractor = spectator_extractor.SpectatorExtractor()
    assert type(extractor.active_game) == spectator_extractor.ActiveGameExtractor
