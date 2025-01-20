"""
Given a string text, you want to use the characters of text to form as many instances of 
the word "balloon" as possible. You can use each character in text at most once. 

Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

"""
import collections
def maxNumberOfBalloons(text):
    
    char_map = collections.defaultdict(int)

    for ch in text:
        char_map[ch] = char_map.get(ch, 0) + 1

    max_balloons = min(char_map['b'], char_map['a'], char_map['n'], char_map['l']//2, char_map['o']//2)
    return max_balloons

text = "nlaebolko"
print(text, maxNumberOfBalloons(text))

text = "loonbalxballpoon"
print(text, maxNumberOfBalloons(text))

text = "leetcode"
print(text, maxNumberOfBalloons(text))