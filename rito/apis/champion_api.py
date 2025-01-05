from rito.apis.base_api import BaseRiotAPI
from rito.models.champion import ChampionRotations


class ChampionV3(BaseRiotAPI):
    def champion_rotations(self) -> ChampionRotations:
        endpoint = f"{self.routes['platform']}/lol/platform/v3/champion-rotations"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = ChampionRotations()
        return result.parse(json=j)
