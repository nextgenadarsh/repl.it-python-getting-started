print("\n\n***** JSON Data *****\n")

import json

numbers = list(range(1, 11))

with open('data/json_file.json', 'w') as jsonFile:
  json.dump(numbers, jsonFile)

with open('data/json_file.json') as jsonFile:
  jsonData = json.load(jsonFile)

print(jsonData)