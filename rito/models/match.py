from pydantic import BaseModel

from typing import Optional


class Match(BaseModel):
    match_id: Optional[str]
    queue_id: Optional[str]
    game_version: Optional[str]
    game_start_time: Optional[int]
    game_end_time: Optional[int]
    game_duration: Optional[int]
    participants_puuid: Optional[list[Optional[str]]]
    participants_id: list[Optional[str]]


class MatchSummoner(BaseModel):
    team_id: Optional[str]
    summoner_id: Optional[str]
    summoner_name: Optional[str]
    summoner_puuid: Optional[str]
    champion_id: Optional[str]
    champion_name: Optional[str]
    champion_level: Optional[int]
    individual_position: Optional[str]
    team_position: Optional[str]
    win: Optional[bool]
    kills: Optional[int]
    deaths: Optional[int]
    assists: Optional[int]
    gold_earned: Optional[int]
    neutral_minions_killed: Optional[int]
    total_minions_killed: Optional[int]
    total_damage_dealt_to_champions: Optional[int]
    total_damage_taken: Optional[int]
    vision_score: Optional[int]
    summoner1_id: Optional[str]
    summoner2_id: Optional[str]
    kda: Optional[float]


class TeamTotals(BaseModel):
    team_id: Optional[str]
    total_kills: Optional[int]
    total_deaths: Optional[int]
    total_assists: Optional[int]
    total_neutral_minions_killed: Optional[int]
    total_minions_killed: Optional[int]
    total_gold_earned: Optional[int]
    total_damage_dealt_to_champions: Optional[int]
    total_damage_taken: Optional[int]
    total_vision_score: Optional[int]
