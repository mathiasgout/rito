from rito.apis.base_api import BaseRiotAPI

from typing import Union


class ChampionMasteryAPIV4(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def masteries_by_summoner(self, summoner_id: str) -> Union[None, list[dict]]:
        params = {"count": 500}
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/top"
        return self.riot_request.make_request(endpoint=endpoint, params=params)

    def by_summoner_and_champion(self, summoner_id: str, champion_id: int) -> Union[None, dict]:
        endpoint = f"{self.routes['platform']}/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}"
        return self.riot_request.make_request(endpoint=endpoint)
