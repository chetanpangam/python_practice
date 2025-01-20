'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''

def letterCombinations(s):
    result = []
    N = len(s)

    char_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def recurse(index, current):
        if index == N:
            result.append("".join(current))
            return
        
        letters = char_map.get(s[index])

        for ch in letters:
            current.append(ch)
            recurse(index + 1, current)
            current.pop()

        return
    
    recurse(0, [])
    return result

digits = "23"
print(digits, letterCombinations(digits))
digits = "2"
print(digits, letterCombinations(digits))
digits ='777'
print(digits, letterCombinations(digits))
