print("\n\n***** Working with List *****\n")

table_of_5 = range(5, 51, 5)
print(f"\nrange(5, 51, 5): {table_of_5}")

table_of_5 = list(table_of_5)
print(f"\nlist(range(5, 51, 5)): {table_of_5}")

print(f"\nmin(table_of_5): {min(table_of_5)}")

print(f"\nmax(table_of_5): {max(table_of_5)}")

print(f"\nmin(table_of_5): {sum(table_of_5)}")

print(f"\ntable_of_5[0:3] - index 3 exclusive: {table_of_5[0:3]}")

print(f"\ntable_of_5[:3]: {table_of_5[:3]}")

print(f"\ntable_of_5[3:]: {table_of_5[3:]}")

print(f"\ntable_of_5[-3:]: {table_of_5[-3:]}")

print(f"\ntable_of_5[:]: {table_of_5[:]}")
