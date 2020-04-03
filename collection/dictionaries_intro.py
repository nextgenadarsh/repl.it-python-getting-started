print("\n\n***** Dictionary *****\n")

print("\nDictionary is similar to JSON object")

# Don't use 'id' as it is reserved
city = {'code': 'hyd', 'name': 'Hyderabad', 'Alias': 'Hyderabad'}
print(f"\nCity Dictionary: {city}")
print(f"\ncity['name']: {city['name']}")

# adding new key/value
city['attractions'] = ['Golconda Fort', 'Charminar']

# getting value for key
print(f"\ncity['attractions']: {city['attractions']}")
print(f"\ncity.get('invalid', 'default value'): {city.get('invalid', 'default value')}")

# deleting key/value
del city['attractions']
print(f"\ndel city['attractions']: {city}")

# iterating through dictionary items
print("\nfor item in city.items():")
for item in city.items():
  print(f"\tDictionary Item: {item}")

print("\nfor key, value in city.items():")
for key, value in city.items():
  print(f"\tDictionary Item Key/Value: {key}:{value}")

print("\nfor key in city.keys():")
for key in city.keys():
  print(f"\tDictionary Item Key: {key}")

print("\nfor value in city.values():")
for value in city.values():
  print(f"\tDictionary Item Value: {value}")
