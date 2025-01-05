from rito.apis.base_api import BaseRiotAPI
from rito.models.spectator import ActiveGame
from rito.models.spectator import FeaturedGames


class ActiveGameAPI(BaseRiotAPI):
    def by_summoner(self, puuid: str) -> ActiveGame:
        endpoint = f"{self.routes['platform']}/lol/spectator/v5/active-games/by-summoner/{puuid}"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = ActiveGame()
        return result.parse(json=j)


class FeaturedGamesAPI(BaseRiotAPI):
    def game_list(self) -> FeaturedGames:
        endpoint = f"{self.routes['platform']}/lol/spectator/v5/featured-games"
        j = self.riot_request.make_request(endpoint=endpoint)
        result = FeaturedGames()
        return result.parse(json=j)


class SpectatorAPIV5(BaseRiotAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.active_game = ActiveGameAPI(self.riot_api_key, self.region, self.return_none_on_404, self.retry_on_rate_limit, self.timeout_on_servor_error)
        self.featured_games = FeaturedGamesAPI(self.riot_api_key, self.region, self.return_none_on_404, self.retry_on_rate_limit, self.timeout_on_servor_error)
