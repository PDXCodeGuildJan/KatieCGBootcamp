import requests
import json

search = "Corn"

r = requests.get("http://api.yummly.com/v1/api/recipes?_app_id=243f40b9&_app_key=0b99d35c38f2043e163a04a97e9c5476&q=" + 
	search)

data = r.json()

print(json.dumps(data['matches'], indent=4, sort_keys=True))