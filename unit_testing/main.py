print("\n\n***** Unit Testing *****\n")

import unittest

from functions.all import isEligibleToVote

class VoteEligibilityTestCase(unittest.TestCase):
  def test_eligibility_check_false(self):
    can_vote = isEligibleToVote(13)
    self.assertEqual(can_vote, False)

  def test_eligibility_check_true(self):
    can_vote = isEligibleToVote(18)
    self.assertEqual(can_vote, True)

if __name__ == '__main__':
  unittest.main()

