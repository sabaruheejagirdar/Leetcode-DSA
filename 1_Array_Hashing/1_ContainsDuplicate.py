""" 
LEETCODE: 217- Contains Duplicate
Given an integer array nums, 
return true if any value appears at least twice in the array, and
return false if every element is distinct.

Example1
Input: nums = [1,2,3,1]
Output: true

Example2
Input: nums = [1,2,3,4]
Output: false

STEPS:
1. Create a SET to keep track of visited elements
2. If element exists in the SET, return true
        Else, add the element to the SET
3. All elements traversed and no duplicate found in SET then return false
"""

def containsDuplicate(nums):   
    numset = set();

    for i in nums:
        print("Num: ",i)
        if i in numset:
            return True
        numset.add(i);

    return False

nums = [1,2,78,4];
result = containsDuplicate(nums);
print(result)