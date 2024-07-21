""" 
LEETCODE: 15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example2
Input: nums = [0,1,1]
Output: []
"""
"""
APPROACH:
"""

def threeSum(nums): 

    for i in range(len(nums)):
        while l < r:
        l, r = i+1, len(nums)-1
        while nums[l] == nums[i]:
            l += 1
        while nums[r] == nums[i]:
            r -= 1
        
        whi


    return False

nums = [-3,-3,1,2,3,4]
result = threeSum(nums)
print(result)