from rito.extractors.base_extractor import BaseExtractor
from rito.models.match import Match, MatchSummoner, TeamTotals
from rito.errors import ExtractorError

from typing import Optional


class MatchExtractor(BaseExtractor):
    def extract(self, match_dict: dict) -> Match:
        if not isinstance(match_dict, dict):
            raise ExtractorError(f"type(match_dict)={type(match_dict)} (!= dict)")

        metadata_dict = self._get_metadata(d=match_dict)
        info_dict = self._get_info(d=match_dict)

        match = Match(
            match_id=metadata_dict.get("matchId", None),
            queue_id=info_dict.get("queueId", None),
            game_version=info_dict.get("gameVersion", None),
            game_start_time=info_dict.get("gameStartTimestamp", None),
            game_end_time=info_dict.get("gameEndTimestamp", None),
            game_duration=info_dict.get("gameDuration", None),
            participants_puuid=metadata_dict.get("participants", None),
            participants_id=self._get_participants_id(self._get_participants_info(info=info_dict)),
        )
        return match

    def extract_summoner(self, match_dict: dict, summoner_id: Optional[str] = None, puuid: Optional[str] = None) -> MatchSummoner:
        if not isinstance(match_dict, dict):
            raise ExtractorError(f"type(match_dict)={type(match_dict)} (!= dict)")
        if not any([summoner_id, puuid]):
            raise ExtractorError(f"summoner_id or puuid must not be None")

        info_dict = self._get_info(d=match_dict)
        participants_info = self._get_participants_info(info=info_dict)
        if summoner_id:
            participant_dict = self._get_participant_by_summoner_id(
                participants_info=participants_info, 
                summoner_id=summoner_id
            )
        else:
            participant_dict = self._get_participant_by_puuid(
                participants_info=participants_info, 
                puuid=puuid
            )

        match_summoner = MatchSummoner(
            team_id=participant_dict.get("teamId", None),
            summoner_id=participant_dict.get("summonerId", None),
            summoner_name=participant_dict.get("summonerName", None),
            summoner_puuid=participant_dict.get("puuid", None),
            champion_id=participant_dict.get("championId", None),
            champion_name=participant_dict.get("championName", None),
            champion_level=participant_dict.get("champLevel", None),
            individual_position=participant_dict.get("individualPosition", None),
            team_position=participant_dict.get("teamPosition", None),
            win=participant_dict.get("win", None),
            kills=participant_dict.get("kills", None),
            deaths=participant_dict.get("deaths", None),
            assists=participant_dict.get("assists", None),
            gold_earned=participant_dict.get("goldEarned", None),
            neutral_minions_killed=participant_dict.get("neutralMinionsKilled", None),
            total_minions_killed=participant_dict.get("totalMinionsKilled", None),
            total_damage_dealt_to_champions=participant_dict.get("totalDamageDealtToChampions", None),
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

    def extract_opponent(self, match_dict: dict, summoner_id: Optional[str] = None, puuid: Optional[str] = None) -> MatchSummoner:
        if not isinstance(match_dict, dict):
            raise ExtractorError(f"type(match_dict)={type(match_dict)} (!= dict)")
        if not any([summoner_id, puuid]):
            raise ExtractorError(f"summoner_id or puuid must not be None")

        info_dict = self._get_info(d=match_dict)
        participants_info = self._get_participants_info(info=info_dict)
        if summoner_id:
            opponent_participant_dict = self._get_opponent_participant_by_summoner_id(
                participants_info=participants_info,
                summoner_id=summoner_id
            )
        else:
            opponent_participant_dict = self._get_opponent_participant_by_puuid(
                participants_info=participants_info,
                puuid=puuid
            )   

        match_summoner = MatchSummoner(
            team_id=opponent_participant_dict.get("teamId", None),
            summoner_id=opponent_participant_dict.get("summonerId", None),
            summoner_name=opponent_participant_dict.get("summonerName", None),
            summoner_puuid=opponent_participant_dict.get("puuid", None),
            champion_id=opponent_participant_dict.get("championId", None),
            champion_name=opponent_participant_dict.get("championName", None),
            champion_level=opponent_participant_dict.get("champLevel", None),
            individual_position=opponent_participant_dict.get("individualPosition", None),
            team_position=opponent_participant_dict.get("teamPosition", None),
            win=opponent_participant_dict.get("win", None),
            kills=opponent_participant_dict.get("kills", None),
            deaths=opponent_participant_dict.get("deaths", None),
            assists=opponent_participant_dict.get("assists", None),
            gold_earned=opponent_participant_dict.get("goldEarned", None),
            neutral_minions_killed=opponent_participant_dict.get("neutralMinionsKilled", None),
            total_minions_killed=opponent_participant_dict.get("totalMinionsKilled", None),
            total_damage_dealt_to_champions=opponent_participant_dict.get("totalDamageDealtToChampions", None),
            total_damage_taken=opponent_participant_dict.get("totalDamageTaken", None),
            vision_score=opponent_participant_dict.get("visionScore", None),
            summoner1_id=opponent_participant_dict.get("summoner1Id", None),
            summoner2_id=opponent_participant_dict.get("summoner2Id", None),
            kda=self._get_kda(
                kills=opponent_participant_dict.get("kills", None),
                deaths=opponent_participant_dict.get("deaths", None),
                assists=opponent_participant_dict.get("assists", None),
            ),
        )
        return match_summoner

    def extract_totals(self, match_dict: dict) -> list[TeamTotals]:
        if not isinstance(match_dict, dict):
            raise ExtractorError(f"type(match_dict)={type(match_dict)} (!= dict)")

        info_dict = self._get_info(d=match_dict)
        participants_infos = self._get_participants_info(info=info_dict)

        totals = [
            TeamTotals(
                team_id="100",
                total_gold_earned=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="goldEarned", 
                    team_id="100"
                ),
                total_assists=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="assists", 
                    team_id="100"
                ),
                total_deaths=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="deaths", 
                    team_id="100"
                ),
                total_kills=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="kills", 
                    team_id="100"
                ),
                total_neutral_minions_killed=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="neutralMinionsKilled", 
                    team_id="100"
                ),
                total_minions_killed=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="totalMinionsKilled", 
                    team_id="100"
                ),
                total_damage_dealt_to_champions=self._get_total_by_key_and_team(
                    participants_info=participants_infos,
                    key="totalDamageDealtToChampions",
                    team_id="100",
                ),
                total_damage_taken=self._get_total_by_key_and_team(
                    participants_info=participants_infos,
                    key="totalDamageTaken",
                    team_id="100",
                ),
                total_vision_score=self._get_total_by_key_and_team(
                    participants_info=participants_infos,
                    key="visionScore",
                    team_id="100",
                ),
            ),
            TeamTotals(
                team_id="200",
                total_gold_earned=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="goldEarned", 
                    team_id="200"
                ),
                total_assists=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="assists", 
                    team_id="200"
                ),
                total_deaths=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="deaths", 
                    team_id="200"
                ),
                total_kills=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="kills", 
                    team_id="200"
                ),
                total_neutral_minions_killed=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="neutralMinionsKilled", 
                    team_id="200"
                ),
                total_minions_killed=self._get_total_by_key_and_team(
                    participants_info=participants_infos, 
                    key="totalMinionsKilled", 
                    team_id="200"
                ),
                total_damage_dealt_to_champions=self._get_total_by_key_and_team(
                    participants_info=participants_infos,
                    key="totalDamageDealtToChampions",
                    team_id="200",
                ),
                total_damage_taken=self._get_total_by_key_and_team(
                    participants_info=participants_infos,
                    key="totalDamageTaken",
                    team_id="200",
                ),
                total_vision_score=self._get_total_by_key_and_team(
                    participants_info=participants_infos,
                    key="visionScore",
                    team_id="200",
                ),
            ),
        ]
        return totals

    @staticmethod
    def _get_total_by_key_and_team(participants_info: list[dict], key: str, team_id: str) -> int:
        total = 0
        for participant_info in participants_info:
            if int(team_id) == participant_info.get("teamId", None):
                value = participant_info.get(key, None)
                if value is None:
                    raise ExtractorError(f"no value for key={key} and team_id={team_id} in participants_info")
                total += value
        return total

    @staticmethod
    def _get_participants_info(info: dict) -> list[dict]:
        participants_info = info.get("participants", None)
        if participants_info:
            return participants_info
        raise ExtractorError(f"no participants in info")

    @staticmethod
    def _get_participant_by_summoner_id(participants_info: list[dict], summoner_id: str) -> dict:
        for participant_info in participants_info:
            if summoner_id == participant_info.get("summonerId", None):
                return participant_info
        raise ExtractorError(f"summoner with summoner_id={summoner_id} not in participants info")
    
    @staticmethod
    def _get_participant_by_puuid(participants_info: list[dict], puuid: str) -> dict:
        for participant_info in participants_info:
            if puuid == participant_info.get("puuid", None):
                return participant_info
        raise ExtractorError(f"summoner with puuid={puuid} not in participants info")

    @staticmethod
    def _get_opponent_participant_by_summoner_id(participants_info: list[dict], summoner_id: str) -> dict:
        exists = False
        for participant_info in participants_info:
            if summoner_id == participant_info.get("summonerId", None):
                team_position = participant_info.get("teamPosition", None)
                team_id = participant_info.get("teamId", None)
                exists = True

        if exists:
            if team_position and team_id:
                for participant_info in participants_info:
                    if (
                        team_position == participant_info.get("teamPosition", None)
                    ) and (team_id != participant_info.get("teamId", None)):
                        return participant_info
        raise ExtractorError(f"opponent of summoner with summoner_id={summoner_id} not in participants info")

    @staticmethod
    def _get_opponent_participant_by_puuid(participants_info: list[dict], puuid: str) -> dict:
        exists = False
        for participant_info in participants_info:
            if puuid == participant_info.get("puuid", None):
                team_position = participant_info.get("teamPosition", None)
                team_id = participant_info.get("teamId", None)
                exists = True

        if exists:
            if team_position and team_id:
                for participant_info in participants_info:
                    if (
                        team_position == participant_info.get("teamPosition", None)
                    ) and (team_id != participant_info.get("teamId", None)):
                        return participant_info
        raise ExtractorError(f"opponent of summoner with puuid={puuid} not in participants info")

    @staticmethod
    def _get_kda(kills: Optional[int], deaths: Optional[int], assists: Optional[int]) -> Optional[float]:
        if (kills is not None) and (deaths is not None) and (assists is not None):
            deaths = max(deaths, 1)
            return round((kills + assists) / deaths, 2)
        return None

    @staticmethod
    def _get_metadata(d: dict) -> dict:
        metadata = d.get("metadata", None)
        if metadata:
            return metadata
        raise ExtractorError(f"no metadata in dict")

    @staticmethod
    def _get_info(d: dict) -> dict:
        info = d.get("info", None)
        if info:
            return info
        raise ExtractorError(f"no info in dict")

    @staticmethod
    def _get_participants_id(participants_info: list[dict]) -> list[Optional[str]]:
        participants_id = []
        for participant_info in participants_info:
            participants_id.append(participant_info.get("summonerId", None))
        return participants_id
