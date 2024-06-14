from rito.apis import account_api, base_api
from rito.models import account
from rito import riot_request


def test_accountapiv1():
    assert issubclass(account_api.AccountAPIV1, base_api.BaseRiotAPI)


def test_accountapiv1_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    a_api = account_api.AccountAPIV1(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = a_api.by_puuid("puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/puuid1"
    )
    assert type(return_value) == account.Account
    assert return_value._json == {"lol": "xd"}


def test_accountapiv1_by_riot_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    a_api = account_api.AccountAPIV1(        
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = a_api.by_riot_id("game_name1", "tag_line1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/game_name1/tag_line1"
    )
    assert type(return_value) == account.Account
    assert return_value._json == {"lol": "xd"}
