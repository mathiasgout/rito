from rito.extractors.base_extractor import BaseExtractor
from rito.models.match import Match, MatchSummoner, MatchTotals
from rito.errors import ExtractorError

from typing import Optional


class MatchExtractor(BaseExtractor):
    def extract(self, match: dict) -> Match:
        if not isinstance(match, dict):
            raise ExtractorError(f"type(entry_dict)={type(match)} (!= dict)")

        metadata_dict = self._get_metadata_from_match(match=match)
        info_dict = self._get_info_from_match(match=match)

        match = Match(
            match_id=metadata_dict.get("matchId", None),
            queue_id=info_dict.get("queueId", None),
            game_version=info_dict.get("gameVersion", None),
            game_start_time=info_dict.get("gameStartTimestamp", None),
            game_end_time=info_dict.get("gameEndTimestamp", None),
            game_duration=info_dict.get("gameDuration", None),
            participants_puuid=metadata_dict.get("participants", []),
            participants_id=self._get_participants_id(
                info_dict.get("participants", None)
            ),
        )
        return match

    def extract_summoner(self, match: dict, summoner_id: str) -> MatchSummoner:
        if not isinstance(match, dict):
            raise ExtractorError(f"type(entry_dict)={type(match)} (!= dict)")

        info_dict = self._get_info_from_match(match=match)
        participant_dict = self._get_participant_by_summoner_id(
            participants_info=info_dict.get("participants", None),
            summoner_id=summoner_id,
        )

        match_summoner = MatchSummoner(
            team_id=participant_dict.get("teamId", None),
            summoner_id=participant_dict.get("summonerId", None),
            summoner_name=participant_dict.get("summonerName", None),
            summoner_puuid=participant_dict.get("puuid", None),
            champion_id=participant_dict.get("championId", None),
            champion_name=participant_dict.get("championName", None),
            team_position=participant_dict.get("teamPosition", None),
            win=participant_dict.get("win", None),
            kills=participant_dict.get("kills", None),
            deaths=participant_dict.get("deaths", None),
            assists=participant_dict.get("assists", None),
            total_damage_dealt_to_champions=participant_dict.get(
                "totalDamageDealtToChampions", None
            ),
            total_damage_taken=participant_dict.get("totalDamageTaken", None),
            vision_score=participant_dict.get("visionScore", None),
            summoner1_id=participant_dict.get("summoner1Id", None),
            summoner2_id=participant_dict.get("summoner2Id", None),
            kda=self._get_kda(
                kills=participant_dict.get("kills", None),
                deaths=participant_dict.get("deaths", None),
                assists=participant_dict.get("assists", None),
            ),
        )
        return match_summoner

    def extract_totals(self, match: dict) -> MatchTotals:
        if not isinstance(match, dict):
            raise ExtractorError(f"type(entry_dict)={type(match)} (!= dict)")

        info_dict = self._get_info_from_match(match=match)
        participants_infos = info_dict.get("participants", None)

        match_totals = MatchTotals(
            total_assists_team100=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="assists", team_id="100"
            ),
            total_assists_team200=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="assists", team_id="200"
            ),
            total_deaths_team100=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="deaths", team_id="100"
            ),
            total_deaths_team200=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="deaths", team_id="200"
            ),
            total_kills_team100=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="kills", team_id="100"
            ),
            total_kills_team200=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="kills", team_id="200"
            ),
            total_damage_dealt_to_champions_team100=self._get_total_by_key_and_team(
                participants_info=participants_infos,
                key="totalDamageDealtToChampions",
                team_id="100",
            ),
            total_damage_dealt_to_champions_team200=self._get_total_by_key_and_team(
                participants_info=participants_infos,
                key="totalDamageDealtToChampions",
                team_id="200",
            ),
            total_damage_taken_team100=self._get_total_by_key_and_team(
                participants_info=participants_infos,
                key="totalDamageTaken",
                team_id="100",
            ),
            total_damage_taken_team200=self._get_total_by_key_and_team(
                participants_info=participants_infos,
                key="totalDamageTaken",
                team_id="200",
            ),
            total_vision_score_team100=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="visionScore", team_id="100"
            ),
            total_vision_score_team200=self._get_total_by_key_and_team(
                participants_info=participants_infos, key="visionScore", team_id="200"
            ),
        )
        return match_totals

    @staticmethod
    def _get_total_by_key_and_team(
        participants_info: Optional[list[dict]], key: str, team_id: str
    ) -> Optional[int]:
        if not participants_info:
            return None

        total = 0
        for participant_info in participants_info:
            if int(team_id) == participant_info.get("teamId", None):
                value = participant_info.get(key, None)
                if value is None:
                    return None
                total += value
        return total

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
    def _get_kda(
        kills: Optional[int], deaths: Optional[int], assists: Optional[int]
    ) -> Optional[float]:
        if kills and deaths and assists:
            return round((kills + assists) / deaths, 2)
        return None

    @staticmethod
    def _get_metadata_from_match(match: dict) -> dict:
        return match.get("metadata", {})

    @staticmethod
    def _get_info_from_match(match: dict) -> dict:
        return match.get("info", {})

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
