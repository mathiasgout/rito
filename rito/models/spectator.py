from rito.models.base_model import Model


class PerksActiveGame(Model):
    @classmethod
    def parse(cls, json):
        perks = cls()
        setattr(perks, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(perks, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(participant, "perks", perks.parse(v))
                else:
                    setattr(participant, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return participant


class Observers(Model):
    @classmethod
    def parse(cls, json):
        observers = cls()
        setattr(observers, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(observers, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return observers
    

class BannedChampion(Model):
    @classmethod
    def parse(cls, json):
        banned_champion = cls()
        setattr(banned_champion, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(banned_champion, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(active_game, "participants", l)
                elif k == "observers":
                    observers = Observers()
                    setattr(active_game, "observers", observers.parse(v))
                elif k == "bannedChampions":
                    l = [BannedChampion().parse(j) for j in v]
                    setattr(active_game, "banned_champions", l)
                else:
                    setattr(active_game, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return active_game
