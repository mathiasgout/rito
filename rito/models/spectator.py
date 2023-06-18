from pydantic import BaseModel

from typing import Optional


class ActiveGame(BaseModel):
    match_id: Optional[str]
    queue_id: Optional[str]
    game_start_time: Optional[int]
    participants_id: Optional[list[str]]


class ActiveGameSummoner(BaseModel):
    team_id: Optional[str]
    champion_id: Optional[str]
    summoner_name: Optional[str]
    summoner_id: Optional[str]
    bot: Optional[bool]
    spell_id1: Optional[str]
    spell_id2: Optional[str]
