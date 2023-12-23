from rito.extractors.base_extractor import BaseExtractor
from rito.models.account import Account
from rito.errors import ExtractorError


class AccountExtractor(BaseExtractor):
    def extract(self, account_dict: dict) -> Account:
        if not isinstance(account_dict, dict):
            raise ExtractorError(f"type(account_dict)={type(account_dict)} (!= dict)")
        
        account = Account(
            puuid=account_dict.get("puuid", None),
            game_name=account_dict.get("gameName", None),
            tag_line=account_dict.get("tagLine", None)
        )
        return account
