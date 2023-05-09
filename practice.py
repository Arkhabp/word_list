import requests

api_key = 'ce8fec5a-0280-41e8-9e8e-88d8b3f0f6df'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)