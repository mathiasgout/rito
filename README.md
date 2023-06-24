# Rito

Riot API python SDK

## Installation
Install from the github repository:
````bash
pip install git+https://github.com/mathiasgout/rito.git
````

## Exemple
````python
from rito import RitoClient, ExtractorClient

rito_client = RitoClient(riot_api_key="my_riot_api_key", region="EUW")
extractor_client = ExtractorClient()

summoner_dict = rito_client.summoner.by_name("faker")
summoner = extractor_client.summoner.extract(summoner_dict)
print(summoner.name) # Faker
print(summoner.summoner_level) # 212
````