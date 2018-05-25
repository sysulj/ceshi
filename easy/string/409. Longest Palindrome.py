"""
409. Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""
import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for v in collections.Counter(s).values():
            ans += v//2 *2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

"""

"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 0
        ans = 0
        for e in set(s):
            temp = s.count(e)
            ans += temp // 2 * 2
            if not flag:
                flag = temp % 2
        return ans + flag


"""
 关注奇数字母。
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 统计奇数字母
        hs=set()
        for c in s:
            if c not in hs:
                hs.add(c)
            else:
                hs.remove(c)
        return len(s)-len(hs)+1 if len(hs) > 0 else len(s)