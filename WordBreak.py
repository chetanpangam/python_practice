"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

def wordBreak(s, wordDict):
    queue = []
    queue.append(s)

    visited = set()

    while queue:
        word = queue.pop(0)

        if word in visited:
            continue
        else:
            if not word:
                return True
            
            visited.add(word)
            
            for w in wordDict:
                if word.startswith(w):
                    queue.append(word[len(w):])
                    break
            print(queue)

    
    return False


s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))