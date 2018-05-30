"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any nleading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == num2 == "0":
            return "0"
        l1,l2 = len(num1),len(num2)
        min_l = min(l1, l2)
        s =''
        more = 0
        for i in range(1,min_l +1):
            tmp = ord(num1[-i])- ord('0') + ord(num2[-i])- ord('0') + more
            more = tmp//10
            s = chr(tmp%10 +ord('0'))+s
        for i in range(min_l+1, l1+1):
            tmp = ord(num1[-i])-ord('0')+more
            more = tmp//10
            s = chr(tmp%10 +ord('0'))+s
        for i in range(min_l+1, l2+1):
            tmp = ord(num2[-i])-ord('0')+more
            more = tmp//10
            s = chr(tmp%10 +ord('0'))+s
        s = chr(more+ord('0'))+s
        return s.lstrip('0')