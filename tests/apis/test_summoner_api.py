from rito.apis import summoner_api, base_api
from rito.models import summoner
from rito import riot_request


def test_summonerapiv4():
    assert issubclass(summoner_api.SummonerAPIV4, base_api.BaseRiotAPI)


def test_summonerapiv4_by_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    s_api = summoner_api.SummonerAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = s_api.by_id("summoner_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/summoner_id1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == summoner.Summoner


def test_summonerapiv4_by_account(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    s_api = summoner_api.SummonerAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = s_api.by_account("account1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-account/account1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == summoner.Summoner


def test_summonerapiv4_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    s_api = summoner_api.SummonerAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = s_api.by_puuid("puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/puuid1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == summoner.Summoner
