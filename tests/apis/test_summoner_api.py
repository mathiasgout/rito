from rito.apis import summoner_api, base_api
from rito import riot_request


def test_summonerapiv4():
    assert issubclass(summoner_api.SummonerAPIV4, base_api.BaseRiotAPI)


def test_summonerapiv4_by_name(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    s_api = summoner_api.SummonerAPIV4(riot_api_key="riot_api_key", region="EUW")
    s_api.by_name("name1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/name1"
    )


def test_summonerapiv4_by_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    s_api = summoner_api.SummonerAPIV4(riot_api_key="riot_api_key", region="EUW")
    s_api.by_id("summoner_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/summoner_id1"
    )


def test_summonerapiv4_by_account(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    s_api = summoner_api.SummonerAPIV4(riot_api_key="riot_api_key", region="EUW")
    s_api.by_account("account1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-account/account1"
    )


def test_summonerapiv4_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    s_api = summoner_api.SummonerAPIV4(riot_api_key="riot_api_key", region="EUW")
    s_api.by_puuid("puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/puuid1"
    )
