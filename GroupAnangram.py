"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.


Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""
import collections
def groupAnagram(strs):
    result = collections.defaultdict(list)
    for str in strs:
        char_map = [0] * 26
        for ch in str:
            char_map[ord(ch) - 97] += 1
        result[tuple(char_map)].append(str)

    return [val for val in result.values()]

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))

strs = [""]
print(groupAnagram(strs))

strs = ["a"]
print(groupAnagram(strs))