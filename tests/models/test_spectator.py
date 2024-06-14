from rito.models import spectator, base_model


def test_perksactivegames_inheritance():
    isinstance(spectator.PerksActiveGame(), base_model.Model)


def test_perksactivegames_parse():
    result = spectator.PerksActiveGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.PerksActiveGame
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_participantactivegames_inheritance():
    isinstance(spectator.ParticipantActiveGame(), base_model.Model)


def test_participantactivegames_parse():
    result = spectator.ParticipantActiveGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.ParticipantActiveGame
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_participantactivegames_parse_PERKS():
    result = spectator.ParticipantActiveGame()
    a = result.parse({"lolXd": "xd", "perks": {"lolXd": "xd"}})

    assert a.perks._json == {"lolXd": "xd"}
    assert type(a.perks) == spectator.PerksActiveGame
    assert a.perks.lol_xd == "xd"


def test_observers_inheritance():
    isinstance(spectator.Observers(), base_model.Model)


def test_observers_parse():
    result = spectator.Observers()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.Observers
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_bannedchampion_inheritance():
    isinstance(spectator.BannedChampion(), base_model.Model)


def test_bannedchampion_parse():
    result = spectator.BannedChampion()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.BannedChampion
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_activegame_inheritance():
    isinstance(spectator.ActiveGame(), base_model.Model)


def test_activegame_parse():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.ActiveGame
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_activegame_parse_OBSERVERS():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd", "observers": {"lolXd": "xd"}})

    assert a.observers._json == {"lolXd": "xd"}
    assert type(a.observers) == spectator.Observers
    assert a.observers.lol_xd == "xd"


def test_activegame_parse_PARTICIPANTS():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd", "participants": [{"lolXd": "xd"}]})

    assert len(a.participants) == 1
    assert a.participants[0]._json == {"lolXd": "xd"}
    assert type(a.participants[0]) == spectator.ParticipantActiveGame
    assert a.participants[0].lol_xd == "xd"


def test_activegame_parse_BANNEDCHAMPIONS():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd", "bannedChampions": [{"lolXd": "xd"}]})

    assert len(a.banned_champions) == 1
    assert a.banned_champions[0]._json == {"lolXd": "xd"}
    assert type(a.banned_champions[0]) == spectator.BannedChampion
    assert a.banned_champions[0].lol_xd == "xd"
