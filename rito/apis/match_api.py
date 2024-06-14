from rito.apis.base_api import BaseRiotAPI
from rito.models.match import Match, Timeline

from typing import Optional


class MatchAPIV5(BaseRiotAPI):
    def list_by_puuid(
        self,
        puuid: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        queue: Optional[int] = None,
        type: Optional[str] = None,
        start: Optional[int] = None,
        count: int = 20,
    ) -> list[str]:
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "queue": queue,
            "type": type,
            "start": start,
            "count": count,
        }
        endpoint = f"{self.routes['regional']}/lol/match/v5/matches/by-puuid/{puuid}/ids"
        return self.riot_request.make_request(endpoint=endpoint, params=params)

    def by_match_id(self, match_id: str) -> Match:
        endpoint = f"{self.routes['regional']}/lol/match/v5/matches/{match_id}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = Match()
        return result.parse(json=j)

    def timeline_by_match_id(self, match_id: str) -> Timeline:
        endpoint = f"{self.routes['regional']}/lol/match/v5/matches/{match_id}/timeline"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = Timeline()
        return result.parse(json=j)
