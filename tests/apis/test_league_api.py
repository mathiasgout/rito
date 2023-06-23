from rito.apis import league_api, base_api
from rito import riot_request


def test_entryapi():
    entries_api = league_api.EntriesAPI(
        riot_api_key="riot_api_key",
        routes={
            "regional": "https://europe.api.riotgames.com",
            "platform": "https://euw1.api.riotgames.com",
        },
        riot_request=riot_request.RiotRequest("riot_api_key"),
    )

    assert entries_api.riot_api_key == "riot_api_key"
    assert entries_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert isinstance(entries_api.riot_request, riot_request.RiotRequest)


def test_entryapi_by_summoner(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    entries_api = league_api.EntriesAPI(
        riot_api_key="riot_api_key",
        routes={
            "regional": "https://europe.api.riotgames.com",
            "platform": "https://euw1.api.riotgames.com",
        },
        riot_request=riot_request.RiotRequest("riot_api_key"),
    )
    entries_api.by_summoner("summoner_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/summoner_id1"
    )


def test_entryapi_by_rank(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    entries_api = league_api.EntriesAPI(
        riot_api_key="riot_api_key",
        routes={
            "regional": "https://europe.api.riotgames.com",
            "platform": "https://euw1.api.riotgames.com",
        },
        riot_request=riot_request.RiotRequest("riot_api_key"),
    )
    entries_api.by_rank(queue="RANKED_SOLO_5v5", tier="DIAMOND", division="I", page=2)

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5v5/DIAMOND/I",
        params={"page": 2},
    )


def test_leagueapiv4():
    l_api = league_api.LeagueAPIV4(riot_api_key="riot_api_key", region="EUW")

    assert issubclass(league_api.LeagueAPIV4, base_api.BaseRiotAPI)
    assert isinstance(l_api.entries, league_api.EntriesAPI)
