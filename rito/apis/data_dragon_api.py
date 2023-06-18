from rito.apis.base_api import BaseRiotAPI

from typing import Union


class DataDragonAPI(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def versions(self) -> Union[None, list[str]]:
        endpoint = "https://ddragon.leagueoflegends.com/api/versions.json"
        return self.riot_request.make_request(endpoint=endpoint)

    def champions(self, version: str) -> Union[None, dict]:
        endpoint = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
        return self.riot_request.make_request(endpoint=endpoint)
