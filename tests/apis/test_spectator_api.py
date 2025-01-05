from rito.apis import spectator_api, base_api
from rito.models import spectator
from rito import riot_request


def test_spectatorapiv5():
    ag_api = spectator_api.SpectatorAPIV5(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    assert issubclass(spectator_api.SpectatorAPIV5, base_api.BaseRiotAPI)
    assert isinstance(ag_api.active_game, spectator_api.ActiveGameAPI)
    assert isinstance(ag_api.featured_games, spectator_api.FeaturedGamesAPI)



def test_activegameapi():
    ag_api = spectator_api.ActiveGameAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    assert ag_api.riot_api_key == "riot_api_key"
    assert ag_api.region == "EUW"
    assert ag_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert isinstance(ag_api.riot_request, riot_request.RiotRequest)


def test_activegameapi_by_summoner(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    ag_api = spectator_api.ActiveGameAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = ag_api.by_summoner("summoner_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/summoner_id1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == spectator.ActiveGame


def test_featuredgamesapi():
    fg_api = spectator_api.FeaturedGamesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    assert fg_api.riot_api_key == "riot_api_key"
    assert fg_api.region == "EUW"
    assert fg_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert isinstance(fg_api.riot_request, riot_request.RiotRequest)


def test_featuredgamesapi_game_list(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    fg_api = spectator_api.FeaturedGamesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = fg_api.game_list()

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/spectator/v5/featured-games"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == spectator.FeaturedGames
