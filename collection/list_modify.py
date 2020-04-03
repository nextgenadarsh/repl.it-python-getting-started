print("\n\n**** Modifying List *****\n")

cities = ["Hyderabad", "Mumbai", "Pune", "Mumbai"]
print(f"\nCities: {cities}")

print(f"cities[-1]: {cities[-1]}")

cities.append("Delhi")
print(f"\ncities.append('Delhi'): {cities}")

cities.insert(1, "Patna")
print(f"\ncities.insert(1, 'Patna'): {cities}")

del cities[1]
print(f"\ndel cities[1]: {cities}")

print(f"\ncities.pop(): {cities.pop()} : {cities}")

print(f"\ncities.pop(0): {cities.pop(0)} : {cities}")

print(f"\ncities.remove('Mumbai') removes 1st occurance: {cities.remove('Mumbai')} : {cities}")

