""" 
LEETCODE: 347- Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example1
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example2
Input: nums = [1], k = 1
Output: [1]
"""
"""
APPROACH:
[1,1,1,2,2,100]
i(count) -->    0      1        2      3       4       5       6
values   -->   []    [100]     [2]     [1]     []      []      []

1. Count Frequencies: 
    Use a dictionary to count the frequency of each element in the array.
2. Bucket Sort by Frequency: 
    Create a list of empty lists where the index represents the frequency of elements.
3. Populate the buckets with elements based on their frequencies.
4. Iterate over the buckets in reverse order to gather the top k frequent elements.
"""


def topKFrequent(nums, k):   

    countOfNum = dict()
    freq = [[] for i in range(len(nums)+1)]
    # freq: [[], [], [], [], [], [], [], [], [], []]

    for n in nums:
        countOfNum[n] = 1 + countOfNum.get(n,0)
    # countOfNum: {->3: 3, ->2: 1, ->9: 1, ->100: 1, ->110: 3}
    for key, value in countOfNum.items():
        freq[value].append(key)
    # freq: [[], [9,100,2], [], [3,110], [], [], [], [], [], []]

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    print(res)
    
    return False

nums = [3,3,3,2,9,100,110,110,110];
target = 2;
result = topKFrequent(nums, target);
print(result)