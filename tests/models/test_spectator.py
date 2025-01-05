from rito.models import spectator, base_model


def test_perksactivegames_inheritance():
    isinstance(spectator.PerksActiveGame(), base_model.Model)


def test_perksactivegames_parse():
    result = spectator.PerksActiveGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.PerksActiveGame
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_participantactivegames_inheritance():
    isinstance(spectator.ParticipantActiveGame(), base_model.Model)


def test_participantactivegames_parse():
    result = spectator.ParticipantActiveGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.ParticipantActiveGame
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_participantactivegames_parse_PERKS():
    result = spectator.ParticipantActiveGame()
    a = result.parse({"lolXd": "xd", "perks": {"lolXd": "xd"}})

    assert a.perks._json == {"lolXd": "xd"}
    assert type(a.perks) == spectator.PerksActiveGame
    assert a.perks.lolXd == "xd"


def test_observers_inheritance():
    isinstance(spectator.Observers(), base_model.Model)


def test_observers_parse():
    result = spectator.Observers()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.Observers
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_bannedchampion_inheritance():
    isinstance(spectator.BannedChampion(), base_model.Model)


def test_bannedchampion_parse():
    result = spectator.BannedChampion()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.BannedChampion
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_activegame_inheritance():
    isinstance(spectator.ActiveGame(), base_model.Model)


def test_activegame_parse():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.ActiveGame
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_activegame_parse_OBSERVERS():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd", "observers": {"lolXd": "xd"}})

    assert a.observers._json == {"lolXd": "xd"}
    assert type(a.observers) == spectator.Observers
    assert a.observers.lolXd == "xd"


def test_activegame_parse_PARTICIPANTS():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd", "participants": [{"lolXd": "xd"}]})

    assert len(a.participants) == 1
    assert a.participants[0]._json == {"lolXd": "xd"}
    assert type(a.participants[0]) == spectator.ParticipantActiveGame
    assert a.participants[0].lolXd == "xd"


def test_activegame_parse_BANNEDCHAMPIONS():
    result = spectator.ActiveGame()
    a = result.parse({"lolXd": "xd", "bannedChampions": [{"lolXd": "xd"}]})

    assert len(a.bannedChampions) == 1
    assert a.bannedChampions[0]._json == {"lolXd": "xd"}
    assert type(a.bannedChampions[0]) == spectator.BannedChampion
    assert a.bannedChampions[0].lolXd == "xd"


def test_participantfeaturedgame_inheritance():
    isinstance(spectator.ParticipantFeaturedGame(), base_model.Model)


def test_participantfeaturedgame_parse():
    result = spectator.ParticipantFeaturedGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.ParticipantFeaturedGame
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_featuredgame_inheritance():
    isinstance(spectator.FeaturedGame(), base_model.Model)


def test_featuredgame_parse():
    result = spectator.FeaturedGame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.FeaturedGame
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_featuredgame_parse_PARTICIPANTS():
    result = spectator.FeaturedGame()
    a = result.parse({"lolXd": "xd", "participants": [{"lolXd": "xd"}]})

    assert len(a.participants) == 1
    assert a.participants[0]._json == {"lolXd": "xd"}
    assert type(a.participants[0]) == spectator.ParticipantFeaturedGame
    assert a.participants[0].lolXd == "xd"


def test_featuredgames_inheritance():
    isinstance(spectator.FeaturedGames(), base_model.Model)


def test_featuredgames_parse():
    result = spectator.FeaturedGames()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == spectator.FeaturedGames
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_featuredgame_parse_GAMELISTS():
    result = spectator.FeaturedGames()
    a = result.parse({"lolXd": "xd", "gameList": [{"lolXd": "xd"}]})

    assert len(a.gameList) == 1
    assert a.gameList[0]._json == {"lolXd": "xd"}
    assert type(a.gameList[0]) == spectator.FeaturedGame
    assert a.gameList[0].lolXd == "xd"
