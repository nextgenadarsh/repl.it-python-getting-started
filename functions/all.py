
"""Check eligiblity to cast vote"""
def isEligibleToVote(age):
  return None if age is None else False if age < 18 else True


""" Arguments Demo """
def cast_vote(age, name = 'Guest', *childrenNames):
  print(f"\nHello {name.title()}!")

  isEligible = isEligibleToVote(age)

  if isEligible is None:
    print("Please share your age to check eligibility to vote.")
  else:
    print(f"You are {'' if isEligible else 'not '}eligible to vote.")
  
  print(f"Your childrens are:")
  for index, children in enumerate(childrenNames):
    print(f"\t{index+1}.: {children}")

""" Arbitrary Named Arguments """
def build_profile(**profileInfo):
  profileInfo['isVerified'] = True;
  return profileInfo;

# Pass None
cast_vote(None)
# Postional argument
cast_vote(34, "adarsh kumar")
# Keyword argument
cast_vote(name="adarsh kumar", age=14)
# Default Arguments
cast_vote(12)
# Arbitrary number of Arguments
cast_vote(34, 'Brad', 'Paul', 'Samy')

# Arbitrary Named Arguments
userProfile = build_profile(firstChild='Tina', secondChild='Samy')
print(f"\nUser Profile: {userProfile}")
