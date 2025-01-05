from rito.apis import champion_api, base_api
from rito.models import champion
from rito import riot_request


def test_championv3():
    assert issubclass(champion_api.ChampionV3, base_api.BaseRiotAPI)


def test_championapiv3_champion_rotations(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    c_api = champion_api.ChampionV3(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = c_api.champion_rotations()

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations"
    )
    assert type(return_value) == champion.ChampionRotations
    assert return_value._json == {"lol": "xd"}
