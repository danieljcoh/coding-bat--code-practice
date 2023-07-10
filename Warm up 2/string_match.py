"""
PROBLEM: 
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""


"""
THOUGHT PROCESS:
    - I have to make sure that the strs are long enough to have substring comparisons of 2 length long
    - I need to create new strs of the smaller substrings to compare to one another in order to get the proper count of matching substrings
    - I need to make sure that I am not going out-of-bounds of the length of the List.
    
"""

# MY ANSWER (INCOMPLETE // NOT WORKING)
def string_match(a, b):
    str1 = ""
    str2 = ""
    count = 0
    if len(a) < 3 or len(b) < 3:
        return 0
    bigger = max(a,b)
  
    for i in range(len(bigger) - 2):
        str1 = a[i:i+2]
        str2 = b[i:i+2]
        if str1 == str2:
            count += 1
      
    return count


# GIVEN SOLUTION
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count


"""
WHAT I LEARNED:

    - At first I was doing an "IF" statement to instantiate bigger but then I remembered there is a min() and max() methods I can use.
    - Secondly I was doing this: str_2 = b[i] + b[i + 1] to create a str_2 to compare to str_1 and I remembered I can use splicing instead.
"""