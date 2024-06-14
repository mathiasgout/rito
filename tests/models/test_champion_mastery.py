from rito.models import champion_mastery, base_model


def test_rewardconfig_inheritance():
    isinstance(champion_mastery.RewardConfig(), base_model.Model)


def test_rewardconfig_parse():
    result = champion_mastery.RewardConfig()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == champion_mastery.RewardConfig
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_nextseasonmilestone_inheritance():
    isinstance(champion_mastery.NextSeasonMilestone(), base_model.Model)


def test_nextseasonmilestone_parse():
    result = champion_mastery.NextSeasonMilestone()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == champion_mastery.NextSeasonMilestone
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_nextseasonmilestone_parse_REWARDCONFIG():
    result = champion_mastery.NextSeasonMilestone()
    a = result.parse({"lolXd": "xd", "rewardConfig": {"lolXd": "xd"}})

    assert a._json == {"lolXd": "xd", "rewardConfig": {"lolXd": "xd"}}
    assert a.reward_config._json == {"lolXd": "xd"}
    assert type(a.reward_config) == champion_mastery.RewardConfig
    assert a.reward_config.lol_xd == "xd"


def test_championmastery_inheritance():
    isinstance(champion_mastery.ChampionMastery(), base_model.Model)


def test_championmastery_parse():
    result = champion_mastery.ChampionMastery()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == champion_mastery.ChampionMastery
    assert a._json == {"lolXd": "xd"}
    assert a.lol_xd == "xd"


def test_championmastery_parse_NEXTSEASONMILESTONE():
    result = champion_mastery.ChampionMastery()
    a = result.parse({"lolXd": "xd", "nextSeasonMilestone": {"lolXd": "xd"}})

    assert a._json == {"lolXd": "xd", "nextSeasonMilestone": {"lolXd": "xd"}}
    assert a.next_season_milestone._json == {"lolXd": "xd"}
    assert type(a.next_season_milestone) == champion_mastery.NextSeasonMilestone
    assert a.next_season_milestone.lol_xd == "xd"
