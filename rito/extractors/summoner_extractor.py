from rito.extractors.base_extractor import BaseExtractor
from rito.models.summoner import Summoner
from rito.errors import ExtractorError


class SummonerExtractor(BaseExtractor):
    def extract(self, summoner_dict: dict) -> Summoner:
        if not isinstance(summoner_dict, dict):
            raise ExtractorError(f"type(entry_dict)={type(summoner_dict)} (!= dict)")

        summoner = Summoner(
            summoner_id=summoner_dict.get("id", None),
            account_id=summoner_dict.get("accountId", None),
            puuid=summoner_dict.get("puuid", None),
            name=summoner_dict.get("name", None),
            profile_icon_id=summoner_dict.get("profileIconId", None),
            revision_date=summoner_dict.get("revisionDate", None),
            summoner_level=summoner_dict.get("summonerLevel", None),
        )
        return summoner
