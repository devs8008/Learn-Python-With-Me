# 383 Ransom Note

#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.

#solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        b = list(magazine)   # turn magazine into a list (so we can remove letters)
        
        for ch in ransomNote:
            if ch in b:
                b.remove(ch)  # remove one occurrence of the letter
            else:
                return False  # letter not found → can't construct
        
        return True
