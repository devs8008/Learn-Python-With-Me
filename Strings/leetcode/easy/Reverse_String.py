#Reverse String 344

#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def reverseString(self, s):
        o = s.reverse()
        return o
    
class Solution(object):
    def reverseString(self, s):
        s.reverse()

# both works because we need to modify the existing array in place, not return a new one. 