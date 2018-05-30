"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。
示例:
输入: "Hello, my name is John"
输出: 5

"""

"""
时间复杂度 O(n),空间复杂度 O(n) （split 返回list）
"""
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

"""
更好的解决办法：
segment 片段统计 时间复杂度 O(n),空间复杂度 O(1) 
"""
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segment_count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1]== ' ') and s[i] !=" ":
                segment_count += 1
        return segment_count

"""
和前一个方法思想一样
"""
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre = " "
        count = 0
        for i in s:
            if i != ' ' and pre == " ":
                count += 1
            pre = i
        return count