from rito.models import match, base_model


def test_metadata_inheritance():
    isinstance(match.Metadata(), base_model.Model)


def test_metadata_parse():
    result = match.Metadata()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Metadata
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_ban_inheritance():
    isinstance(match.Ban(), base_model.Model)


def test_ban_parse():
    result = match.Ban()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Ban
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_objectives_inheritance():
    isinstance(match.Objectives(), base_model.Model)


def test_objectives_parse():
    result = match.Objectives()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Objectives
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_team_inheritance():
    isinstance(match.Team(), base_model.Model)


def test_team_parse():
    result = match.Team()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Team
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_team_parse_BANS():
    result = match.Team()
    a = result.parse({"lolXd": "xd", "bans": [{"lolXd": "xd"}]})

    assert len(a.bans) == 1
    assert a.bans[0]._json == {"lolXd": "xd"}
    assert type(a.bans[0]) == match.Ban
    assert a.bans[0].lolXd == "xd"


def test_team_parse_OBJECTIVES():
    result = match.Team()
    a = result.parse({"lolXd": "xd", "objectives": {"lolXd": "xd"}})

    assert a.objectives._json == {"lolXd": "xd"}
    assert type(a.objectives) == match.Objectives
    assert a.objectives.lolXd == "xd"


def test_challenges_inheritance():
    isinstance(match.Challenges(), base_model.Model)


def test_challenges_parse():
    result = match.Challenges()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Challenges
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_missions_inheritance():
    isinstance(match.Missions(), base_model.Model)


def test_missions_parse():
    result = match.Missions()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Missions
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_styles_inheritance():
    isinstance(match.Styles(), base_model.Model)


def test_styles_parse():
    result = match.Styles()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Styles
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_perks_inheritance():
    isinstance(match.PerksMatch(), base_model.Model)


def test_perks_parse():
    result = match.PerksMatch()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.PerksMatch
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_perks_parse_STYLES():
    result = match.PerksMatch()
    a = result.parse({"lolXd": "xd", "styles": [{"lolXd": "xd"}]})

    assert len(a.styles) == 1
    assert a.styles[0]._json == {"lolXd": "xd"}
    assert type(a.styles[0]) == match.Styles
    assert a.styles[0].lolXd == "xd"


def test_participant_inheritance():
    isinstance(match.ParticipantMatch(), base_model.Model)


def test_participant_parse():
    result = match.ParticipantMatch()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.ParticipantMatch
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_participant_parse_CHALLENGES():
    result = match.ParticipantMatch()
    a = result.parse({"lolXd": "xd", "challenges": {"lolXd": "xd"}})

    assert a.challenges._json == {"lolXd": "xd"}
    assert type(a.challenges) == match.Challenges
    assert a.challenges.lolXd == "xd"


def test_participant_parse_MISSIONS():
    result = match.ParticipantMatch()
    a = result.parse({"lolXd": "xd", "missions": {"lolXd": "xd"}})

    assert a.missions._json == {"lolXd": "xd"}
    assert type(a.missions) == match.Missions
    assert a.missions.lolXd == "xd"


def test_participant_parse_PERKS():
    result = match.ParticipantMatch()
    a = result.parse({"lolXd": "xd", "perks": {"lolXd": "xd"}})

    assert a.perks._json == {"lolXd": "xd"}
    assert type(a.perks) == match.PerksMatch
    assert a.perks.lolXd == "xd"


def test_infomatch_inheritance():
    isinstance(match.InfoMatch(), base_model.Model)


def test_infomatch_parse():
    result = match.InfoMatch()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.InfoMatch
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_infomatch_parse_TEAMS():
    result = match.InfoMatch()
    a = result.parse({"lolXd": "xd", "teams": [{"lolXd": "xd"}]})

    assert len(a.teams) == 1
    assert a.teams[0]._json == {"lolXd": "xd"}
    assert type(a.teams[0]) == match.Team
    assert a.teams[0].lolXd == "xd"


def test_infomatch_parse_PARTICIPANTS():
    result = match.InfoMatch()
    a = result.parse({"lolXd": "xd", "participants": [{"lolXd": "xd"}]})

    assert len(a.participants) == 1
    assert a.participants[0]._json == {"lolXd": "xd"}
    assert type(a.participants[0]) == match.ParticipantMatch
    assert a.participants[0].lolXd == "xd"


def test_match_inheritance():
    isinstance(match.Match(), base_model.Model)


def test_match_parse():
    result = match.Match()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Match
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_match_parse_METADATA():
    result = match.Match()
    a = result.parse({"lolXd": "xd", "metadata": {"lolXd": "xd"}})

    assert a.metadata._json == {"lolXd": "xd"}
    assert type(a.metadata) == match.Metadata
    assert a.metadata.lolXd == "xd"


def test_match_parse_INFO():
    result = match.Match()
    a = result.parse({"lolXd": "xd", "info": {"lolXd": "xd"}})

    assert a.info._json == {"lolXd": "xd"}
    assert type(a.info) == match.InfoMatch
    assert a.info.lolXd == "xd"


def test_participanttimeline_inheritance():
    isinstance(match.ParticipantTimeline(), base_model.Model)


def test_participanttimeline_parse():
    result = match.ParticipantTimeline()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.ParticipantTimeline
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_championstats_inheritance():
    isinstance(match.ChampionStats(), base_model.Model)


def test_championstats_parse():
    result = match.ChampionStats()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.ChampionStats
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_damagestats_inheritance():
    isinstance(match.DamageStats(), base_model.Model)


def test_damagestats_parse():
    result = match.DamageStats()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.DamageStats
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_participantframe_inheritance():
    isinstance(match.ParticipantFrame(), base_model.Model)


def test_participantframe_parse():
    result = match.ParticipantFrame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.ParticipantFrame
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_participantframe_parse_CHAMPIONSTATS():
    result = match.ParticipantFrame()
    a = result.parse({"lolXd": "xd", "championStats": {"lolXd": "xd"}})

    assert a.championStats._json == {"lolXd": "xd"}
    assert type(a.championStats) == match.ChampionStats
    assert a.championStats.lolXd == "xd"


def test_participantframe_parse_DAMAGESTATS():
    result = match.ParticipantFrame()
    a = result.parse({"lolXd": "xd", "damageStats": {"lolXd": "xd"}})

    assert a.damageStats._json == {"lolXd": "xd"}
    assert type(a.damageStats) == match.DamageStats
    assert a.damageStats.lolXd == "xd"


def test_event_inheritance():
    isinstance(match.ParticipantFrame(), base_model.Model)


def test_event_parse():
    result = match.Event()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Event
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_frame_inheritance():
    isinstance(match.Frame(), base_model.Model)


def test_frame_parse():
    result = match.Frame()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Frame
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_frame_parse_PARTICIPANTFRAMES():
    result = match.Frame()
    a = result.parse({"lolXd": "xd", "participantFrames": {"1": {"lolXd": "xd"}}})

    assert type(a.participantFrames) == dict
    assert a.participantFrames["1"]._json == {"lolXd": "xd"}
    assert type(a.participantFrames["1"]) == match.ParticipantFrame
    assert a.participantFrames["1"].lolXd == "xd"


def test_frame_parse_EVENTS():
    result = match.Frame()
    a = result.parse({"lolXd": "xd", "events": [{"lolXd": "xd"}]})

    assert len(a.events) == 1
    assert a.events[0]._json == {"lolXd": "xd"}
    assert type(a.events[0]) == match.Event
    assert a.events[0].lolXd == "xd"


def test_infotimeline_inheritance():
    isinstance(match.InfoTimeline(), base_model.Model)


def test_infotimeline_parse():
    result = match.InfoTimeline()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.InfoTimeline
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_infotimeline_parse_PARTICIPANTS():
    result = match.InfoTimeline()
    a = result.parse({"lolXd": "xd", "participants": [{"lolXd": "xd"}]})

    assert len(a.participants) == 1
    assert a.participants[0]._json == {"lolXd": "xd"}
    assert type(a.participants[0]) == match.ParticipantTimeline
    assert a.participants[0].lolXd == "xd"


def test_infotimeline_parse_FRAMES():
    result = match.InfoTimeline()
    a = result.parse({"lolXd": "xd", "frames": [{"lolXd": "xd"}]})

    assert len(a.frames) == 1
    assert a.frames[0]._json == {"lolXd": "xd"}
    assert type(a.frames[0]) == match.Frame
    assert a.frames[0].lolXd == "xd"


def test_timeline_inheritance():
    isinstance(match.Timeline(), base_model.Model)


def test_timeline_parse():
    result = match.Timeline()
    a = result.parse({"lolXd": "xd"})

    assert type(a) == match.Timeline
    assert a._json == {"lolXd": "xd"}
    assert a.lolXd == "xd"


def test_timeline_parse_METADATA():
    result = match.Timeline()
    a = result.parse({"lolXd": "xd", "metadata": {"lolXd": "xd"}})

    assert a.metadata._json == {"lolXd": "xd"}
    assert type(a.metadata) == match.Metadata
    assert a.metadata.lolXd == "xd"


def test_timeline_parse_INFO():
    result = match.Timeline()
    a = result.parse({"lolXd": "xd", "info": {"lolXd": "xd"}})

    assert a.info._json == {"lolXd": "xd"}
    assert type(a.info) == match.InfoTimeline
    assert a.info.lolXd == "xd"
