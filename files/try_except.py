title = "Exception Handling"
print(f"\n\n{title.center(50, '*')}\n")


import sys
import traceback

first_number = input("Enter a number: ")
second_number = input("Enter second number: ")

try:
  answer = int(first_number)/int(second_number)
except ZeroDivisionError:
  print(sys.exc_info()[0])
  print(traceback.format_exc())
  print(f"You can not divide by zero")
except Exception as e:
  print(f"Error occured: {e.__str__()}")
  # print(traceback.format_exc())
  
  pass      # Fail silently
  raise     # Raise exception to calling code block
else:
  print(f"\n{first_number}/{second_number} = {answer}")

