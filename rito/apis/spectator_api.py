from rito.apis.base_api import BaseRiotAPI

from typing import Union


class ActiveGameAPI:
    def __init__(self, riot_api_key: str, routes: dict, riot_request) -> None:
        self.riot_api_key = riot_api_key
        self.routes = routes
        self.riot_request = riot_request

    def by_summoner(self, summoner_id: str) -> Union[None, dict]:
        endpoint = f"{self.routes['platform']}/lol/spectator/v4/active-games/by-summoner/{summoner_id}"
        return self.riot_request.make_request(endpoint=endpoint)


class SpectatorAPIV4(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.active_game = ActiveGameAPI(
            riot_api_key=self.riot_api_key,
            routes=self.routes,
            riot_request=self.riot_request,
        )
