from rito.models.base_model import Model


class Entry(Model):
    @classmethod
    def parse(cls, json):
        entry = cls()
        setattr(entry, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(entry, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return entry


class League(Model):
    @classmethod
    def parse(cls, json):
        league = cls()
        setattr(league, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "entries":
                    l = [Entry().parse(j) for j in v]
                    setattr(league, "entries", l)
                else:
                    setattr(league, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return league
