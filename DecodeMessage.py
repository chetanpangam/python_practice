"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively.

The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example: 
given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"

Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
Output: "the five boxing wizards jump quickly"
"""

def decodeMessage(key, message):
    
    index = 97
    conversion = [0] * 26
    result = [" "] * len(message)

    for ch in key:
        if ch.isalpha() and not conversion[ord(ch) - 97]:
            conversion[ord(ch) - 97] = chr(index)
            index += 1
    
    for i in range(len(message)):
        if message[i].isalpha():
            result[i] = conversion[ord(message[i]) - 97]
    
    return "".join(result)

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(message + "\n" + decodeMessage(key, message))

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(message + "\n" +  decodeMessage(key, message))