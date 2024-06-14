from rito.models.base_model import Model


class Metadata(Model):
    @classmethod
    def parse(cls, json):
        metadata = cls()
        setattr(metadata, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(metadata, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return metadata


class Ban(Model):
    @classmethod
    def parse(cls, json):
        ban = cls()
        setattr(ban, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(ban, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return ban


class Objectives(Model):
    @classmethod
    def parse(cls, json):
        objectives = cls()
        setattr(objectives, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(objectives, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(team, "bans", l)
                elif k == "objectives":
                    objectives = Objectives()
                    setattr(team, "objectives", objectives.parse(v))
                else:
                    setattr(team, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return team
    

class Challenges(Model):
    @classmethod
    def parse(cls, json):
        challenges = cls()
        setattr(challenges, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(challenges, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return challenges
    

class Missions(Model):
    @classmethod
    def parse(cls, json):
        missions = cls()
        setattr(missions, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(missions, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return missions
    

class Styles(Model):
    @classmethod
    def parse(cls, json):
        styles = cls()
        setattr(styles, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(styles, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(perks, "styles", l)
                else:
                    setattr(perks, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(participant, "challenges", challenges.parse(v))
                elif k == "missions":
                    missions = Missions()
                    setattr(participant, "missions", missions.parse(v))
                elif k == "perks":
                    perks = PerksMatch()
                    setattr(participant, "perks", perks.parse(v))
                else:
                    setattr(participant, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(info, "teams", l)
                elif k == "participants":
                    l = [ParticipantMatch().parse(j) for j in v]
                    setattr(info, "participants", l)
                else:
                    setattr(info, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(match, "metadata", metadata.parse(v))
                elif k == "info":
                    info = InfoMatch()
                    setattr(match, "info", info.parse(v))
                else:
                    setattr(match, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return match


class ParticipantTimeline(Model):
    @classmethod
    def parse(cls, json):
        participant = cls()
        setattr(participant, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(participant, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return participant


class ChampionStats(Model):
    @classmethod
    def parse(cls, json):
        champion_stats = cls()
        setattr(champion_stats, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(champion_stats, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return champion_stats


class DamageStats(Model):
    @classmethod
    def parse(cls, json):
        damage_stats = cls()
        setattr(damage_stats, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(damage_stats, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(participant_frame, "champion_stats", champion_stats.parse(v))
                elif k == "damageStats":
                    damage_stats = DamageStats()
                    setattr(participant_frame, "damage_stats", damage_stats.parse(v))
                else:
                    setattr(participant_frame, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return participant_frame


class Event(Model):
    @classmethod
    def parse(cls, json):
        event = cls()
        setattr(event, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(event, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(frame, "participant_frames", d)
                elif k == "events":
                    l = [Event().parse(j) for j in v]
                    setattr(frame, "events", l)
                else:
                    setattr(frame, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(info, "participants", l)
                elif k == "frames":
                    l = [Frame().parse(j) for j in v]
                    setattr(info, "frames", l)
                else:
                    setattr(info, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
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
                    setattr(timeline, "metadata", metadata.parse(v))
                elif k == "info":
                    info = InfoTimeline()
                    setattr(timeline, "info", info.parse(v))
                else:
                    setattr(timeline, cls._format_attribute_name(self=cls, raw_attribute_name=k), v)
        return timeline
