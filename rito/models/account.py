from rito.models.base_model import Model


class Account(Model):
    @classmethod
    def parse(cls, json):
        account = cls()
        setattr(account, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(account, k, v)
        return account
