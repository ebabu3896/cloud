# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# Input: s = "anagram", t = "nagaram"

def find_anagram(s, t):
    hashT, hashS = {}, {}
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        hashT[t[i]] = 1 + hashT.get(t[i], 0)
        hashS[s[i]] = 1 + hashS.get(s[i], 0)
    for i in hashT:
        if hashT[i] != hashS[i]:
            return False 
    return True                      

s = "anagram"
t = "nagaram"
print(find_anagram(s, t))