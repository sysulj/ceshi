"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counter = Counter(s)
        for i in range(len(s)):
            if s_counter[s[i]] == 1:
                return i
        return -1


"""
 不用Counter函数  
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


"""

"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        return min([s.find(i) for i in string.ascii_lowercase if s.count(i) == 1] or [-1])