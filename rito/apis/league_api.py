from rito.apis.base_api import BaseRiotAPI
from rito.models.league import Entry, League


class EntriesAPI(BaseRiotAPI):
    def by_summoner(self, summoner_id: str) -> list[Entry]:
        endpoint = f"{self.routes['platform']}/lol/league/v4/entries/by-summoner/{summoner_id}"
        l = self.riot_request.make_request(endpoint=endpoint)
        result = Entry()
        return [result.parse(json=j) for j in l]

    def by_rank(self, queue: str, tier: str, division: str, page: int = 1) -> list[Entry]:
        params = {"page": page}
        endpoint = f"{self.routes['platform']}/lol/league-exp/v4/entries/{queue}/{tier}/{division}"
        l = self.riot_request.make_request(endpoint=endpoint, params=params)
        result = Entry()
        return [result.parse(json=j) for j in l]


class LeaguesAPI(BaseRiotAPI):
    def by_league_id(self, league_id: str) -> League:
        endpoint = f"{self.routes['platform']}/lol/league/v4/leagues/{league_id}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = League()
        return result.parse(json=j)

    def challenger_leagues_by_queue(self, queue: str) -> League:
        endpoint = f"{self.routes['platform']}/lol/league/v4/challengerleagues/by-queue/{queue}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = League()
        return result.parse(json=j)
    
    def grandmaster_leagues_by_queue(self, queue: str) -> League:
        endpoint = f"{self.routes['platform']}/lol/league/v4/grandmasterleagues/by-queue/{queue}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = League()
        return result.parse(json=j)
    
    def master_leagues_by_queue(self, queue: str) -> League:
        endpoint = f"{self.routes['platform']}/lol/league/v4/masterleagues/by-queue/{queue}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = League()
        return result.parse(json=j)


class LeagueAPIV4(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.entries = EntriesAPI(self.riot_api_key, self.region, self.return_none_on_404, self.retry_on_rate_limit, self.timeout_on_servor_error)
        self.leagues = LeaguesAPI(self.riot_api_key, self.region, self.return_none_on_404, self.retry_on_rate_limit, self.timeout_on_servor_error)
