from rito import RitoClient, ExtractorClient
from rito.apis import account_api
from rito.apis import champion_mastery_api
from rito.apis import data_dragon_api
from rito.apis import league_api
from rito.apis import match_api
from rito.apis import spectator_api
from rito.apis import static_api
from rito.apis import summoner_api
from rito.extractors import account_extractor
from rito.extractors import champion_mastery_extractor
from rito.extractors import league_extractor
from rito.extractors import match_extractor
from rito.extractors import spectator_extractor
from rito.extractors import summoner_extractor


def test_ritoclient():
    rito = RitoClient(riot_api_key="riot_api_key", region="EUW")
    
    assert type(rito.account) == account_api.AccountAPIV1
    assert type(rito.champion_mastery) == champion_mastery_api.ChampionMasteryAPIV4
    assert type(rito.league) == league_api.LeagueAPIV4
    assert type(rito.match) == match_api.MatchAPIV5
    assert type(rito.spectator) == spectator_api.SpectatorAPIV4
    assert type(rito.summoner) == summoner_api.SummonerAPIV4
    assert type(rito.data_dragon) == data_dragon_api.DataDragonAPI
    assert type(rito.static) == static_api.StaticAPI


def test_extractorclient():
    extractor = ExtractorClient()

    assert type(extractor.account) == account_extractor.AccountExtractor
    assert type(extractor.champion_mastery) == champion_mastery_extractor.ChampionMasteryExtractor
    assert type(extractor.league) == league_extractor.LeagueExtractor
    assert type(extractor.match) == match_extractor.MatchExtractor
    assert type(extractor.spectator) == spectator_extractor.SpectatorExtractor
    assert type(extractor.summoner) == summoner_extractor.SummonerExtractor
