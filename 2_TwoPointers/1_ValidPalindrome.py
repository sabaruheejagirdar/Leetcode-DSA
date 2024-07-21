""" 
LEETCODE: 1- Two Sum
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""

"""
APPROACH:
   A_man,_a_plan,_a_canal:_Panama
  [L]                          [R]
- Assign Left and right
- Increement Left and decreement right until L==R or L>R
- Make sure to read only aphanumeric and skip others
"""

def isPalindrome(s): 
    l, r = 0, len(s) -1

    while l<r:
        while l<r and not alphaNum(s[l]):
            l += 1
        while r>l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        
        l,r = l+1, r-1

    return True

def alphaNum(character):

    return ((ord('A') <= ord(character) <= ord('Z')) or
            (ord('a') <= ord(character) <= ord('z')) or
            (ord('1') <= ord(character) <= ord('9')))

s = "A man, a plan, a canal: Panama"
result = isPalindrome(s);
print(result)



def unoptimized_isPalindrome(s):   

    newStr = ""

    for c in s:
        if c.isalnum():
            newStr += c.lower()

    return newStr == newStr[::-1]