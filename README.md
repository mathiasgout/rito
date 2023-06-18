# Rito

Riot API python SDK

## Installation
Install from the github repository:
````bash
pip install git+https://github.com/mathiasgout/rito.git
````

## Exemple
````python
from rito.clients import RitoClient, ExtractorClient

rito = RitoClient(riot_api_key="my_riot_api_key", region="EUW")
extractor = ExtractorClient()

summoner_dict = rito.summoner.by_name("faker")
summoner = extractor.summoner.extract(summoner_dict)
print(summoner.name) # Faker
print(summoner.summoner_level) # 212
````