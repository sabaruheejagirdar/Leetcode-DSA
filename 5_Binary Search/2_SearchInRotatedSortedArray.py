""" 
LEETCODE: 33. Search in Rotated Sorted Array
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
"""
APPROACH:
Use Binary Search.
First check if the middle element matches the target, then determines whether the left or right half of the array is sorted. 
Depending on where the target could potentially lie, it adjusts the search range accordingly. Handle edge cases by shrinking the range.
"""

def search(nums, target):   
    n = len(nums)  # size of the array
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # if mid points to the target
        if nums[mid] == target:
            return mid

        # Edge case:
        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue

        # if left part is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if nums[mid] <= target <= nums[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1

    return -1

nums = [4,5,6,7,0,1,2]
target = 0
result = search(nums, target)
print(result)