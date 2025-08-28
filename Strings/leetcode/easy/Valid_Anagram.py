#242. Valid Anagram

#wo strings are considered anagrams if they have the same characters with the same frequency, but the order of the characters is different.

#To sort a string in Python, the most common and efficient method involves using the built-in sorted()

class Solution(object):
    def isAnagram(self, s, t):
        a = len(s)
        b = len(t)
        if a == b:
            c = sorted(s)
            d = sorted(t)
            if c == d:
                return True
            else:
                return False
        else:
            return False
        