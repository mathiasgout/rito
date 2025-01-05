from rito import RitoClient
from rito.apis import account_api
from rito.apis import champion_mastery_api
from rito.apis import data_dragon_api
from rito.apis import league_api
from rito.apis import match_api
from rito.apis import spectator_api
from rito.apis import static_api
from rito.apis import summoner_api
from rito.apis import challenges_api
from rito.apis import champion_api


def test_ritoclient():
    rito = RitoClient(riot_api_key="riot_api_key", region="EUW")
    
    assert type(rito.account) == account_api.AccountAPIV1
    assert type(rito.champion_mastery) == champion_mastery_api.ChampionMasteryAPIV4
    assert type(rito.league) == league_api.LeagueAPIV4
    assert type(rito.match) == match_api.MatchAPIV5
    assert type(rito.spectator) == spectator_api.SpectatorAPIV5
    assert type(rito.summoner) == summoner_api.SummonerAPIV4
    assert type(rito.data_dragon) == data_dragon_api.DataDragonAPI
    assert type(rito.static) == static_api.StaticAPI
    assert type(rito.challenges) == challenges_api.ChallengesV1
    assert type(rito.champion) == champion_api.ChampionV3
