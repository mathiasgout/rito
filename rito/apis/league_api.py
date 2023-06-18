from rito.apis.base_api import BaseRiotAPI

from typing import Union


class EntriesAPI:
    def __init__(self, riot_api_key: str, routes: dict, riot_request) -> None:
        self.riot_api_key = riot_api_key
        self.routes = routes
        self.riot_request = riot_request

    def by_summoner(self, summoner_id: str) -> Union[None, list[dict]]:
        endpoint = (
            f"{self.routes['platform']}/lol/league/v4/entries/by-summoner/{summoner_id}"
        )
        return self.riot_request.make_request(endpoint=endpoint)

    def by_rank(
        self, queue: str, tier: str, division: str, page: int = 1
    ) -> Union[None, list[dict]]:
        params = {"page": page}
        endpoint = f"{self.routes['platform']}/lol/league-exp/v4/entries/{queue}/{tier}/{division}"
        return self.riot_request.make_request(endpoint=endpoint, params=params)


class LeagueAPIV4(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.entries = EntriesAPI(
            riot_api_key=self.riot_api_key,
            routes=self.routes,
            riot_request=self.riot_request,
        )
