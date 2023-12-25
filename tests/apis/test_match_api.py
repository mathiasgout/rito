from rito.apis import match_api, base_api
from rito import riot_request


def test_matchapiv5():
    assert issubclass(match_api.MatchAPIV5, base_api.BaseRiotAPI)


def test_matchapiv5_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    m_api = match_api.MatchAPIV5(riot_api_key="riot_api_key", region="EUW")
    m_api.list_by_puuid("summoner_puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/summoner_puuid1/ids",
        params={
            "startTime": None,
            "endTime": None,
            "queue": None,
            "type": None,
            "start": None,
            "count": 20,
        },
    )


def test_matchapiv5_by_match_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    m_api = match_api.MatchAPIV5(riot_api_key="riot_api_key", region="EUW")
    m_api.by_match_id("match_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/lol/match/v5/matches/match_id1"
    )


def test_matchapiv5_timeline_by_match_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    m_api = match_api.MatchAPIV5(riot_api_key="riot_api_key", region="EUW")
    m_api.timeline_by_match_id("match_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/lol/match/v5/matches/match_id1/timeline"
    )
