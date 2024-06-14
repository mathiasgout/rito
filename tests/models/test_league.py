from rito.models import league, base_model


def test_entry_inheritance():
    isinstance(league.Entry(), base_model.Model)


def test_entry_parse():
    result = league.Entry()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == league.Entry
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_league_inheritance():
    isinstance(league.League(), base_model.Model)


def test_league_parse():
    result = league.League()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == league.League
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_league_parse_ENTRIES():
    result = league.League()
    a = result.parse({"lolXd": "xd", "entries": [{"lolXd": "xd"}]})

    assert len(a.entries) == 1
    assert a.entries[0]._json == {"lolXd": "xd"}
    assert type(a.entries[0]) == league.Entry
    assert a.entries[0].lol_xd == "xd"
