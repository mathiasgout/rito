from rito.apis.base_api import BaseRiotAPI
from rito.models.challenges import ChallengesConfig
from rito.models.challenges import LeaderboardPlayer
from rito.models.challenges import ChallengesPlayerInformation


class ChallengesV1(BaseRiotAPI):
    def config(self) -> list[ChallengesConfig]:
        endpoint = f"{self.routes['platform']}/lol/challenges/v1/challenges/config"
        l = self.riot_request.make_request(endpoint=endpoint)
        result = ChallengesConfig()
        return [result.parse(json=j) for j in l]

    def percentiles(self) -> dict:
        endpoint = f"{self.routes['platform']}/lol/challenges/v1/challenges/percentiles"
        return self.riot_request.make_request(endpoint=endpoint)
    
    def config_by_challenge_id(self, challenge_id: str) -> ChallengesConfig:
        endpoint = f"{self.routes['platform']}/lol/challenges/v1/challenges/{challenge_id}/config"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = ChallengesConfig()
        return result.parse(json=j)

    def percentiles_by_challenge_id(self, challenge_id: str) -> dict:
        endpoint = f"{self.routes['platform']}/lol/challenges/v1/challenges/{challenge_id}/percentiles"
        return self.riot_request.make_request(endpoint=endpoint)

    def leaderboards_by_challenge_id_by_level(self, challenge_id: str, level: str, limit: int = None) -> list[LeaderboardPlayer]:
        params = {"limit": limit}
        endpoint = f"{self.routes['platform']}/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level}"
        l = self.riot_request.make_request(endpoint=endpoint, params=params)
        result = LeaderboardPlayer()
        return [result.parse(json=j) for j in l]

    def player_information(self, puuid: str) -> ChallengesPlayerInformation:
        endpoint = f"{self.routes['platform']}/lol/challenges/v1/player-data/{puuid}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = ChallengesPlayerInformation()
        return result.parse(json=j)
