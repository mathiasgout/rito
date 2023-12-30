from rito.apis.base_api import BaseRiotAPI

from typing import Union


class ChampionMasteryAPIV4(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def by_puuid(self, puuid: str) -> Union[None, list[dict]]:
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
        return self.riot_request.make_request(endpoint=endpoint)

    def by_puuid_by_champion(self, puuid: str, champion_id: int) -> Union[None, dict]:
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
        return self.riot_request.make_request(endpoint=endpoint)
