from rito.extractors.base_extractor import BaseExtractor
from rito.models.champion_mastery import ChampionMastery, ChampionMasteryTotals
from rito.errors import ExtractorError


class ChampionMasteryExtractor(BaseExtractor):
    def extract(self, champion_mastery_dict: dict) -> ChampionMastery:
        if not isinstance(champion_mastery_dict, dict):
            raise ExtractorError(
                f"type(champion_mastery_dict)={type(champion_mastery_dict)} (!= dict)"
            )

        champion_mastery = ChampionMastery(
            puuid=champion_mastery_dict.get("puuid", None),
            champion_id=champion_mastery_dict.get("championId", None),
            champion_level=champion_mastery_dict.get("championLevel", None),
            champion_points=champion_mastery_dict.get("championPoints", None),
            last_play_time=champion_mastery_dict.get("lastPlayTime", None),
            champion_points_since_last_level=champion_mastery_dict.get(
                "championPointsSinceLastLevel", None
            ),
            champion_points_until_next_level=champion_mastery_dict.get(
                "championPointsUntilNextLevel", None
            ),
            chest_granted=champion_mastery_dict.get("chestGranted", None),
            tokens_earned=champion_mastery_dict.get("tokensEarned", None),
            summoner_id=champion_mastery_dict.get("summonerId", None),
        )
        return champion_mastery

    def extract_from_list(
        self, champion_masteries_list: list[dict], champion_id: str
    ) -> ChampionMastery:
        if not isinstance(champion_masteries_list, list):
            raise ExtractorError(
                f"type(champion_masteries_list)={type(champion_masteries_list)} (!= list of dictionnaries)"
            )

        for champion_mastery_dict in champion_masteries_list:
            if champion_mastery_dict.get("championId", None) == int(champion_id):
                champion_mastery = ChampionMastery(
                    puuid=champion_mastery_dict.get("puuid", None),
                    champion_id=champion_mastery_dict.get("championId", None),
                    champion_level=champion_mastery_dict.get("championLevel", None),
                    champion_points=champion_mastery_dict.get("championPoints", None),
                    last_play_time=champion_mastery_dict.get("lastPlayTime", None),
                    champion_points_since_last_level=champion_mastery_dict.get(
                        "championPointsSinceLastLevel", None
                    ),
                    champion_points_until_next_level=champion_mastery_dict.get(
                        "championPointsUntilNextLevel", None
                    ),
                    chest_granted=champion_mastery_dict.get("chestGranted", None),
                    tokens_earned=champion_mastery_dict.get("tokensEarned", None),
                    summoner_id=champion_mastery_dict.get("summonerId", None),
                )
                return champion_mastery
        raise ExtractorError(
            f"champion with champion_id={champion_id} not in champion_masteries_list"
        )

    def extract_totals_from_list(
        self, champion_masteries_list: list[dict]
    ) -> ChampionMasteryTotals:
        if not isinstance(champion_masteries_list, list):
            raise ExtractorError(
                f"type(champion_masteries_list)={type(champion_masteries_list)} (!= list of dictionnaries)"
            )

        total_champion_level = 0
        total_champion_points = 0

        for champion_mastery_dict in champion_masteries_list:
            total_champion_level += int(champion_mastery_dict.get("championLevel", 0))
            total_champion_points += int(champion_mastery_dict.get("championPoints", 0))

        champion_mastery_summary = ChampionMasteryTotals(
            total_champion_level=total_champion_level,
            total_champion_points=total_champion_points,
        )
        return champion_mastery_summary
