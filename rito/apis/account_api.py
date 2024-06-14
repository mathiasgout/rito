from rito.apis.base_api import BaseRiotAPI
from rito.models.account import Account


class AccountAPIV1(BaseRiotAPI):
    def by_puuid(self, puuid: str) -> Account:
        endpoint = f"{self.routes['regional']}/riot/account/v1/accounts/by-puuid/{puuid}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = Account()
        return result.parse(json=j)
        
    def by_riot_id(self, game_name: str, tag_line: str) -> Account:
        endpoint = f"{self.routes['regional']}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = Account()
        return result.parse(json=j)
