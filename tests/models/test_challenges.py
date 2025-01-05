from rito.models import challenges, base_model


def test_localizednames_inheritance():
    isinstance(challenges.LocalizedNames(), base_model.Model)


def test_localizednames_parse():
    result = challenges.LocalizedNames()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == challenges.LocalizedNames
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_challengesconfig_inheritance():
    isinstance(challenges.ChallengesConfig(), base_model.Model)


def test_challengesconfig_parse():
    result = challenges.ChallengesConfig()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == challenges.ChallengesConfig
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_challengesconfig_parse_LOCALIZEDNAMES():
    result = challenges.ChallengesConfig()
    a = result.parse({"lolXd": "xd", "localizedNames": {"lolXd": "xd"}})

    assert a.localizedNames._json == {"lolXd": "xd"}
    assert type(a.localizedNames) == challenges.LocalizedNames
    assert a.localizedNames.lolXd == "xd"


def test_leaderboardplayer_inheritance():
    isinstance(challenges.LeaderboardPlayer(), base_model.Model)


def test_leaderboardplayer_parse():
    result = challenges.LeaderboardPlayer()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == challenges.LeaderboardPlayer
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_challengeplayerinformation_inheritance():
    isinstance(challenges.ChallengePlayerInformation(), base_model.Model)


def test_challengeplayerinformation_parse():
    result = challenges.ChallengePlayerInformation()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == challenges.ChallengePlayerInformation
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_challengesplayerinformation_inheritance():
    isinstance(challenges.ChallengesPlayerInformation(), base_model.Model)


def test_challengesplayerinformation_parse():
    result = challenges.ChallengesPlayerInformation()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == challenges.ChallengesPlayerInformation
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_challengesplayerinformation_parse_CHALLENGES():
    result = challenges.ChallengesPlayerInformation()
    a = result.parse({"lolXd": "xd", "challenges": [{"lolXd": "xd"}]})

    assert len(a.challenges) == 1
    assert a.challenges[0]._json == {"lolXd": "xd"}
    assert type(a.challenges[0]) == challenges.ChallengePlayerInformation
    assert a.challenges[0].lolXd == "xd"