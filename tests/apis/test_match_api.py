from rito.apis import match_api, base_api
from rito.models import match
from rito import riot_request


def test_matchapiv5():
    assert issubclass(match_api.MatchAPIV5, base_api.BaseRiotAPI)


def test_matchapiv5_list_by_puuid(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=["match1", "match2"])

    # Calls
    m_api = match_api.MatchAPIV5(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = m_api.list_by_puuid("summoner_puuid1")

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
    assert return_value == ["match1", "match2"]


def test_matchapiv5_by_match_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    m_api = match_api.MatchAPIV5(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = m_api.by_match_id("match_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/lol/match/v5/matches/match_id1"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == match.Match


def test_matchapiv5_timeline_by_match_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    m_api = match_api.MatchAPIV5(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = m_api.timeline_by_match_id("match_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://europe.api.riotgames.com/lol/match/v5/matches/match_id1/timeline"
    )
    assert return_value._json == {"lol": "xd"}
    assert type(return_value) == match.Timeline
