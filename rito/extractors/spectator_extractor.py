from rito.extractors.base_extractor import BaseExtractor
from rito.models.spectator import ActiveGame, ActiveGameSummoner
from rito.errors import ExtractorError

from typing import Optional
from datetime import datetime, timezone


class ActiveGameExtractor(BaseExtractor):
    def extract(self, active_game: dict) -> ActiveGame:
        if not isinstance(active_game, dict):
            raise ExtractorError(f"type(active_game)={type(active_game)} (!= dict)")

        active_game = ActiveGame(
            match_id=self._get_match_id(
                game_id=active_game.get("gameId", None),
                platform_id=active_game.get("platformId", None),
            ),
            queue_id=active_game.get("gameQueueConfigId", None),
            game_start_time=self._get_game_start_time(
                game_start_time=active_game.get("gameStartTime", None)
            ),
            participants_id=self._get_participants_id(
                active_game.get("participants", None)
            ),
        )
        return active_game

    def extract_summoner(
        self, active_game: dict, summoner_id: str
    ) -> ActiveGameSummoner:
        if not isinstance(active_game, dict):
            raise ExtractorError(f"type(active_game)={type(active_game)} (!= dict)")

        participant_dict = self._get_participant_by_summoner_id(
            participants_info=active_game.get("participants", None),
            summoner_id=summoner_id,
        )

        active_game_summoner = ActiveGameSummoner(
            team_id=participant_dict.get("teamId", None),
            champion_id=participant_dict.get("championId", None),
            summoner_name=participant_dict.get("summonerName", None),
            summoner_id=participant_dict.get("summonerId", None),
            bot=participant_dict.get("bot", None),
            spell_id1=participant_dict.get("spell1Id", None),
            spell_id2=participant_dict.get("spell2Id", None),
        )
        return active_game_summoner

    def _get_game_start_time(self, game_start_time: Optional[int]) -> int:
        if game_start_time:
            return game_start_time
        return self._get_ts_milli_utc()

    @staticmethod
    def _get_participant_by_summoner_id(
        participants_info: Optional[list[dict]], summoner_id: Optional[str]
    ) -> dict:
        if not participants_info:
            return {}

        for participant_info in participants_info:
            if summoner_id == participant_info.get("summonerId", None):
                return participant_info
        return {}

    @staticmethod
    def _get_participants_id(
        participants_info: Optional[list[dict]],
    ) -> list[Optional[str]]:
        if not participants_info:
            return []

        participants_id = []
        for participant_info in participants_info:
            participants_id.append(participant_info.get("summonerId", None))
        return participants_id

    @staticmethod
    def _get_match_id(
        game_id: Optional[str], platform_id: Optional[str]
    ) -> Optional[str]:
        if game_id and platform_id:
            return f"{platform_id}_{game_id}"
        return None

    @staticmethod
    def _get_ts_milli_utc() -> int:
        dt_utc = datetime.now(timezone.utc)
        utc_timestamp = int(dt_utc.timestamp() * 1000)
        return utc_timestamp


class SpectatorExtractor:
    def __init__(self) -> None:
        self.active_game = ActiveGameExtractor()
