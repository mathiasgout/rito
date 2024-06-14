from rito.models import summoner, base_model


def test_summoner_inheritance():
    isinstance(summoner.Summoner(), base_model.Model)


def test_summoner_parse():
    result = summoner.Summoner()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == summoner.Summoner
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"
