"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


"""
交换
"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s =list(s)
        low = 0
        high = len(s)-1
        while low <= high:
            s[low],s[high] = s[high],s[low]
            low += 1
            high -= 1
        return "".join(s)