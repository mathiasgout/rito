from pydantic import BaseModel

from typing import Optional


class ChampionMastery(BaseModel):
    puuid: Optional[str]
    champion_id: Optional[str]
    champion_level: Optional[int]
    champion_points: Optional[int]
    last_play_time: Optional[int]
    champion_points_since_last_level: Optional[int]
    champion_points_until_next_level: Optional[int]
    chest_granted: Optional[bool]
    tokens_earned: Optional[int]
    summoner_id: Optional[str]


class ChampionMasteryTotals(BaseModel):
    total_champion_level: Optional[int]
    total_champion_points: Optional[int]
