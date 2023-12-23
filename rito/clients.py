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
    def __init__(self, riot_api_key: str, region: str, timeout: int = 300, tries_max: int = 5) -> None:
        self.champion_mastery = ChampionMasteryAPIV4(riot_api_key, region, timeout, tries_max)
        self.league = LeagueAPIV4(riot_api_key, region, timeout, tries_max)
        self.match = MatchAPIV5(riot_api_key, region, timeout, tries_max)
        self.spectator = SpectatorAPIV4(riot_api_key, region, timeout, tries_max)
        self.summoner = SummonerAPIV4(riot_api_key, region, timeout, tries_max)
        self.data_dragon = DataDragonAPI(riot_api_key, region, timeout, tries_max)
        self.static = StaticAPI(riot_api_key, region, timeout, tries_max)


class ExtractorClient:
    def __init__(self) -> None:
        self.champion_mastery = ChampionMasteryExtractor()
        self.league = LeagueExtractor()
        self.match = MatchExtractor()
        self.spectator = SpectatorExtractor()
        self.summoner = SummonerExtractor()
