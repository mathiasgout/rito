from rito.apis.base_api import BaseRiotAPI

from typing import Union


class MatchAPIV5(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def list_by_puuid(
        self,
        puuid: str,
        start_time: Union[None, int] = None,
        end_time: Union[None, int] = None,
        queue: Union[None, int] = None,
        type: Union[None, str] = None,
        start: Union[None, int] = None,
        count: int = 20,
    ) -> Union[None, list[str]]:
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "queue": queue,
            "type": type,
            "start": start,
            "count": count,
        }
        endpoint = (
            f"{self.routes['regional']}/lol/match/v5/matches/by-puuid/{puuid}/ids"
        )
        return self.riot_request.make_request(endpoint=endpoint, params=params)

    def by_match_id(self, match_id: str) -> Union[None, dict]:
        endpoint = f"{self.routes['regional']}/lol/match/v5/matches/{match_id}"
        return self.riot_request.make_request(endpoint=endpoint)
