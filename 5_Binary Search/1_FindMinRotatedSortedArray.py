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
[3,4,5,1,2]
- When left is smaller then right, its sorted array. Return left [3,4,5]
- When middle is part of left sorted array, then smaller number is part of right sorted array.
    nums[M] >= num[L]:
        search smaller element at right side
    else:
        search smaller element at left side
"""

def findMin(nums):   
    res = nums[0]
    L = 0
    R = len(nums)-1

    
    while L <= R:
        if nums[L] < nums[R]:
            res = min(res,nums[L])
            break
        
        M = (L+R) //2
        res = min(res, nums[M])

        if nums[M] >= nums[L]:
            L = M + 1
        else:
            R = M - 1
    
    return res

nums = [3,4,5,1,2]
# nums = [4,5,1,2,3]
result = findMin(nums)
print(result)