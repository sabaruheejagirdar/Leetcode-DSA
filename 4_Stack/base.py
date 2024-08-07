""" 
LEETCODE: 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "({[]})"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
"""
APPROACH:
- Use a stack to track opening parentheses and a dictionary to map closing parentheses to their corresponding opening ones.
- Iterate through the string, pushing opening parentheses to the stack and checking for matches with closing parentheses.
- Return true if the stack is empty at the end, indicating all parentheses are properly closed.
"""

def isValid(s):   

    dictP = {")":"(", "}":"{", "]":"["}
    stackP = []

    for i in s:
        if i in dictP:
            if stackP and stackP[-1] == dictP[i]:
                stackP.pop()
            else:
                return False
        else:
            stackP.append(i)


    return len(stackP) == 0

s = "()"
result = isValid(s)
print(result)