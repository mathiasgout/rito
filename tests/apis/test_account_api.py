from rito.apis import account_api, base_api
from rito import riot_request


def test_accountapiv1():
    assert issubclass(account_api.AccountAPIV1, base_api.BaseRiotAPI)


def test_accountapiv1_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    a_api = account_api.AccountAPIV1(riot_api_key="riot_api_key", region="EUW")
    a_api.by_puuid("puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/puuid1"
    )


def test_accountapiv1_by_riot_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    a_api = account_api.AccountAPIV1(riot_api_key="riot_api_key", region="EUW")
    a_api.by_riot_id("game_name1", "tag_line1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/game_name1/tag_line1"
    )
