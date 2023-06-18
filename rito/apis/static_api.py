from rito.apis.base_api import BaseRiotAPI

from typing import Union


class StaticAPI(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def queues(self) -> Union[None, list[dict]]:
        endpoint = f"https://static.developer.riotgames.com/docs/lol/queues.json"
        return self.riot_request.make_request(endpoint=endpoint)
