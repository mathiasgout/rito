from rito.apis.champion_mastery_api import ChampionMasteryAPIV4
from rito.apis.league_api import LeagueAPIV4
from rito.apis.match_api import MatchAPIV5
from rito.apis.spectator_api import SpectatorAPIV4
from rito.apis.summoner_api import SummonerAPIV4
from rito.apis.data_dragon_api import DataDragonAPI
from rito.apis.static_api import StaticAPI
from rito.extractors.champion_mastery_extractor import ChampionMasteryExtractor
from rito.extractors.league_extractor import LeagueExtractor
from rito.extractors.match_extractor import MatchExtractor
from rito.extractors.spectator_extractor import SpectatorExtractor
from rito.extractors.summoner_extractor import SummonerExtractor


class RitoClient:
    def __init__(self, riot_api_key: str, region: str, tries_5xx: int = 5) -> None:
        self.champion_mastery = ChampionMasteryAPIV4(
            riot_api_key, region, tries_5xx=tries_5xx
        )
        self.league = LeagueAPIV4(riot_api_key, region, tries_5xx=tries_5xx)
        self.match = MatchAPIV5(riot_api_key, region, tries_5xx=tries_5xx)
        self.spectator = SpectatorAPIV4(riot_api_key, region, tries_5xx=tries_5xx)
        self.summoner = SummonerAPIV4(riot_api_key, region, tries_5xx=tries_5xx)
        self.data_dragon = DataDragonAPI(riot_api_key, region, tries_5xx=tries_5xx)
        self.static = StaticAPI(riot_api_key, region, tries_5xx=tries_5xx)


class ExtractorClient:
    def __init__(self) -> None:
        self.champion_mastery = ChampionMasteryExtractor()
        self.league = LeagueExtractor()
        self.match = MatchExtractor()
        self.spectator = SpectatorExtractor()
        self.summoner = SummonerExtractor()
