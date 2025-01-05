from rito.models.base_model import Model


class Metadata(Model):
    @classmethod
    def parse(cls, json):
        metadata = cls()
        setattr(metadata, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(metadata, k, v)
        return metadata


class Ban(Model):
    @classmethod
    def parse(cls, json):
        ban = cls()
        setattr(ban, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(ban, k, v)
        return ban


class Objectives(Model):
    @classmethod
    def parse(cls, json):
        objectives = cls()
        setattr(objectives, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(objectives, k, v)
        return objectives


class Team(Model):
    @classmethod
    def parse(cls, json):
        team = cls()
        setattr(team, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "bans":
                    l = [Ban().parse(j) for j in v]
                    setattr(team, k, l)
                elif k == "objectives":
                    objectives = Objectives()
                    setattr(team, k, objectives.parse(v))
                else:
                    setattr(team, k, v)
        return team
    

class Challenges(Model):
    @classmethod
    def parse(cls, json):
        challenges = cls()
        setattr(challenges, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(challenges, k, v)
        return challenges
    

class Missions(Model):
    @classmethod
    def parse(cls, json):
        missions = cls()
        setattr(missions, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(missions, k, v)
        return missions
    

class Styles(Model):
    @classmethod
    def parse(cls, json):
        styles = cls()
        setattr(styles, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(styles, k, v)
        return styles


class PerksMatch(Model):
    @classmethod
    def parse(cls, json):
        perks = cls()
        setattr(perks, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "styles":
                    l = [Styles().parse(j) for j in v]
                    setattr(perks, k, l)
                else:
                    setattr(perks, k, v)
        return perks


class ParticipantMatch(Model):
    @classmethod
    def parse(cls, json):
        participant = cls()
        setattr(participant, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "challenges":
                    challenges = Challenges()
                    setattr(participant, k, challenges.parse(v))
                elif k == "missions":
                    missions = Missions()
                    setattr(participant, k, missions.parse(v))
                elif k == "perks":
                    perks = PerksMatch()
                    setattr(participant, k, perks.parse(v))
                else:
                    setattr(participant, k, v)
        return participant


class InfoMatch(Model):
    @classmethod
    def parse(cls, json):
        info = cls()
        setattr(info, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "teams":
                    l = [Team().parse(j) for j in v]
                    setattr(info, k, l)
                elif k == "participants":
                    l = [ParticipantMatch().parse(j) for j in v]
                    setattr(info, k, l)
                else:
                    setattr(info, k, v)
        return info


class Match(Model):
    @classmethod
    def parse(cls, json):
        match = cls()
        setattr(match, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "metadata":
                    metadata = Metadata()
                    setattr(match, k, metadata.parse(v))
                elif k == "info":
                    info = InfoMatch()
                    setattr(match, k, info.parse(v))
                else:
                    setattr(match, k, v)
        return match


class ParticipantTimeline(Model):
    @classmethod
    def parse(cls, json):
        participant = cls()
        setattr(participant, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(participant, k, v)
        return participant


class ChampionStats(Model):
    @classmethod
    def parse(cls, json):
        champion_stats = cls()
        setattr(champion_stats, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(champion_stats, k, v)
        return champion_stats


class DamageStats(Model):
    @classmethod
    def parse(cls, json):
        damage_stats = cls()
        setattr(damage_stats, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(damage_stats, k, v)
        return damage_stats


class ParticipantFrame(Model):
    @classmethod
    def parse(cls, json):
        participant_frame = cls()
        setattr(participant_frame, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "championStats":
                    champion_stats = ChampionStats()
                    setattr(participant_frame, k, champion_stats.parse(v))
                elif k == "damageStats":
                    damage_stats = DamageStats()
                    setattr(participant_frame, k, damage_stats.parse(v))
                else:
                    setattr(participant_frame, k, v)
        return participant_frame


class Event(Model):
    @classmethod
    def parse(cls, json):
        event = cls()
        setattr(event, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(event, k, v)
        return event


class Frame(Model):
    @classmethod
    def parse(cls, json):
        frame = cls()
        setattr(frame, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "participantFrames":
                    d = {key:ParticipantFrame().parse(value) for key, value in v.items()}
                    setattr(frame, k, d)
                elif k == "events":
                    l = [Event().parse(j) for j in v]
                    setattr(frame, k, l)
                else:
                    setattr(frame, k, v)
        return frame


class InfoTimeline(Model):
    @classmethod
    def parse(cls, json):
        info = cls()
        setattr(info, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "participants":
                    l = [ParticipantTimeline().parse(j) for j in v]
                    setattr(info, k, l)
                elif k == "frames":
                    l = [Frame().parse(j) for j in v]
                    setattr(info, k, l)
                else:
                    setattr(info, k, v)
        return info


class Timeline(Model):
    @classmethod
    def parse(cls, json):
        timeline = cls()
        setattr(timeline, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "metadata":
                    metadata = Metadata()
                    setattr(timeline, k, metadata.parse(v))
                elif k == "info":
                    info = InfoTimeline()
                    setattr(timeline, k, info.parse(v))
                else:
                    setattr(timeline, k, v)
        return timeline
