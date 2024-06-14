# Rito

Riot API python SDK

## Installation
Install from the github repository:
````bash
pip install git+https://github.com/mathiasgout/rito.git
````

## Exemple
````python
from rito import RitoClient

rito_client = RitoClient(riot_api_key="my_riot_api_key", region="EUW")

summoner = rito_client.account.by_riot_id(game_name="davlaf", tag_line="EUW")
print(summoner.puuid) # the summoner's PUUID
print(summoner.game_name) # davlaf
print(summoner.tag_line) # EUW
````
