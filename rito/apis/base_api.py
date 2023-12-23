from rito.routes import ROUTES
from rito.riot_request import RiotRequest


class BaseRiotAPI:
    def __init__(self, riot_api_key: str, region: str, timeout: int = 300, tries_max: int = 5) -> None:
        self.riot_api_key = riot_api_key
        self.region = region
        self.tries_max = tries_max
        self.timeout = timeout
        self.routes = ROUTES[region]
        self.riot_request = RiotRequest(riot_api_key, timeout, tries_max)
