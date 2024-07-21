""" 
LEETCODE: 1- Two Sum
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Example1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example2
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""
"""
APPROACH:
1. Create a dictionary to store indices of seen elements.
2. Iterate through the list.
3. Calculate potentialNum = target - nums[i].
4. If potentialNum is in the dictionary, return both indices.
5. Otherwise, add nums[i] and its index to the dictionary.
6. Return False if no two numbers add up to the target.
"""


def twoSum(nums, target):   
    seenElements = {}

    for i in range(len(nums)):
        potentialNum = target - nums[i]
        if potentialNum in seenElements:
            return[i, seenElements[potentialNum]]
        seenElements[nums[i]] = i

    return False

nums = [3,1,4,2];
target = 6
result = twoSum(nums, target);
print(result)