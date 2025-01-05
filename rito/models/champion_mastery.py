from rito.models.base_model import Model


class RewardConfig(Model):
    @classmethod
    def parse(cls, json):
        reward_config = cls()
        setattr(reward_config, "_json", json)

        if json is not None:
            for k, v in json.items():
                setattr(reward_config, k, v)
        return reward_config
    

class NextSeasonMilestone(Model):
    @classmethod
    def parse(cls, json):
        next_season_milestone = cls()
        setattr(next_season_milestone, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "rewardConfig":
                    reward_config = RewardConfig()
                    setattr(next_season_milestone, k, reward_config.parse(v))
                else:
                    setattr(next_season_milestone, k, v)
        return next_season_milestone
    

class ChampionMastery(Model):
    @classmethod
    def parse(cls, json):
        champion_mastery = cls()
        setattr(champion_mastery, "_json", json)

        if json is not None:
            for k, v in json.items():
                if k == "nextSeasonMilestone":
                    next_season_milestone = NextSeasonMilestone()
                    setattr(champion_mastery, k, next_season_milestone.parse(v))
                else:
                    setattr(champion_mastery, k, v)
        return champion_mastery
