from rito.apis.base_api import BaseRiotAPI

from typing import Union


class AccountAPIV1(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def by_puuid(self, puuid: str) -> Union[None, dict]:
        endpoint = f"{self.routes['regional']}/riot/account/v1/accounts/by-puuid/{puuid}"
        return self.riot_request.make_request(endpoint=endpoint)

    def by_riot_id(self, game_name: str, tag_line: str) -> Union[None, dict]:
        endpoint = f"{self.routes['regional']}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        return self.riot_request.make_request(endpoint=endpoint)
