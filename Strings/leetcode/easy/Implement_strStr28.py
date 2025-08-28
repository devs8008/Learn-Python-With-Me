#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#solution
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/7131363/implement-strstr-using-pythons-built-in-vqqos/

class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            index = haystack.find(needle)
            return index
        else:
            return -1
        
