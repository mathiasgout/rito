from pydantic import BaseModel

from typing import Optional


class Match(BaseModel):
    match_id: Optional[str]
    queue_id: Optional[str]
    game_version: Optional[str]
    game_start_time: Optional[int]
    game_end_time: Optional[int]
    game_duration: Optional[int]
    participants_puuid: list[Optional[str]]
    participants_id: list[Optional[str]]


class MatchSummoner(BaseModel):
    team_id: Optional[str]
    summoner_id: Optional[str]
    summoner_name: Optional[str]
    summoner_puuid: Optional[str]
    champion_id: Optional[str]
    champion_name: Optional[str]
    team_position: Optional[str]
    win: Optional[bool]
    kills: Optional[int]
    deaths: Optional[int]
    assists: Optional[int]
    total_damage_dealt_to_champions: Optional[int]
    total_damage_taken: Optional[int]
    vision_score: Optional[int]
    summoner1_id: Optional[str]
    summoner2_id: Optional[str]
    kda: Optional[float]


class MatchTotals(BaseModel):
    total_kills_team100: Optional[int]
    total_kills_team200: Optional[int]
    total_deaths_team100: Optional[int]
    total_deaths_team200: Optional[int]
    total_assists_team100: Optional[int]
    total_assists_team200: Optional[int]
    total_damage_dealt_to_champions_team100: Optional[int]
    total_damage_dealt_to_champions_team200: Optional[int]
    total_damage_taken_team100: Optional[int]
    total_damage_taken_team200: Optional[int]
    total_vision_score_team100: Optional[int]
    total_vision_score_team200: Optional[int]
