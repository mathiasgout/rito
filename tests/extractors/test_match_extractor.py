from rito import errors
from rito.models import Match, MatchSummoner, TeamTotals, TimelineDamageStats, TimelineChampionStats
from rito.extractors import base_extractor, match_extractor
from tests.examples import match_example

import pytest


def test_matchextractor():
    assert issubclass(match_extractor.MatchExtractor, base_extractor.BaseExtractor)


def test_matchextractor_get_participants_ids_map_GOOD():
    extractor = match_extractor.MatchExtractor()
    participants_ids_map = extractor._get_participants_ids_map(
        participants_ids=match_example.timeline_example["info"]["participants"]
    )
    participants_ids_map == {
        'eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g': '1', 
        'KR1LzoXFfbMSgq_ij0Wj9Ph-hnXx9ImSnpJ75YLIXud6Nff8W_FUjplpgNVkdYSguyaUuPGPjL-H2w': '2', 
        '3LgDeUuEAqUBgGhZcAZzi6diNVfeLWBFiOfTOgZN2Uzdi7VY_dR_kPp5xKICQReyh9LgO-l0dLbycw': '3', 
        'AJ3DSRe7xoSH5e_7gwkMiaylGWsYg0Zxi42nHd9Sw9VL8uUyGflm3x31Gaj1hHWVPV3zrlDgpBxkLA': '4', 
        'UqYVg0DMOA4bjITnX81fOdAWCP8xIjPv0H7Y_w66l3diLTrHBLLinUTlWZVwsKUc4ud2JIZUIyOJ5A': '5', 
        'c6qwXcs0y8zZsoUuvprXb289ckVeVKzbWeIvT54DujWcEFlWgiXXdISmq8gCAPysZPMLboW8hFDlHg': '6', 
        'GSLeYAqn-ZzGTVhuR4R-EPtIFwDSSmW_QwmF6JWOrocwGugbwj7vg2ojZc7_F8QuIqmqra7qBgG3nw': '7', 
        'oUwJvToO_ANZg_rx5ib5XKtOVa9lzY9R1cXLCoi20HO0y-4AfidBrBhSj0sHMpv45hkrdmvEKrQFSw': '8', 
        'fvIR9ToQ8tBruym-hmlZxs9WUUyL8M_wrQNlByht7wrgpIXNyVw4u2DCveIIO_-pPCkHmwBNleZGJA': '9', 
        'V421Y-fOSwSWfSUZ_Od6MII_FutGBvw97xZrEEXMsukbldO9SLUC_CwrH1uslTR2ZYX4Ti9Knd-oQw': '10'
    }


def test_matchextractor_get_total_by_key_and_team_GOOD():
    extractor = match_extractor.MatchExtractor()
    total_assists_100 = extractor._get_total_by_key_and_team(
        participants_info=match_example.match_example["info"]["participants"],
        key="assists",
        team_id="100",
    )

    assert total_assists_100 == 57


def test_matchextractor_get_total_by_key_and_team_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_total_by_key_and_team(
            participants_info=match_example.match_example["info"]["participants"],
            key="truc",
            team_id="100",
        )


def test_matchextractor_get_participants_info_GOOD():
    extractor = match_extractor.MatchExtractor()
    participants_info = extractor._get_participants_info(info=match_example.match_example["info"])

    assert len(participants_info) == 10
    assert all(
        [type(participant_info) == dict for participant_info in participants_info]
    )
    assert (
        participants_info[1]["puuid"]
        == "LJtcyVp22TT4TkS8dUWRo4c3TyJqkDRq2buGqqnloVuCkHuyXOXR42X1qs3jWlwS-ltX0ZNqCbTlng"
    )


def test_matchextractor_get_participants_info_ERROR():
    extractor = match_extractor.MatchExtractor()
    participants_info = extractor._get_participants_info(info=match_example.match_example)
    
    assert participants_info == []


def test_matchextractor_get_participant_by_summoner_id_GOOD():
    extractor = match_extractor.MatchExtractor()
    participant_dict = extractor._get_participant_by_summoner_id(
        participants_info=match_example.match_example["info"]["participants"],
        summoner_id="8j6vr0mRx-znEI2NwqDS0Ejmv9yGvfd4xgtbN9_sIWGp8_JnItcPHZLcfw",
    )

    assert type(participant_dict) == dict
    assert participant_dict["summonerName"] == "quackyduck99"


def test_matchextractor_get_participant_by_summoner_id_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_participant_by_summoner_id(
            participants_info=match_example.match_example["info"]["participants"],
            summoner_id="dlslds",
        )


def test_matchextractor_get_participant_by_puuid_GOOD():
    extractor = match_extractor.MatchExtractor()
    participant_dict = extractor._get_participant_by_puuid(
        participants_info=match_example.match_example["info"]["participants"],
        puuid="bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
    )

    assert type(participant_dict) == dict
    assert participant_dict["summonerName"] == "Kanae Ruka"


def test_matchextractor_get_participant_by_puuid_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_participant_by_puuid(
            participants_info=match_example.match_example["info"]["participants"],
            puuid="dlslds",
        )


def test_matchextractor_get_opponent_participant_by_summoner_id_GOOD():
    extractor = match_extractor.MatchExtractor()
    participant_dict = extractor._get_opponent_participant_by_summoner_id(
        participants_info=match_example.match_example["info"]["participants"],
        summoner_id="8j6vr0mRx-znEI2NwqDS0Ejmv9yGvfd4xgtbN9_sIWGp8_JnItcPHZLcfw",
    )

    assert type(participant_dict) == dict
    assert participant_dict["summonerName"] == "davlaf"


def test_matchextractor_get_opponent_participant_by_summoner_id_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_opponent_participant_by_summoner_id(
            participants_info=match_example.match_example["info"]["participants"],
            summoner_id="dlslds",
        )


def test_matchextractor_get_opponent_participant_by_puuid_GOOD():
    extractor = match_extractor.MatchExtractor()
    participant_dict = extractor._get_opponent_participant_by_puuid(
        participants_info=match_example.match_example["info"]["participants"],
        puuid="bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
    )

    assert type(participant_dict) == dict
    assert participant_dict["summonerName"] == "Kennen Has A Key"


def test_matchextractor_get_opponent_participant_by_puuid_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor._get_opponent_participant_by_puuid(
            participants_info=match_example.match_example["info"]["participants"],
            puuid="dlslds",
        )


def test_matchextractor_get_kda_GOOD():
    extractor = match_extractor.MatchExtractor()
    assert extractor._get_kda(kills=10, deaths=3, assists=9) == 6.33


def test_matchextractor_get_kda_GOOD_0deaths():
    extractor = match_extractor.MatchExtractor()
    assert extractor._get_kda(kills=10, deaths=0, assists=9) == 19


def test_matchextractor_get_kda_GOOD_0assists():
    extractor = match_extractor.MatchExtractor()
    assert extractor._get_kda(kills=10, deaths=2, assists=0) == 5


def test_matchextractor_get_kda_NONE():
    extractor = match_extractor.MatchExtractor()
    assert extractor._get_kda(kills=None, deaths=3, assists=9) is None


def test_matchextractor_get_metadata_from_match_GOOD():
    extractor = match_extractor.MatchExtractor()
    metadata = extractor._get_metadata(d=match_example.match_example)
    assert metadata == {
        "dataVersion": "2",
        "matchId": "EUW1_6404768237",
        "participants": [
            "bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
            "LJtcyVp22TT4TkS8dUWRo4c3TyJqkDRq2buGqqnloVuCkHuyXOXR42X1qs3jWlwS-ltX0ZNqCbTlng",
            "ZZdcjG9YVBvH5bHVPgjjZFYR02LWFlu1V2tr1_8gPdHM2O9sHvgBTS18zHvpE8CyIZ-dFylICyErQQ",
            "uPuuLLcgzuS07Iep4aHPvq_pzn6h72zXptj_ajhKCFMigDy-EM7ttUGxhcV4dqiC5aTVa9uosB5gKQ",
            "SP8BchrfPeeWnmiTtXGpLlpk-DpOV87gsrbHOym1t144kRbCwfI83mqy-4crlaZJC_p2ZhnVkteCMQ",
            "yySCXP617QJs3Uz8SA7Gkwmo5V80VzRHMbZUby7eJBdc9OGLjm2-tgKIgFBbXFk9XZZsahPnksxEzg",
            "eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g",
            "mowuZ2O29Od7CWPP4mlssoa2VI3GNqukMg9gbicYrqnv1ljRpXj_Huft1aZ9FVeL7Q6VrM1cceVKuQ",
            "9nkx3aYjZ9wfByGqds8s73iSdukDzX-8p4vAcl88F4fif9xq-7lgugTpFM2kNh5MTDMlD7gO7ujEiQ",
            "Stbzzw_WDNFkobnTcXhDrwxJGgdi_PWPcBcSkdhLZPDbgPYK2649Ft3ByeV06PBCa2HIG6wrQyCphA",
        ],
    }


def test_matchextractor_get_metadata_from_match_ERROR():
    extractor = match_extractor.MatchExtractor()
    metadata = extractor._get_metadata(d=match_example.match_example["info"])
    assert metadata == {}


def test_matchextractor_get_info_from_match_GOOD():
    extractor = match_extractor.MatchExtractor()
    info = extractor._get_info(d=match_example.match_example)
    assert type(info) == dict
    assert info["gameCreation"] == 1684177400505


def test_matchextractor_get_info_from_match_ERROR():
    extractor = match_extractor.MatchExtractor()
    info = extractor._get_metadata(d=match_example.match_example["metadata"])
    assert info == {}


def test_matchextractor_get_participants_id():
    extractor = match_extractor.MatchExtractor()
    participants_id = extractor._get_participants_id(
        participants_info=match_example.match_example["info"]["participants"]
    )
    assert participants_id == [
        "TkLNWG5SiEUcFoduwi6jLiGCAGu2pDaX7fZGYqrJTkZH-EGe",
        "8j6vr0mRx-znEI2NwqDS0Ejmv9yGvfd4xgtbN9_sIWGp8_JnItcPHZLcfw",
        "htwMnQsrmJ6lcgj4jXK4zvO4TzV0f0nixPL-hvTYvTorSXU",
        "mgJs7N5kDkcrTXIFg4UhXdSyFKDNUOvPhs-c8QbImVkO7AI",
        "_QAIpNkYRgyisIBqu76tP2ta3TwTtwUKgLmo56H7CIavQVs",
        "ijvE3hsE-fpOJV4zBlCklmK4S4SmeZkDo0MLbuEyexWZ7ag",
        "GmrzDazS_aYqMvEg8ExGWK79lco2sEY2wi_95O8iuZDXKcQ",
        "OHR62kPBv6nKfIu6jy46twJoZCPMfa7hTDmZ7AWof6CbT1A",
        "_cwNMwHRkpnuGzzfkb-tfAHPfXdhpRxpyUfLA8eJmE6J5PU",
        "-CG6cevlMrQ2NdxsSvrNlrMzPLnL_d9LI7dMh6HdIdJOBikJ4VJPXAi3ng",
    ]


def test_matchextractor_extract_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract(["lol", "oui"])


def test_matchextractor_extract():
    extractor = match_extractor.MatchExtractor()
    m = extractor.extract(match_dict=match_example.match_example)

    assert m == Match(
        match_id="EUW1_6404768237",
        queue_id="420",
        game_version="13.9.506.4846",
        game_start_time=1684177467145,
        game_end_time=1684179127774,
        game_duration=1660,
        participants_puuid=[
            "bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
            "LJtcyVp22TT4TkS8dUWRo4c3TyJqkDRq2buGqqnloVuCkHuyXOXR42X1qs3jWlwS-ltX0ZNqCbTlng",
            "ZZdcjG9YVBvH5bHVPgjjZFYR02LWFlu1V2tr1_8gPdHM2O9sHvgBTS18zHvpE8CyIZ-dFylICyErQQ",
            "uPuuLLcgzuS07Iep4aHPvq_pzn6h72zXptj_ajhKCFMigDy-EM7ttUGxhcV4dqiC5aTVa9uosB5gKQ",
            "SP8BchrfPeeWnmiTtXGpLlpk-DpOV87gsrbHOym1t144kRbCwfI83mqy-4crlaZJC_p2ZhnVkteCMQ",
            "yySCXP617QJs3Uz8SA7Gkwmo5V80VzRHMbZUby7eJBdc9OGLjm2-tgKIgFBbXFk9XZZsahPnksxEzg",
            "eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g",
            "mowuZ2O29Od7CWPP4mlssoa2VI3GNqukMg9gbicYrqnv1ljRpXj_Huft1aZ9FVeL7Q6VrM1cceVKuQ",
            "9nkx3aYjZ9wfByGqds8s73iSdukDzX-8p4vAcl88F4fif9xq-7lgugTpFM2kNh5MTDMlD7gO7ujEiQ",
            "Stbzzw_WDNFkobnTcXhDrwxJGgdi_PWPcBcSkdhLZPDbgPYK2649Ft3ByeV06PBCa2HIG6wrQyCphA",
        ],
        participants_id=[
            "TkLNWG5SiEUcFoduwi6jLiGCAGu2pDaX7fZGYqrJTkZH-EGe",
            "8j6vr0mRx-znEI2NwqDS0Ejmv9yGvfd4xgtbN9_sIWGp8_JnItcPHZLcfw",
            "htwMnQsrmJ6lcgj4jXK4zvO4TzV0f0nixPL-hvTYvTorSXU",
            "mgJs7N5kDkcrTXIFg4UhXdSyFKDNUOvPhs-c8QbImVkO7AI",
            "_QAIpNkYRgyisIBqu76tP2ta3TwTtwUKgLmo56H7CIavQVs",
            "ijvE3hsE-fpOJV4zBlCklmK4S4SmeZkDo0MLbuEyexWZ7ag",
            "GmrzDazS_aYqMvEg8ExGWK79lco2sEY2wi_95O8iuZDXKcQ",
            "OHR62kPBv6nKfIu6jy46twJoZCPMfa7hTDmZ7AWof6CbT1A",
            "_cwNMwHRkpnuGzzfkb-tfAHPfXdhpRxpyUfLA8eJmE6J5PU",
            "-CG6cevlMrQ2NdxsSvrNlrMzPLnL_d9LI7dMh6HdIdJOBikJ4VJPXAi3ng",
        ],
    )


def test_matchextractor_extract_summoner_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_summoner(["lol", "oui"], summoner_id="kdsk")


def test_matchextractor_extract_summoner_ERROR2():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_summoner({"lol": "oui"}, summoner_id=None, puuid="")


def test_matchextractor_extract_summoner_SUMMONER_ID():
    extractor = match_extractor.MatchExtractor()
    ms = extractor.extract_summoner(
        match_dict=match_example.match_example,
        summoner_id="TkLNWG5SiEUcFoduwi6jLiGCAGu2pDaX7fZGYqrJTkZH-EGe",
    )

    assert ms == MatchSummoner(
        team_id="100",
        summoner_id="TkLNWG5SiEUcFoduwi6jLiGCAGu2pDaX7fZGYqrJTkZH-EGe",
        summoner_name="Kanae Ruka",
        summoner_puuid="bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
        champion_id="92",
        champion_name="Riven",
        champion_level=16,
        individual_position="TOP",
        team_position="TOP",
        win=True,
        kills=9,
        deaths=4,
        assists=6,
        gold_earned=12811,
        neutral_minions_killed=12, 
        total_minions_killed=203,
        total_damage_dealt_to_champions=23338,
        total_damage_taken=21949,
        vision_score=10,
        summoner1_id=4,
        summoner2_id=14,
        kda=3.75,
    )


def test_matchextractor_extract_summoner_PUUID():
    extractor = match_extractor.MatchExtractor()
    ms = extractor.extract_summoner(
        match_dict=match_example.match_example,
        puuid="bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
    )

    assert ms == MatchSummoner(
        team_id="100",
        summoner_id="TkLNWG5SiEUcFoduwi6jLiGCAGu2pDaX7fZGYqrJTkZH-EGe",
        summoner_name="Kanae Ruka",
        summoner_puuid="bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
        champion_id="92",
        champion_name="Riven",
        champion_level=16,
        individual_position="TOP",
        team_position="TOP",
        win=True,
        kills=9,
        deaths=4,
        assists=6,
        gold_earned=12811,
        neutral_minions_killed=12, 
        total_minions_killed=203,
        total_damage_dealt_to_champions=23338,
        total_damage_taken=21949,
        vision_score=10,
        summoner1_id=4,
        summoner2_id=14,
        kda=3.75,
    )


def test_matchextractor_extract_opponent_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_opponent(["lol", "oui"], summoner_id="kdsk")


def test_matchextractor_extract_opponent_ERROR2():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_opponent({"lol": "oui"}, summoner_id="", puuid=None)


def test_matchextractor_extract_opponent_SUMMONER_ID():
    extractor = match_extractor.MatchExtractor()
    ms = extractor.extract_opponent(
        match_dict=match_example.match_example,
        summoner_id="ijvE3hsE-fpOJV4zBlCklmK4S4SmeZkDo0MLbuEyexWZ7ag",
    )

    assert ms == MatchSummoner(
        team_id="100",
        summoner_id="TkLNWG5SiEUcFoduwi6jLiGCAGu2pDaX7fZGYqrJTkZH-EGe",
        summoner_name="Kanae Ruka",
        summoner_puuid="bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
        champion_id="92",
        champion_name="Riven",
        champion_level=16,
        individual_position="TOP",
        team_position="TOP",
        win=True,
        kills=9,
        deaths=4,
        assists=6,
        gold_earned=12811,
        neutral_minions_killed=12, 
        total_minions_killed=203,
        total_damage_dealt_to_champions=23338,
        total_damage_taken=21949,
        vision_score=10,
        summoner1_id=4,
        summoner2_id=14,
        kda=3.75,
    )


def test_matchextractor_extract_opponent_PUUID():
    extractor = match_extractor.MatchExtractor()
    ms = extractor.extract_opponent(
        match_dict=match_example.match_example,
        puuid="yySCXP617QJs3Uz8SA7Gkwmo5V80VzRHMbZUby7eJBdc9OGLjm2-tgKIgFBbXFk9XZZsahPnksxEzg",
    )

    assert ms == MatchSummoner(
        team_id="100",
        summoner_id="TkLNWG5SiEUcFoduwi6jLiGCAGu2pDaX7fZGYqrJTkZH-EGe",
        summoner_name="Kanae Ruka",
        summoner_puuid="bYf6lRCCzk9vKgGlIYCOj5aCoEEeeQgwJ3zA1uRdI0D0KGuOtpbazT5qbucaby93ePrA_lS-qcLUOQ",
        champion_id="92",
        champion_name="Riven",
        champion_level=16,
        individual_position="TOP",
        team_position="TOP",
        win=True,
        kills=9,
        deaths=4,
        assists=6,
        gold_earned=12811,
        neutral_minions_killed=12, 
        total_minions_killed=203,
        total_damage_dealt_to_champions=23338,
        total_damage_taken=21949,
        vision_score=10,
        summoner1_id=4,
        summoner2_id=14,
        kda=3.75,
    )



def test_matchextractor_extract_totals_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_totals(["lol", "oui"])


def test_matchextractor_extract_totals():
    extractor = match_extractor.MatchExtractor()
    totals = extractor.extract_totals(match_dict=match_example.match_example)

    assert totals == [
        TeamTotals(
            team_id=100,
            total_gold_earned=59843,
            total_assists=57,
            total_deaths=25,
            total_kills=37,
            total_neutral_minions_killed=156, 
            total_minions_killed=567,
            total_damage_dealt_to_champions=99108,
            total_damage_taken=104747,
            total_vision_score=160,
        ),
        TeamTotals(
            team_id=200,
            total_gold_earned=51099,
            total_assists=38,
            total_deaths=37,
            total_kills=25,
            total_neutral_minions_killed=114, 
            total_minions_killed=566,
            total_damage_dealt_to_champions=78915,
            total_damage_taken=118218,
            total_vision_score=136,
        ),
    ]


def test_matchextractor_extract_timeline_ERROR():
    extractor = match_extractor.MatchExtractor()
    with pytest.raises(errors.ExtractorError):
        extractor.extract_timeline(["lol", "oui"])


def test_matchextractor_extract_timeline():
    extractor = match_extractor.MatchExtractor()
    timeline = extractor.extract_timeline(match_timeline_dict=match_example.timeline_example)

    assert timeline.match_id == "EUW1_6727944035"
    assert timeline.participants_puuid == [
        "eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g",
        "KR1LzoXFfbMSgq_ij0Wj9Ph-hnXx9ImSnpJ75YLIXud6Nff8W_FUjplpgNVkdYSguyaUuPGPjL-H2w",
        "3LgDeUuEAqUBgGhZcAZzi6diNVfeLWBFiOfTOgZN2Uzdi7VY_dR_kPp5xKICQReyh9LgO-l0dLbycw",
        "AJ3DSRe7xoSH5e_7gwkMiaylGWsYg0Zxi42nHd9Sw9VL8uUyGflm3x31Gaj1hHWVPV3zrlDgpBxkLA",
        "UqYVg0DMOA4bjITnX81fOdAWCP8xIjPv0H7Y_w66l3diLTrHBLLinUTlWZVwsKUc4ud2JIZUIyOJ5A",
        "c6qwXcs0y8zZsoUuvprXb289ckVeVKzbWeIvT54DujWcEFlWgiXXdISmq8gCAPysZPMLboW8hFDlHg",
        "GSLeYAqn-ZzGTVhuR4R-EPtIFwDSSmW_QwmF6JWOrocwGugbwj7vg2ojZc7_F8QuIqmqra7qBgG3nw",
        "oUwJvToO_ANZg_rx5ib5XKtOVa9lzY9R1cXLCoi20HO0y-4AfidBrBhSj0sHMpv45hkrdmvEKrQFSw",
        "fvIR9ToQ8tBruym-hmlZxs9WUUyL8M_wrQNlByht7wrgpIXNyVw4u2DCveIIO_-pPCkHmwBNleZGJA",
        "V421Y-fOSwSWfSUZ_Od6MII_FutGBvw97xZrEEXMsukbldO9SLUC_CwrH1uslTR2ZYX4Ti9Knd-oQw"
    ]
    assert timeline.frame_interval == 60000
    assert timeline.participants_ids_map == {
        'eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g': '1', 
        'KR1LzoXFfbMSgq_ij0Wj9Ph-hnXx9ImSnpJ75YLIXud6Nff8W_FUjplpgNVkdYSguyaUuPGPjL-H2w': '2', 
        '3LgDeUuEAqUBgGhZcAZzi6diNVfeLWBFiOfTOgZN2Uzdi7VY_dR_kPp5xKICQReyh9LgO-l0dLbycw': '3', 
        'AJ3DSRe7xoSH5e_7gwkMiaylGWsYg0Zxi42nHd9Sw9VL8uUyGflm3x31Gaj1hHWVPV3zrlDgpBxkLA': '4', 
        'UqYVg0DMOA4bjITnX81fOdAWCP8xIjPv0H7Y_w66l3diLTrHBLLinUTlWZVwsKUc4ud2JIZUIyOJ5A': '5', 
        'c6qwXcs0y8zZsoUuvprXb289ckVeVKzbWeIvT54DujWcEFlWgiXXdISmq8gCAPysZPMLboW8hFDlHg': '6', 
        'GSLeYAqn-ZzGTVhuR4R-EPtIFwDSSmW_QwmF6JWOrocwGugbwj7vg2ojZc7_F8QuIqmqra7qBgG3nw': '7', 
        'oUwJvToO_ANZg_rx5ib5XKtOVa9lzY9R1cXLCoi20HO0y-4AfidBrBhSj0sHMpv45hkrdmvEKrQFSw': '8', 
        'fvIR9ToQ8tBruym-hmlZxs9WUUyL8M_wrQNlByht7wrgpIXNyVw4u2DCveIIO_-pPCkHmwBNleZGJA': '9', 
        'V421Y-fOSwSWfSUZ_Od6MII_FutGBvw97xZrEEXMsukbldO9SLUC_CwrH1uslTR2ZYX4Ti9Knd-oQw': '10'
    }
    assert len(timeline.frames) == 37
    assert timeline.frames[0].events == [{
        "realTimestamp": 1703018626410,
        "timestamp": 0,
        "type": "PAUSE_END"
        }
    ]
    assert timeline.frames[32].timestamp == 1920623
    assert timeline.frames[23].participant_frames["1"].champion_stats == TimelineChampionStats(
        ability_haste=0, 
        ability_power=0, 
        armor=136, 
        armor_pen=0, 
        armor_pen_percent=0, 
        attack_damage=218, 
        attack_speed=194, 
        bonus_armor_pen_percent=0, 
        bonus_magic_pen_percent=0, 
        cc_reduction=0, 
        cooldown_reduction=0, 
        health=2598, 
        health_max=2598, 
        health_regen=455, 
        lifesteal=0, 
        magic_pen=0,
        magic_pen_percent=0, 
        magic_resist=93, 
        movement_speed=411,
        omnivamp=0, 
        physical_vamp=0, 
        power=0, 
        power_max=0, 
        power_regen=0, 
        spell_vamp=0
    )
    assert timeline.frames[23].participant_frames["1"].current_gold == 805
    assert timeline.frames[23].participant_frames["1"].damage_stats == TimelineDamageStats(
        magic_damage_done=0, 
        magic_damage_done_to_champions=0, 
        magic_damage_taken=3559, 
        physical_damage_done=78953, 
        physical_damage_done_to_champions=4462, 
        physical_damage_taken=9532, 
        total_damage_done=82384, 
        total_damage_done_to_champions=5288, 
        total_damage_taken=14107, 
        true_damage_done=3430, 
        true_damage_done_to_champions=825, 
        true_damage_taken=1015
    )
    assert timeline.frames[23].participant_frames["1"].gold_per_second == 0
    assert timeline.frames[23].participant_frames["1"].jungle_minions_killed == 0
    assert timeline.frames[23].participant_frames["1"].level == 13
    assert timeline.frames[23].participant_frames["1"].minions_killed == 170
    assert timeline.frames[23].participant_frames["1"].participant_id == "1"
    assert timeline.frames[23].participant_frames["1"].position == {'x': 6371, 'y': 940}
    assert timeline.frames[23].participant_frames["1"].time_enemy_spent_controlled == 110439
    assert timeline.frames[23].participant_frames["1"].total_gold == 7760
