from rito.models.base_model import Model


class Summoner(Model):
    @classmethod
    def parse(cls, json):
        summoner = cls()
        setattr(summoner, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(summoner, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return summoner
