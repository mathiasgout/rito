from rito.apis.base_api import BaseRiotAPI


class DataDragonAPI(BaseRiotAPI):
    @property
    def versions(self) -> list[str]:
        endpoint = "https://ddragon.leagueoflegends.com/api/versions.json"
        return self.riot_request.make_request(endpoint=endpoint)

    def champions(self, version: str) -> dict:
        endpoint = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
        return self.riot_request.make_request(endpoint=endpoint)
