from pydantic import BaseModel

from typing import Optional


class Account(BaseModel):
    puuid: Optional[str]
    game_name: Optional[str]
    tag_line: Optional[str]
