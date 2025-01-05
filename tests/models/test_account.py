from rito.models import account, base_model


def test_account_inheritance():
    isinstance(account.Account(), base_model.Model)


def test_account_parse():
    result = account.Account()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == account.Account
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"
