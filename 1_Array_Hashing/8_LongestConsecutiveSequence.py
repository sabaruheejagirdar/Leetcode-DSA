""" 
LEETCODE: 128. Longest Consecutive Sequence
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence. In O(n)

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
"""
APPROACH:
Imagine this on number line->   1,2,3,4,........,100,....,200

- 1,100,200 is the first digit of sequence because the previous digit doesn't exist i.e- 0,99,199
- Get the first digit
- Keep checking if the next exists and calculate its length
- Keep track of the longest sequence formed
"""


def longestConsecutive(nums):  
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of the sequence
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            longest = max(longest, length)
    
    return longest

nums = [0,3,7,2,5,8,4,6,0,1];
result = longestConsecutive(nums);
print(result)






