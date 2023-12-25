from rito.extractors.base_extractor import BaseExtractor
from rito.models.match import Match, MatchSummoner, TeamTotals
from rito.models.match import MatchTimeline, TimelineFrame, TimelineParticipantFrame, TimelineChampionStats, TimelineDamageStats
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

    def extract_timeline(self, match_timeline_dict: dict) -> MatchTimeline:
        if not isinstance(match_timeline_dict, dict):
            raise ExtractorError(f"type(match_timeline_dict)={type(match_timeline_dict)} (!= dict)")

        metadata_dict = self._get_metadata(d=match_timeline_dict)
        info_dict = self._get_info(d=match_timeline_dict)

        frames = []
        frames_list = info_dict.get("frames", [])
        for frame in frames_list:
            events = frame.get("events", [])
            timestamp = frame.get("timestamp", None)

            participant_frames = {}
            participant_frames_dict = frame.get("participantFrames", {})
            for participant_id, participant_frame in participant_frames_dict.items():
                champion_stats_dict = participant_frame.get("championStats", {})
                champion_stats = TimelineChampionStats(
                    ability_haste=champion_stats_dict.get("abilityHaste", None),
                    ability_power=champion_stats_dict.get("abilityPower", None),
                    armor=champion_stats_dict.get("armor", None),
                    armor_pen=champion_stats_dict.get("armorPen", None),
                    armor_pen_percent=champion_stats_dict.get("armorPenPercent", None),
                    attack_damage=champion_stats_dict.get("attackDamage", None),
                    attack_speed=champion_stats_dict.get("attackSpeed", None),
                    bonus_armor_pen_percent=champion_stats_dict.get("bonusArmorPenPercent", None),
                    bonus_magic_pen_percent=champion_stats_dict.get("bonusMagicPenPercent", None),
                    cc_reduction=champion_stats_dict.get("ccReduction", None),
                    cooldown_reduction=champion_stats_dict.get("cooldownReduction", None),
                    health=champion_stats_dict.get("health", None),
                    health_max=champion_stats_dict.get("healthMax", None),
                    health_regen=champion_stats_dict.get("healthRegen", None),
                    lifesteal=champion_stats_dict.get("lifesteal", None),
                    magic_pen=champion_stats_dict.get("magicPen", None),
                    magic_pen_percent=champion_stats_dict.get("magicPenPercent", None),
                    magic_resist=champion_stats_dict.get("magicResist", None),
                    movement_speed=champion_stats_dict.get("movementSpeed", None),
                    omnivamp=champion_stats_dict.get("omnivamp", None),
                    physical_vamp=champion_stats_dict.get("physicalVamp", None),
                    power=champion_stats_dict.get("power", None),
                    power_max=champion_stats_dict.get("powerMax", None),
                    power_regen=champion_stats_dict.get("powerRegen", None),
                    spell_vamp=champion_stats_dict.get("spellVamp", None)
                )
                
                damage_stats_dict = participant_frame.get("damageStats", {})
                damage_stats = TimelineDamageStats(
                    magic_damage_done=damage_stats_dict.get("magicDamageDone", None),
                    magic_damage_done_to_champions=damage_stats_dict.get("magicDamageDoneToChampions", None),
                    magic_damage_taken=damage_stats_dict.get("magicDamageTaken", None),
                    physical_damage_done=damage_stats_dict.get("physicalDamageDone", None),
                    physical_damage_done_to_champions=damage_stats_dict.get("physicalDamageDoneToChampions", None),
                    physical_damage_taken=damage_stats_dict.get("physicalDamageTaken", None),
                    total_damage_done=damage_stats_dict.get("totalDamageDone", None),
                    total_damage_done_to_champions=damage_stats_dict.get("totalDamageDoneToChampions", None),
                    total_damage_taken=damage_stats_dict.get("totalDamageTaken", None),
                    true_damage_done=damage_stats_dict.get("TrueDamageDone", None),
                    true_damage_done_to_champions=damage_stats_dict.get("TrueDamageDoneToChampions", None),
                    true_damage_taken=damage_stats_dict.get("TrueDamageTaken", None)
                )

                timeline_participant_frame = TimelineParticipantFrame(
                    champion_stats=champion_stats,
                    current_gold=participant_frame.get("currentGold", None),
                    damage_stats=damage_stats,
                    gold_per_second=participant_frame.get("goldPerSecond", None),
                    jungle_minions_killed=participant_frame.get("jungleMinionsKilled", None),
                    level=participant_frame.get("level", None),
                    minions_killed=participant_frame.get("minionsKilled", None),
                    participant_id=str(participant_frame.get("participantId", None)),
                    position=participant_frame.get("position", None),
                    time_enemy_spent_controlled=participant_frame.get("timeEnemySpentControlled", None),
                    total_gold=participant_frame.get("totalGold", None),
                    xp=participant_frame.get("xp", None)
                )
                participant_frames[str(participant_id)] = timeline_participant_frame

            timeline_frame = TimelineFrame(
                events=events,
                participant_frames=participant_frames,
                timestamp=timestamp
            )
            frames.append(timeline_frame)
    
        match_timeline = MatchTimeline(
            match_id=metadata_dict.get("matchId", None),
            participants_puuid=metadata_dict.get("participants", None),
            participants_ids_map=self._get_participants_ids_map(info_dict["participants"]),
            frame_interval=info_dict.get("frameInterval", None),
            frames=frames
        )
        return match_timeline

    @staticmethod
    def _get_participants_ids_map(participants_ids: list[dict]) -> dict[str, str]:
        participants_ids_map = {}
        for participant_ids in participants_ids:
            participants_ids_map[participant_ids["puuid"]] = str(participant_ids["participantId"])
        return participants_ids_map

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
        metadata = d.get("metadata", {})
        return metadata

    @staticmethod
    def _get_info(d: dict) -> dict:
        info = d.get("info", {})
        return info

    @staticmethod
    def _get_participants_id(participants_info: list[dict]) -> list[Optional[str]]:
        participants_id = []
        for participant_info in participants_info:
            participants_id.append(participant_info.get("summonerId", None))
        return participants_id
