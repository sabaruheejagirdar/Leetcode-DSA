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
result = groupAnagrams(strs);
print(result)