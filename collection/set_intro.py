print("\n\n***** Set *****\n")

cities = {'Hyderabad', 'Pune', 'Mumbai', 'Hyderabad'}

#set removes duplicate 'Hyderabad'
print(f"\nCities: {cities}")

city = {'id': 'hyd', 'name': 'Hyderabad', 'alias': 'Hyderabad'}

print(f"\nShow unique values from dictionary: {city}")
print("\nfor value in set(city.values()):")
for value in set(city.values()):
  print(f"\tDictionary Item Value: {value}")