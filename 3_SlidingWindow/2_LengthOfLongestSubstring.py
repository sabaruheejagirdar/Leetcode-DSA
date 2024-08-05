""" 
LEETCODE: 3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "bbbbb"
Output: 1
"""
"""
APPROACH:
- Use a set (charSet) to store characters in the current window.
- Use two pointers (left and right) to represent the sliding window.
- Iterate with the right pointer over the string s.
- If s[right] is already in charSet, remove characters from charSet starting from s[left] until s[right] can be added.
- Add s[right] to charSet.
- Update the length of the longest substring without repeating characters.
"""
charSet = "bc"
s = "a b c abcbb"

def lengthOfLongestSubstring(s):
    charSet = set()
    left = 0
    lenOfLongest = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            print("++",s[left])
            left += 1
        charSet.add(s[right])
        lenOfLongest = max(lenOfLongest, right - left + 1)


    return lenOfLongest

s = "abcabcb b"
result = lengthOfLongestSubstring(s)
print(result)