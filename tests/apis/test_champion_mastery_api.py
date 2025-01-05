from rito.apis import champion_mastery_api, base_api
from rito.models import champion_mastery
from rito import riot_request


def test_championmasteryapiv4():
    assert issubclass(champion_mastery_api.ChampionMasteryAPIV4, base_api.BaseRiotAPI)


def test_championmasteryapiv4_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=[{"lol": "xd"}])

    # Calls
    cm_api = champion_mastery_api.ChampionMasteryAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = cm_api.by_puuid("puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/puuid1"
    )
    assert type(return_value) == list
    assert len(return_value) == 1
    assert return_value[0]._json == {"lol": "xd"}


def test_championmasteryapiv4_by_puuid_by_champion(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    cm_api = champion_mastery_api.ChampionMasteryAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = cm_api.by_puuid_by_champion("puuid1", "1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/puuid1/by-champion/1"
    )
    assert type(return_value) == champion_mastery.ChampionMastery
    assert return_value._json == {"lol": "xd"}


def test_championmasteryapiv4_by_puuid_top(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=[{"lol": "xd"}])

    # Calls
    cm_api = champion_mastery_api.ChampionMasteryAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = cm_api.by_puuid_top(puuid="puuid1", count=2)

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/puuid1/top",
        params={"count": 2}
    )
    assert type(return_value) == list
    assert len(return_value) == 1
    assert return_value[0]._json == {"lol": "xd"}


def test_championmasteryapiv4_scores_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=1)

    # Calls
    cm_api = champion_mastery_api.ChampionMasteryAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = cm_api.scores_by_puuid(puuid="puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/puuid1"
    )
    assert return_value == 1
