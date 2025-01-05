from rito.models.base_model import Model


class PerksActiveGame(Model):
    @classmethod
    def parse(cls, json):
        perks = cls()
        setattr(perks, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(perks, k, v)
        return perks


class ParticipantActiveGame(Model):
    @classmethod
    def parse(cls, json):
        participant = cls()
        setattr(participant, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "perks":
                    perks = PerksActiveGame()
                    setattr(participant, k, perks.parse(v))
                else:
                    setattr(participant, k, v)
        return participant


class Observers(Model):
    @classmethod
    def parse(cls, json):
        observers = cls()
        setattr(observers, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(observers, k, v)
        return observers
    

class BannedChampion(Model):
    @classmethod
    def parse(cls, json):
        banned_champion = cls()
        setattr(banned_champion, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(banned_champion, k, v)
        return banned_champion


class ActiveGame(Model):
    @classmethod
    def parse(cls, json):
        active_game = cls()
        setattr(active_game, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "participants":
                    l = [ParticipantActiveGame().parse(j) for j in v]
                    setattr(active_game, k, l)
                elif k == "observers":
                    observers = Observers()
                    setattr(active_game, k, observers.parse(v))
                elif k == "bannedChampions":
                    l = [BannedChampion().parse(j) for j in v]
                    setattr(active_game, k, l)
                else:
                    setattr(active_game, k, v)
        return active_game


class ParticipantFeaturedGame(Model):
    @classmethod
    def parse(cls, json):
        participant_featured_game = cls()
        setattr(participant_featured_game, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(participant_featured_game, k, v)
        return participant_featured_game


class FeaturedGame(Model):
    @classmethod
    def parse(cls, json):
        featured_game = cls()
        setattr(featured_game, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "participants":
                    l = [ParticipantFeaturedGame().parse(j) for j in v]
                    setattr(featured_game, k, l)
                else:
                    setattr(featured_game, k, v)
        return featured_game


class FeaturedGames(Model):
    @classmethod
    def parse(cls, json):
        featured_games = cls()
        setattr(featured_games, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "gameList":
                    l = [FeaturedGame().parse(j) for j in v]
                    setattr(featured_games, k, l)
                else:
                    setattr(featured_games, k, v)
        return featured_games
