""" 
LEETCODE: 238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
"""
APPROACH:
At any given point a number will be product of 
- All the numbers before it(Prefix) and all the numbers after it(Postfix)

Input-          1       2       3       4

Prefix-         1       1       2       6
Postfix-        24      12      4       1
--------------------------------------------
RESULT-         24      12      8       6
--------------------------------------------
(Prefix * Postfix)
"""


def productExceptSelf(nums):   
    
    prefix = [1 for i in nums]
    postfix = [1 for i in nums]
    result = [1 for i in nums]
    

    for idx in range(len(nums)):
        if idx == 0:
            prefix[idx] = 1
        else:
            prefix[idx] = prefix[idx-1] * nums[idx-1]
    # Prefix [1, 1, 2, 6]      
    
    for idx in range(len(nums)-1,-1,-1):
        if idx == len(nums)-1:
            postfix[idx] = 1
        else:
            postfix[idx] = postfix[idx+1] * nums[idx+1]

    for idx in range(len(nums)):
        result[idx] = prefix[idx] * postfix[idx]

    print("Prefix", prefix)
    print("Postfix", postfix)
    print("Result", result)
    return result

nums = [1,2,3,4] 
result = productExceptSelf(nums)
print(result)



