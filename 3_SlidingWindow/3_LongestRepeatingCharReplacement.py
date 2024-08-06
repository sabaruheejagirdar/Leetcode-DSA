""" 
424. Longest Repeating Character Replacement
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get 
after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
"""
"""
APPROACH:
- Sliding window represented by the left and right pointers.
- For each character s[right]:
    Increment the count of s[right] in the count dictionary.
    If the window size (right - left + 1) minus the count of the most frequent character exceeds k, increment the left pointer to shrink the window and decrement the count of s[left].
    Update res with the maximum length of the valid window.
"""

def  characterReplacement(s, k): 
    count = {} # contains frequency of characters in the current window.
    res = 0

    left = 0 # pointer to the start of the string.

    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right],0)

        if (right-left+1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right-left+1)

    return res

s= "AABABBA"
k = 1
result = characterReplacement(s, k)
print(result)