print("\n***** User Input *****\n")

name = input("Please enter your name: ")
print(f"\nWelcome: {name}!")

age = input("Please enter your age: ")
if int(age) > 18:
  print (f"You are an adult Mr. {name}!")
