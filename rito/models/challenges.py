from rito.models.base_model import Model


class LocalizedNames(Model):
    @classmethod
    def parse(cls, json):
        localized_names = cls()
        setattr(localized_names, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(localized_names, k, v)
        return localized_names


class ChallengesConfig(Model):
    @classmethod
    def parse(cls, json):
        challenges_config = cls()
        setattr(challenges_config, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "localizedNames":
                    localized_names = LocalizedNames()
                    setattr(challenges_config, k, localized_names.parse(v))
                else:
                    setattr(challenges_config, k, v)
        return challenges_config


class LeaderboardPlayer(Model):
    @classmethod
    def parse(cls, json):
        leaderboard_player = cls()
        setattr(leaderboard_player, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(leaderboard_player, k, v)
        return leaderboard_player


class ChallengePlayerInformation(Model):
    @classmethod
    def parse(cls, json):
        challenge_player_information = cls()
        setattr(challenge_player_information, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(challenge_player_information, k, v)
        return challenge_player_information


class ChallengesPlayerInformation(Model):
    @classmethod
    def parse(cls, json):
        challenges_player_information = cls()
        setattr(challenges_player_information, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "challenges":
                    l = [ChallengePlayerInformation().parse(j) for j in v]
                    setattr(challenges_player_information, k, l)
                else:
                    setattr(challenges_player_information, k, v)
        return challenges_player_information
