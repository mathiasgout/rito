from rito.apis import spectator_api, base_api
from rito import riot_request


def test_entryapi():
    ag_api = spectator_api.ActiveGameAPI(
        riot_api_key="riot_api_key",
        routes={
            "regional": "https://europe.api.riotgames.com",
            "platform": "https://euw1.api.riotgames.com",
        },
        riot_request=riot_request.RiotRequest("riot_api_key"),
    )

    assert ag_api.riot_api_key == "riot_api_key"
    assert ag_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert isinstance(ag_api.riot_request, riot_request.RiotRequest)


def test_entryapi_by_summoner(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    ag_api = spectator_api.ActiveGameAPI(
        riot_api_key="riot_api_key",
        routes={
            "regional": "https://europe.api.riotgames.com",
            "platform": "https://euw1.api.riotgames.com",
        },
        riot_request=riot_request.RiotRequest("riot_api_key"),
    )
    ag_api.by_summoner("summoner_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/summoner_id1"
    )


def test_leagueapiv4():
    ag_api = spectator_api.SpectatorAPIV4(riot_api_key="riot_api_key", region="EUW")

    assert issubclass(spectator_api.SpectatorAPIV4, base_api.BaseRiotAPI)
    assert isinstance(ag_api.active_game, spectator_api.ActiveGameAPI)
