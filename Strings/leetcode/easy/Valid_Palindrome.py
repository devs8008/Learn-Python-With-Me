#125. Valid Palindrome
#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# https://leetcode.com/problems/valid-palindrome/solutions/7131236/solution-valid-palindrome-using-string-f-jd3z/


class Solution(object):
    def isPalindrome(self, s):
        a = ""
        for x in s:
            if x.isalpha() or x.isdigit():
                a = a + x.lower()
        b = a[::-1]
        if a == b:
            return True
        else:
            return False      
