from rito.apis import static_api, base_api
from rito import riot_request


def test_staticapi():
    assert issubclass(static_api.StaticAPI, base_api.BaseRiotAPI)


def test_staticapi_queues(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    s_api = static_api.StaticAPI(riot_api_key="riot_api_key", region="EUW")
    s_api.queues

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://static.developer.riotgames.com/docs/lol/queues.json"
    )
