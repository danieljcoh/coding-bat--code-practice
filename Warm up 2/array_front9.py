"""
PROBLEM: 

Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""


"""
THOUGHT PROCESS:

    I know that I have to cycle through all of the numbers to check if the number is a -.
    - There are also extra things to keep in mind for this challenge. It cannot be after the fourth index and if the index is too small, make sure not to go out of index.
    - I think looping through the array to see every item and compare it to the target num (9), we first need to the check the length if it's empty.
    - In the event we find a 9, we need to make sure that it's within the first four index spots which I can do by comparing the contents of the array at a specific index that I can keep track of using a for loop.
"""

def array_front9(nums):
    if len(nums) < 1:
        return False
    for i in range(len(nums)):
        if i >= 4:
            return False
        if nums[i] == 9:
            return True
    return False
        

"""
WHAT I LEARNED:

    - At first I was doing "for i in nums" and I kept getting a out of index error
    - I realized that what that does, is makes i = to the contents of nums, not the index at which the contents are at. So I knew to change it to range() to get the index numbers.

"""
