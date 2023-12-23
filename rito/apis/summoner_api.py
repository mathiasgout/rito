from rito.apis.base_api import BaseRiotAPI

from typing import Union


class SummonerAPIV4(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def by_name(self, name: str) -> Union[None, dict]:
        endpoint = f"{self.routes['platform']}/lol/summoner/v4/summoners/by-name/{name}"
        return self.riot_request.make_request(endpoint=endpoint)

    def by_id(self, summoner_id: str) -> Union[None, dict]:
        endpoint = f"{self.routes['platform']}/lol/summoner/v4/summoners/{summoner_id}"
        return self.riot_request.make_request(endpoint=endpoint)

    def by_account(self, account_id: str) -> Union[None, dict]:
        endpoint = f"{self.routes['platform']}/lol/summoner/v4/summoners/by-account/{account_id}"
        return self.riot_request.make_request(endpoint=endpoint)

    def by_puuid(self, puuid: str) -> Union[None, dict]:
        endpoint = f"{self.routes['platform']}/lol/summoner/v4/summoners/by-puuid/{puuid}"
        return self.riot_request.make_request(endpoint=endpoint)
