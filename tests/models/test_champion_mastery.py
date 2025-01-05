from rito.models import champion_mastery, base_model


def test_rewardconfig_inheritance():
    isinstance(champion_mastery.RewardConfig(), base_model.Model)


def test_rewardconfig_parse():
    result = champion_mastery.RewardConfig()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == champion_mastery.RewardConfig
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_nextseasonmilestone_inheritance():
    isinstance(champion_mastery.NextSeasonMilestone(), base_model.Model)


def test_nextseasonmilestone_parse():
    result = champion_mastery.NextSeasonMilestone()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == champion_mastery.NextSeasonMilestone
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_nextseasonmilestone_parse_REWARDCONFIG():
    result = champion_mastery.NextSeasonMilestone()
    a = result.parse({"lolXd": "xd", "rewardConfig": {"lolXd": "xd"}})

    assert a._json == {"lolXd": "xd", "rewardConfig": {"lolXd": "xd"}}
    assert a.rewardConfig._json == {"lolXd": "xd"}
    assert type(a.rewardConfig) == champion_mastery.RewardConfig
    assert a.rewardConfig.lolXd == "xd"


def test_championmastery_inheritance():
    isinstance(champion_mastery.ChampionMastery(), base_model.Model)


def test_championmastery_parse():
    result = champion_mastery.ChampionMastery()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == champion_mastery.ChampionMastery
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_championmastery_parse_NEXTSEASONMILESTONE():
    result = champion_mastery.ChampionMastery()
    a = result.parse({"lolXd": "xd", "nextSeasonMilestone": {"lolXd": "xd"}})

    assert a._json == {"lolXd": "xd", "nextSeasonMilestone": {"lolXd": "xd"}}
    assert a.nextSeasonMilestone._json == {"lolXd": "xd"}
    assert type(a.nextSeasonMilestone) == champion_mastery.NextSeasonMilestone
    assert a.nextSeasonMilestone.lolXd == "xd"
