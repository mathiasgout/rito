from rito.models.base_model import Model


class ChampionRotations(Model):
    @classmethod
    def parse(cls, json):
        champion_rotation = cls()
        setattr(champion_rotation, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(champion_rotation, k, v)
        return champion_rotation
