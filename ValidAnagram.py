"""
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    char_map = [0] * 26

    for i in range(len(s)):
        char_map[ord(s[i]) - 97] += 1
        char_map[ord(t[i]) - 97] -= 1

    return not any(char_map)

s = "anagram"
t = "nagaram"
print(f"Is '{s}' anagram of '{t}' ? ", isAnagram(s, t))

s = "rat"
t = "car"
print(f"Is '{s}' anagram of '{t}' ? ", isAnagram(s, t))

s = "rat"
t = "cart"
print(f"Is '{s}' anagram of '{t}' ? ", isAnagram(s, t))