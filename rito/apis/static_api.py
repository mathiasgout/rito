from rito.apis.base_api import BaseRiotAPI


class StaticAPI(BaseRiotAPI):
    @property
    def queues(self) -> list[dict]:
        endpoint = f"https://static.developer.riotgames.com/docs/lol/queues.json"
        return self.riot_request.make_request(endpoint=endpoint)
