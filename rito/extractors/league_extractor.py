from rito.extractors.base_extractor import BaseExtractor
from rito.errors import ExtractorError
from rito.models.league import Entry, League
from rito import constants

from typing import Optional


class EntriesExtractor(BaseExtractor):
    def extract(self, entries_list: list[dict]) -> list[Entry]:
        if not isinstance(entries_list, list):
            raise ExtractorError(f"type(entries_list)={type(entries_list)} (!= list of dictionnaries)")

        entries = []
        for entry_dict in entries_list:
            entry = self.extract_from_entry(entry_dict=entry_dict)
            entries.append(entry)
        return entries

    def extract_entry(self, entries_list: list[dict], queue_type: str) -> Entry:
        if not isinstance(entries_list, list):
            raise ExtractorError(f"type(entries_list)={type(entries_list)} (!= list of dictionnaries)")
        if not queue_type:
            raise ExtractorError(f"queue_type={queue_type} (!= non null string)")

        entry_dict = self._get_entry_by_queue_type(entries_list=entries_list, queue_type=queue_type)
        entry = self.extract_from_entry(entry_dict=entry_dict)
        return entry

    def extract_from_entry(self, entry_dict: dict) -> Entry:
        if not isinstance(entry_dict, dict):
            raise ExtractorError(f"type(entry_dict)={type(entry_dict)} (!= dict)")

        entry = Entry(
            league_id=entry_dict.get("leagueId", None),
            queue_type=entry_dict.get("queueType", None),
            tier=entry_dict.get("tier", None),
            rank=entry_dict.get("rank", None),
            summoner_id=entry_dict.get("summonerId", None),
            summoner_name=entry_dict.get("summonerName", None),
            league_points=entry_dict.get("leaguePoints", None),
            wins=entry_dict.get("wins", None),
            losses=entry_dict.get("losses", None),
            veteran=entry_dict.get("veteran", None),
            inactive=entry_dict.get("inactive", None),
            fresh_blood=entry_dict.get("freshBlood", None),
            hot_streak=entry_dict.get("hotStreak", None),
            miniseries_progress=self._get_miniseries_progress(entry_dict=entry_dict),
            total_lp=self._get_total_lp(
                tier=entry_dict.get("tier", None),
                rank=entry_dict.get("rank", None),
                league_points=entry_dict.get("leaguePoints", None),
            ),
        )
        return entry

    @staticmethod
    def _get_miniseries_progress(entry_dict: dict) -> Optional[str]:
        miniseries = entry_dict.get("miniSeries", None)
        if miniseries:
            miniseries_progress = miniseries.get("progress", None)
            if miniseries_progress:
                return miniseries_progress
        return None

    @staticmethod
    def _get_entry_by_queue_type(entries_list: list[dict], queue_type: str) -> dict:
        for entry_dict in entries_list:
            if queue_type == entry_dict.get("queueType", None):
                return entry_dict

        raise ExtractorError(f"entry with queue_type={queue_type} not in entries_list")

    @staticmethod
    def _get_total_lp(tier: Optional[str], rank: Optional[str], league_points: Optional[int]) -> Optional[int]:
        TIERS = constants.CLASSIC_TIERS + constants.MASTER_TIERS

        if (tier not in TIERS) or (rank not in constants.RANKS) or (league_points is None):
            return None

        if tier in constants.MASTER_TIERS:
            return len(constants.CLASSIC_TIERS) * len(constants.RANKS) * 100 + league_points

        lp = 0
        for t in TIERS:
            for r in constants.RANKS:
                if (t == tier) and (r == rank):
                    return lp + league_points
                lp += 100


class LeaguesExtractor(BaseExtractor):
    def extract(self, league_dict: dict) -> League:
        if not isinstance(league_dict, dict):
            raise ExtractorError(f"type(league_dict)={type(league_dict)} (!= dictionnaries)")
    
        tier = league_dict.get("tier", None)
        league_id = league_dict.get("leagueId", None)
        queue = league_dict.get("queue", None)

        entries_list_raw=league_dict.get("entries", [])
        entries_list = []
        for entry_dict in entries_list_raw:
            entry_dict["leagueId"] = league_id
            entry_dict["queueType"] = queue
            entry_dict["tier"] = tier
            entries_list.append(entry_dict)

        entries_extractor = EntriesExtractor()
        league = League(
            tier=tier,
            league_id=league_id,
            queue=queue,
            name=league_dict.get("name", None),
            entries=entries_extractor.extract(entries_list=entries_list)
        )

        return league


class LeagueExtractor:
    def __init__(self) -> None:
        self.entries = EntriesExtractor()
        self.leagues = LeaguesExtractor()
