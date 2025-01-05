from rito.models.base_model import Model


class Entry(Model):
    @classmethod
    def parse(cls, json):
        entry = cls()
        setattr(entry, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(entry, k, v)
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
                    setattr(league, k, l)
                else:
                    setattr(league, k, v)
        return league
