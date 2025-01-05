from rito.apis import challenges_api, base_api
from rito.models import challenges
from rito import riot_request


def test_championsv1():
    assert issubclass(challenges_api.ChallengesV1, base_api.BaseRiotAPI)


def test_championsv1_config(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=[{"lol": "xd"}])

    # Calls
    c_api = challenges_api.ChallengesV1(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = c_api.config()

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/challenges/v1/challenges/config"
    )
    assert type(return_value) == list
    assert len(return_value) == 1
    assert return_value[0]._json == {"lol": "xd"}


def test_championsv1_percentiles(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    c_api = challenges_api.ChallengesV1(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = c_api.percentiles()

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/challenges/v1/challenges/percentiles"
    )
    assert type(return_value) == dict
    assert return_value == {"lol": "xd"}


def test_championsv1_config_by_challenge_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    c_api = challenges_api.ChallengesV1(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = c_api.config_by_challenge_id("1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/challenges/v1/challenges/1/config"
    )
    assert type(return_value) == challenges.ChallengesConfig
    assert return_value._json == {"lol": "xd"}


def test_championsv1_percentiles_by_challenge_id(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    c_api = challenges_api.ChallengesV1(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = c_api.percentiles_by_challenge_id("1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/challenges/v1/challenges/1/percentiles"
    )
    assert type(return_value) == dict
    assert return_value == {"lol": "xd"}


def test_championsv1_leaderboards_by_challenge_id_by_level(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value=[{"lol": "xd"}])

    # Calls
    c_api = challenges_api.ChallengesV1(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = c_api.leaderboards_by_challenge_id_by_level(challenge_id="1", level="MASTER", limit=2)

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/challenges/v1/challenges/1/leaderboards/by-level/MASTER",
        params={"limit": 2}
    )
    assert type(return_value) == list
    assert len(return_value) == 1
    assert return_value[0]._json == {"lol": "xd"}


def test_championsv1_player_information(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request", return_value={"lol": "xd"})

    # Calls
    c_api = challenges_api.ChallengesV1(
        riot_api_key="riot_api_key", 
        region="EUW",
        return_none_on_404=True,
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = c_api.player_information(puuid="puuid1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/challenges/v1/player-data/puuid1"
    )
    assert type(return_value) == challenges.ChallengesPlayerInformation
    assert return_value._json == {"lol": "xd"}
