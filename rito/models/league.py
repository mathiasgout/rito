from pydantic import BaseModel

from typing import Optional


class Entry(BaseModel):
    league_id: Optional[str]
    queue_type: Optional[str]
    tier: Optional[str]
    rank: Optional[str]
    summoner_id: Optional[str]
    summoner_name: Optional[str]
    league_points: Optional[int]
    wins: Optional[int]
    losses: Optional[int]
    veteran: Optional[bool]
    inactive: Optional[bool]
    fresh_blood: Optional[bool]
    hot_streak: Optional[bool]
    miniseries_progress: Optional[str]
    total_lp: Optional[int]


class League(BaseModel):
    tier: Optional[str]
    league_id: Optional[str]
    queue: Optional[str]
    name: Optional[str]
    entries: Optional[list[Entry]]
