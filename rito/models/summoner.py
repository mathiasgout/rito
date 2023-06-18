from pydantic import BaseModel

from typing import Optional


class Summoner(BaseModel):
    summoner_id: Optional[str]
    account_id: Optional[str]
    puuid: Optional[str]
    name: Optional[str]
    profile_icon_id: Optional[str]
    revision_date: Optional[int]
    summoner_level: Optional[int]
