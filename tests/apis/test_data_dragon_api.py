from rito.apis import data_dragon_api, base_api
from rito import riot_request


def test_datadragonapi():
    assert issubclass(data_dragon_api.DataDragonAPI, base_api.BaseRiotAPI)


def test_datadragonapi_versions(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    dd_api = data_dragon_api.DataDragonAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    dd_api.versions

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://ddragon.leagueoflegends.com/api/versions.json"
    )


def test_datadragonapi_champions(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    dd_api = data_dragon_api.DataDragonAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    dd_api.champions("version1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://ddragon.leagueoflegends.com/cdn/version1/data/en_US/champion.json"
    )
