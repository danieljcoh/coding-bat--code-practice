"""
PROBLEM:
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab
"""

"""
THOUGHT PROCESS:
    - My original thought process was to find the len of the str because
    that's how many times we will cycle through the string
    - Then we need to only go up to a specific index.
    - So if we have a for i in range() algo that goes to the len of the str
    - We can print out the chars, slowly adding up to the word, little by little, sliced to the index of the cycle iteration we are on.
    
"""


def string_splosion(str):
    n = len(str)
    new_str = ""
    for i in range(n + 1):
        new_str += str[:i:]
    print(new_str)
    
string_splosion("Code")