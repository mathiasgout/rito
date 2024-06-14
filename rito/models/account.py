from rito.models.base_model import Model


class Account(Model):
    @classmethod
    def parse(cls, json):
        account = cls()
        setattr(account, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(account, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return account
