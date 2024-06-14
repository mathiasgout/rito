from rito.apis import league_api, base_api
from rito.models import league
from rito import riot_request


def test_entriesapi():
    entries_api = league_api.EntriesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    assert entries_api.riot_api_key == "riot_api_key"
    assert entries_api.region == "EUW"
    assert entries_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert isinstance(entries_api.riot_request, riot_request.RiotRequest)


def test_entriesapi_by_summoner(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=[{"lol": "xd"}])

    # Calls
    entries_api = league_api.EntriesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = entries_api.by_summoner("summoner_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/summoner_id1"
    )
    assert len(return_value) == 1
    assert type(return_value[0]) == league.Entry
    assert return_value[0]._json == {"lol": "xd"}


def test_entriesapi_by_rank(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=[{"lol": "xd"}])

    # Calls
    entries_api = league_api.EntriesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = entries_api.by_rank(queue="RANKED_SOLO_5v5", tier="DIAMOND", division="I", page=2)

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5v5/DIAMOND/I",
        params={"page": 2},
    )
    assert len(return_value) == 1
    assert type(return_value[0]) == league.Entry
    assert return_value[0]._json == {"lol": "xd"}


def test_leaguesapi():
    leagues_api = league_api.LeaguesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    assert leagues_api.riot_api_key == "riot_api_key"
    assert leagues_api.region == "EUW"
    assert leagues_api.routes == {
        "regional": "https://europe.api.riotgames.com",
        "platform": "https://euw1.api.riotgames.com",
    }
    assert isinstance(leagues_api.riot_request, riot_request.RiotRequest)


def test_leaguesapi_by_league_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    leagues_api = league_api.LeaguesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = leagues_api.by_league_id("league_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league/v4/leagues/league_id1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == league.League


def test_leaguesapi_challenger_leagues_by_queue(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    leagues_api = league_api.LeaguesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = leagues_api.challenger_leagues_by_queue("queue1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/queue1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == league.League


def test_leaguesapi_grandmaster_leagues_by_queue(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    leagues_api = league_api.LeaguesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = leagues_api.grandmaster_leagues_by_queue("queue1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/queue1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == league.League


def test_leaguesapi_master_leagues_by_queue(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    leagues_api = league_api.LeaguesAPI(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = leagues_api.master_leagues_by_queue("queue1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/queue1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == league.League


def test_leagueapiv4():
    l_api = league_api.LeagueAPIV4(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    assert issubclass(league_api.LeagueAPIV4, base_api.BaseRiotAPI)
    assert isinstance(l_api.entries, league_api.EntriesAPI)
    assert isinstance(l_api.leagues, league_api.LeaguesAPI)
