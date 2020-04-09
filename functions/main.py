title = "Functions"
print(f"\n\n{title.center(50, '*')}\n")

print("\n\n***** Importing Specific Functions from Module *****\n")

from functions.all import cast_vote as castYourVote, build_profile

# Import happens only once
import functions.all as allFunctions
import functions.all as allFunctions

# Importing all functions in module
from functions.all import *

# Alias for functions
cast_vote(67)



# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
