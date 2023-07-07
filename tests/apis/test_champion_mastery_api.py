from rito.apis import champion_mastery_api, base_api
from rito import riot_request


def test_championmasteryapiv4():
    assert issubclass(champion_mastery_api.ChampionMasteryAPIV4, base_api.BaseRiotAPI)


def test_championmasteryapiv4_by_summoner(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    cm_api = champion_mastery_api.ChampionMasteryAPIV4(
        riot_api_key="riot_api_key", region="EUW"
    )
    cm_api.masteries_by_summoner("summoner_id1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/summoner_id1/top",
        params={"count": 500},
    )


def test_championmasteryapiv4_by_summoner_and_champion(mocker):
    # Patchs
    mocker.patch("rito.riot_request.RiotRequest.make_request")

    # Calls
    cm_api = champion_mastery_api.ChampionMasteryAPIV4(
        riot_api_key="riot_api_key", region="EUW"
    )
    cm_api.by_summoner_and_champion("summoner_id1", "1")

    # Verifs
    riot_request.RiotRequest.make_request.assert_called_once_with(
        endpoint="https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/summoner_id1/by-champion/1"
    )
