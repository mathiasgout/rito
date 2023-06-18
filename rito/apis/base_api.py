from rito.routes import ROUTES
from rito.riot_request import RiotRequest


class BaseRiotAPI:
    def __init__(self, riot_api_key: str, region: str, tries_5xx: int = 5) -> None:
        self.riot_api_key = riot_api_key
        self.region = region
        self.tries_5xx = tries_5xx
        self.routes = ROUTES[region]
        self.riot_request = RiotRequest(riot_api_key=riot_api_key, tries_5xx=tries_5xx)
