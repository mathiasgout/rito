from rito.apis.base_api import BaseRiotAPI
from rito.models.summoner import Summoner


class SummonerAPIV4(BaseRiotAPI):
    def by_id(self, summoner_id: str) -> Summoner:
        endpoint = f"{self.routes['platform']}/lol/summoner/v4/summoners/{summoner_id}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = Summoner()
        return result.parse(json=j)

    def by_account(self, account_id: str) -> Summoner:
        endpoint = f"{self.routes['platform']}/lol/summoner/v4/summoners/by-account/{account_id}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = Summoner()
        return result.parse(json=j)

    def by_puuid(self, puuid: str) -> Summoner:
        endpoint = f"{self.routes['platform']}/lol/summoner/v4/summoners/by-puuid/{puuid}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = Summoner()
        return result.parse(json=j)
