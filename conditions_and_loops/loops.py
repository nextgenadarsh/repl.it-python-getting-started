print("\n***** Loops *****\n")

print("\nfor num in list(range(5, 51, 5))")
for num in list(range(5, 51, 5)):
  if num == 15:
    continue;
  if num == 45:
    break;
  print (num)

print(f"[value ** 2 for value in range(1, 11)]: {[value ** 2 for value in range(1, 11)]}")

print("\nwhile loop")
num = 0
while num < 5:
  num += 1
  print(num)
