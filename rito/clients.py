from rito.apis.account_api import AccountAPIV1
from rito.apis.challenges_api import ChallengesV1
from rito.apis.champion_mastery_api import ChampionMasteryAPIV4
from rito.apis.champion_api import ChampionV3
from rito.apis.league_api import LeagueAPIV4
from rito.apis.match_api import MatchAPIV5
from rito.apis.spectator_api import SpectatorAPIV5
from rito.apis.summoner_api import SummonerAPIV4
from rito.apis.data_dragon_api import DataDragonAPI
from rito.apis.static_api import StaticAPI


class RitoClient:
    def __init__(
        self, 
        riot_api_key: str, 
        region: str,
        return_none_on_404: bool = True,
        retry_on_rate_limit: bool = True, 
        timeout_on_servor_error: int = 600
    ) -> None:
        self.account = AccountAPIV1(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.challenges = ChallengesV1(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.champion_mastery = ChampionMasteryAPIV4(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.champion = ChampionV3(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.league = LeagueAPIV4(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.match = MatchAPIV5(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.spectator = SpectatorAPIV5(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.summoner = SummonerAPIV4(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.data_dragon = DataDragonAPI(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
        self.static = StaticAPI(riot_api_key, region, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
