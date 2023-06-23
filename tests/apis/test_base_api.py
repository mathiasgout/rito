from rito.apis import base_api
from rito import riot_request


def test_baseapiriot():
    base_riot_api = base_api.BaseRiotAPI(
        riot_api_key="riot_api_key", region="EUW", tries_5xx=6
    )

    assert base_riot_api.riot_api_key == "riot_api_key"
    assert base_riot_api.region == "EUW"
    assert base_riot_api.tries_5xx == 6
    assert base_riot_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert type(base_riot_api.riot_request) == riot_request.RiotRequest
