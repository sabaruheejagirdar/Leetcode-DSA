"""
Leetcode: 242- Valid Anagrams
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
"""
APPROACH:
1. Check lengths: If the lengths of the strings are different, return False
2. Count characters: Create dictionaries to count characters in each string
3. Compare counts: If the character counts in the dictionaries do not match, return False
"""

def isAnagram(s, t):


    if len(s) != len(t):
        return False

    dict_s, dict_t = {}, {}

    for i in range(len(s)):
        dict_s[s[i]] = 1 + dict_s.get(s[i],0)
        dict_t[t[i]] = 1 + dict_t.get(t[i],0)

    for key,value in dict_s.items():
        if dict_s[key] != dict_t.get(key,0):
            return False

    return True

s = "anagram";
t = "nagaram";
print(isAnagram(s,t));

