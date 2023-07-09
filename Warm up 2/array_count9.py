"""
PROBLEM: 
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""


"""
THOUGHT PROCESS:
    Initially I am aware that there is a count() function I can use that counts the number of a specified parameter.
"""

def array_count9(nums):
    counted = nums.count(9)
    print(counted)
    
array_count9([1, 9, 9, 3, 9])
        
