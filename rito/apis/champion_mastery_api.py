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
