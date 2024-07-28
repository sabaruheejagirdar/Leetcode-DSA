""" 
LEETCODE: 11. Container With Most Water
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Example1
Input: height=[1,8,6,2,5,4,8,3,7]
Output: 49

Example2
Input: height = [1,1]
Output: 1
"""
"""
APPROACH:
1. Set the left pointer to the first index and the right pointer to the last.
2. Calculate the area using:
    length = minimum of the two heights
    width = difference between the right and left indices
    area = length * width
3. At every iteration, calculate the area and increment the pointer at the shorter line to potentially increase the area.
4. Return the maximum area found.
"""

def maxArea(height):

    left = 0
    right = len(height)-1
    res = 0

    while left < right:
        length = min(height[left], height[right])
        width = right - left
        area = length * width

        res = max(area, res)
        if height[left] < height[right]: 
            left += 1
        else: 
            right -= 1

    return res

def maxAreaBruteForce(height):
    res = 0
    for left in range(len(height)):
        for right in range(left+1, len(height)):
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            res = max(res, area)

    return res

height = [1,8,6,2,5,4,8,3,7]
result = maxArea(height)
resultBruteForce = maxAreaBruteForce(height)
print(result)
# print(resultBruteForce)