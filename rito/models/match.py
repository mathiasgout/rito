from pydantic import BaseModel

from typing import Optional


class Match(BaseModel):
    match_id: Optional[str]
    queue_id: Optional[str]
    game_version: Optional[str]
    game_start_time: Optional[int]
    game_end_time: Optional[int]
    game_duration: Optional[int]
    participants_puuid: Optional[list[str]]
    participants_id: list[Optional[str]]


class MatchSummoner(BaseModel):
    team_id: Optional[str]
    summoner_id: Optional[str]
    summoner_name: Optional[str]
    puuid: Optional[str]
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


class TimelineChampionStats(BaseModel):
    ability_haste: Optional[int]
    ability_power: Optional[int]
    armor: Optional[int]
    armor_pen: Optional[int]
    armor_pen_percent: Optional[int]
    attack_damage: Optional[int]
    attack_speed: Optional[int]
    bonus_armor_pen_percent: Optional[int]
    bonus_magic_pen_percent: Optional[int]
    cc_reduction: Optional[int]
    cooldown_reduction: Optional[int]
    health: Optional[int]
    health_max: Optional[int]
    health_regen: Optional[int]
    lifesteal: Optional[int]
    magic_pen: Optional[int]
    magic_pen_percent: Optional[int]
    magic_resist: Optional[int]
    movement_speed: Optional[int]
    omnivamp: Optional[int]
    physical_vamp: Optional[int]
    power: Optional[int]
    power_max: Optional[int]
    power_regen: Optional[int]
    spell_vamp: Optional[int]


class TimelineDamageStats(BaseModel):
    magic_damage_done: Optional[int]
    magic_damage_done_to_champions: Optional[int]
    magic_damage_taken: Optional[int]
    physical_damage_done: Optional[int]
    physical_damage_done_to_champions: Optional[int]
    physical_damage_taken: Optional[int]
    total_damage_done: Optional[int]
    total_damage_done_to_champions: Optional[int]
    total_damage_taken: Optional[int]
    true_damage_done: Optional[int]
    true_damage_done_to_champions: Optional[int]
    true_damage_taken: Optional[int]


class TimelineParticipantFrame(BaseModel):
    champion_stats: Optional[TimelineChampionStats]
    current_gold: Optional[int]
    damage_stats: Optional[TimelineDamageStats]
    gold_per_second: Optional[int]
    jungle_minions_killed: Optional[int]
    level: Optional[int]
    minions_killed: Optional[int]
    participant_id: Optional[str]
    position: Optional[dict[str, int]]
    time_enemy_spent_controlled: Optional[int]
    total_gold: Optional[int]
    xp: Optional[int]


class TimelineFrame(BaseModel):
    events: Optional[list[dict]]
    participant_frames: Optional[dict[str, TimelineParticipantFrame]]
    timestamp: Optional[int]


class MatchTimeline(BaseModel):
    match_id: Optional[str]
    participants_puuid: Optional[list[str]]
    participants_ids_map: Optional[dict[str, str]]
    frame_interval: Optional[int]
    frames: Optional[list[TimelineFrame]]
