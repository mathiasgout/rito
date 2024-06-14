from rito.routes import ROUTES
from rito.riot_request import RiotRequest


class BaseRiotAPI:
    def __init__(
        self, 
        riot_api_key: str,
        region: str,
        return_none_on_404: bool,
        retry_on_rate_limit: bool, 
        timeout_on_servor_error: int
    ) -> None:

        self.riot_api_key = riot_api_key
        self.region = region
        self.return_none_on_404 = return_none_on_404
        self.retry_on_rate_limit = retry_on_rate_limit
        self.timeout_on_servor_error = timeout_on_servor_error

        self.routes = ROUTES[region]
        self.riot_request = RiotRequest(riot_api_key, return_none_on_404, retry_on_rate_limit, timeout_on_servor_error)
