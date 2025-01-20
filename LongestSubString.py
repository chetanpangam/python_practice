"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""

def longestSubString(s):
    longest = 0
    start, end = 0, 0
    char_set = set()
    while end < len(s):
        while end < len(s) and s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        end += 1
        longest = max(longest, end - start)

    return longest

s = "abcabcbb"
print(s, longestSubString(s))

s = 'bbbbbb'
print(s, longestSubString(s))

s = "pwwkew"
print(s, longestSubString(s))