from rito.apis.base_api import BaseRiotAPI
from rito.models.champion_mastery import ChampionMastery


class ChampionMasteryAPIV4(BaseRiotAPI):
    def by_puuid(self, puuid: str) -> list[ChampionMastery]:
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
        l = self.riot_request.make_request(endpoint=endpoint)
        result = ChampionMastery()
        return [result.parse(json=j) for j in l]

    def by_puuid_by_champion(self, puuid: str, champion_id: int) -> ChampionMastery:
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = ChampionMastery()
        return result.parse(json=j)

    def by_puuid_top(self, puuid: str, count: int = 3) -> list[ChampionMastery]:
        params = {"count": count} 
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"
        l = self.riot_request.make_request(endpoint=endpoint, params=params)
        result = ChampionMastery()
        return [result.parse(json=j) for j in l]

    def scores_by_puuid(self, puuid: str) -> int:
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/scores/by-puuid/{puuid}"
        score = self.riot_request.make_request(endpoint=endpoint)
        return score
