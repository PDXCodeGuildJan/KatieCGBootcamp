import requests
import json
from yummly import Client

#### First try- worked... sort of. ####
# search = "Chicken"

# r = requests.get("http://api.yummly.com/v1/api/recipes?_app_id=243f40b9&_app_key=0b99d35c38f2043e163a04a97e9c5476&q&" + 
# 	search)

# data = r.json()

# print(json.dumps(data['matches'], indent=4, sort_keys=True))

########

TIMEOUT = 5.0
RETRIES = 0

client = Client(api_id="243f40b9", api_key="0b99d35c38f2043e163a04a97e9c5476", timeout=TIMEOUT, retries=RETRIES)
	
params = {
    'q': 'pork chops',
    'start': 0,
    'maxResult': 40,
    'requirePicutres': True,
    'allowedIngredient[]': ['salt', 'pepper'],
    'excludedIngredient[]': ['cumin', 'paprika'],
    'maxTotalTimeInSeconds': 3600,
    'facetField[]': ['ingredient', 'diet'],
    'flavor.meaty.min': 0.5,
    'flavor.meaty.max': 1,
    'flavor.sweet.min': 0,
    'flavor.sweet.max': 0.5,
    'nutrition.FAT.min': 0,
    'nutrition.FAT.max': 15
}

results = client.search(**params)
print(json.dumps(results.matches, indent=4, sort_keys=True))
# print(results.matches)

print('Total Matches:', results.totalMatchCount)
for match in results.matches:
    print('Recipe ID:', match.id)
    print('Recipe:', match.recipeName)
    print('Ingredients:')
    for x in match.ingredients:
    	print('\t' + x)
    print('Recipe:', match.recipeName)
    print('Rating:', match.rating)
    print('Total Time (mins):', match.totalTimeInSeconds / 60.0)
    print('----------------------------------------------------')

