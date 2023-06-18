from rito.extractors.base_extractor import BaseExtractor
from rito.models.league import Entry
from rito.errors import ExtractorError

from typing import Optional


class EntriesExtractor(BaseExtractor):
    def extract(self, entries_list: list[dict]) -> list[Entry]:
        if not isinstance(entries_list, list):
            raise ExtractorError(
                f"type(entries_list)={type(entries_list)} (!= list of dictionnaries)"
            )

        entries = []
        for entry_dict in entries_list:
            entry = self.extract_from_entry(entry_dict=entry_dict)
            entries.append(entry)
        return entries

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
            total_lp=self._get_total_lp(
                tier=entry_dict.get("tier", None),
                rank=entry_dict.get("rank", None),
                league_points=entry_dict.get("leaguePoints", None),
            ),
        )
        return entry

    @staticmethod
    def _get_total_lp(
        tier: Optional[str], rank: Optional[str], league_points: Optional[int]
    ) -> Optional[int]:
        classic_tiers = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
        masters_tiers = ["MASTER", "GRANDMASTER", "CHALLENGER"]
        tiers = classic_tiers + masters_tiers
        ranks = ["IV", "III", "II", "I"]

        if (tier not in tiers) or (rank not in ranks) or (league_points is None):
            return None

        if tier in masters_tiers:
            return len(classic_tiers) * len(ranks) * 100 + league_points

        lp = 0
        for t in tiers:
            for r in ranks:
                if (t == tier) and (r == rank):
                    return lp + league_points
                lp += 100
        return None


class LeagueExtractor:
    def __init__(self) -> None:
        self.entries = EntriesExtractor()
