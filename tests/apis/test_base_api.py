from rito.apis import base_api
from rito import riot_request


def test_baseapiriot():
    base_riot_api = base_api.BaseRiotAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    assert base_riot_api.riot_api_key == "riot_api_key"
    assert base_riot_api.region == "EUW"
    assert base_riot_api.return_none_on_404 is True
    assert base_riot_api.retry_on_rate_limit is True
    assert base_riot_api.timeout_on_servor_error == 10
    assert base_riot_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert type(base_riot_api.riot_request) == riot_request.RiotRequest
