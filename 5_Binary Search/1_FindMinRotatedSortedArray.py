""" 
LEETCODE: 153. Find Minimum in Rotated Sorted Array

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0

"""
"""
APPROACH:
Use binary search to find the minimum element in a rotated sorted array by comparing the middle element
with the left and right boundaries, adjusting the search range accordingly.
"""

def findMin(nums):   

    left = 0
    right = len(nums) - 1
    res = nums[0]
    while left<= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break

        mid = (left + right)// 2
        res = min(res, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid -1

    return res

nums = [3,4,5,1,2]
result = findMin(nums)
print(result)