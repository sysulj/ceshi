"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
示例 2:
输入: "aba"
输出: False
示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

"""

"""

"""
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, int(len(s)/2) +1):
            if len(s) % i == 0 and int(len(s)/i)*s[:i] == s:
                return True
        return False

class Solution01:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return  False
        ss = (s+s)[1:-1]
        return ss.find(s) != -1  # -1 为找不到


if __name__ == '__main__':
    pass
    s = Solution01()
    str = "abcacabc"
    print(s.repeatedSubstringPattern(str))