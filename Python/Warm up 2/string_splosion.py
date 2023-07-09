"""
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab
"""


def string_splosion(str):
    n = len(str)
    new_str = ""
    for i in range(n + 1):
        new_str += str[:i:]
    print(new_str)
    
string_splosion("Code")