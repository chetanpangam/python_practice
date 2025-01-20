'''
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
'''

def minOperation(s):
    mismatch_0 = 0
    mismatch_1 = 0

    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '0':
                mismatch_1 += 1
            else:
                mismatch_0 += 1
        else:
            if s[i] == '1':
                mismatch_1 += 1
            else:
                mismatch_0 += 1
    print(mismatch_0, mismatch_1)
    return min(mismatch_0, mismatch_1)

s= '0100001'
s = '010'
s = "1110111"
print(minOperation(s))