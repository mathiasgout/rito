from rito.models import champion, base_model


def test_championrotations_inheritance():
    isinstance(champion.ChampionRotations(), base_model.Model)


def test_championrotations_parse():
    result = champion.ChampionRotations()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == champion.ChampionRotations
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"
