""" 
LEETCODE: 15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example2
Input: nums = [2,2,-4]
Output: [[-4, 2, 2]]

"""
"""
APPROACH:
Follow the two-sum approach while keeping the current value constant in the loop.
    threeSum = Current + left + right
If Sum < 0: Increement left
Sum > 0: Decreement Right.
Handle duplicates to ensure unique triplets are considered.
"""

def threeSum(nums): 
    res = []
    nums.sort()

    for idx, val in enumerate(nums):
        if val == nums[idx-1]:
            continue

        left, right = idx+1, len(nums)-1

        while left < right:
            threeSum = val + nums[left] + nums[right]

            if threeSum< 0:
                left += 1
            elif threeSum > 0:
                right -= 1
            else:
                res.append([val, nums[left], nums[right]])
                left += 1
                while nums[left] != nums[left-1] and left < right:
                    left += 1
    
    return res

nums = [-3,-3,1,2,3,4]
result = threeSum(nums)
print(result)