"""
PROBLEM: 
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""


"""
THOUGHT PROCESS:
    - Are the numbers assumed in a row or do I prepare for that?
    - I was trying to think of a python .contains() equivalent for Lists and I decided to use the count() method.
    - This way I can check regardless if the numbers are in a specified order or not. If they are it will still come out True.
"""

# MY ANSWER
def array123(nums):
  one = nums.count(1)
  if one:
    two = nums.count(2)
    if two:
      three = nums.count(3)
      if three:
        return True
  return False


# GIVEN ANSWER
def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False


"""
WHAT I LEARNED:

    - I was a little confused at first whether the problem wanted the numbers to be coded in a row or if simply 1, 2, 3 being in the array in any order.
    - After seing the given answer to the problem, I understand that the problem was looking for the numbers in a row.
"""