import random

print("\n***** Conditional Statements *****\n")

print("\nUsing 'if elif else' condition to show message based on random age:")

age = random.randrange(1, 100, 5);
if (age < 18):
  print("\nGrow up!")
elif (age < 40):
  print("\nIt is time for you to earn enough!")
elif (age < 60):
  print("\nYou are old enough to vote!")
else: # avoid else to be confident about scenarios your code should execute in
  print("\nSir, please take rest!")

cities=[]
print(f"\n\nCheck if cities is empty: if (cities): {cities}")
if(cities):
  print(f"\nCities are: {cities}")
else:
  print("\nThere is no city")
