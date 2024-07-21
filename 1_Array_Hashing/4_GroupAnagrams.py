""" 
LEETCODE: 49. Group Anagrams
Given an array of strings strs, group the anagrams together. 
An Anagram is a word or phrase formed by rearranging the letters exactly once.

Example1
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example2
Input: strs = [""]
Output: [[""]]

APPROACH:
1. Create a dictionary to track anagrams.
2. Traverse each string, sort it, and check if the sorted string exists in the dictionary.
3. If not found, add the sorted string as a key and 
   the current string as the first element in the value list.
4. If found, append the current string to the list of values for the sorted string key.
5. Return the dictionary values, which represent the grouped anagrams.
"""









def groupAnagrams(strs):   
    dictOfAnagrams = dict()

    for i in strs:
        sortedWord = "".join(sorted(i))
        if sortedWord not in dictOfAnagrams.keys():
            dictOfAnagrams[sortedWord] = [i]
        else:
            dictOfAnagrams[sortedWord].append(i)

    # print(list(dictOfAnagrams.values()))
    return list(dictOfAnagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
# result = groupAnagrams(strs)
# print(result)



def optimized_groupAnagrams(strs):   
    res = dict()

    for s in strs:
        count = [0] * 26  # a...z

        for c in s:
            count[ord(c) - ord("a")] += 1

        count_tuple = tuple(count)
        if count_tuple not in res:
            res[count_tuple] = []

        res[count_tuple].append(s)
        # print(res)

    return list(res.values())



strs = ["eat","tea","tan","ate","nat","bat"]
result = optimized_groupAnagrams(strs);
print(result)