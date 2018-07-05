"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

 示例 2:
输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

"""

"""
！！！
"""
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s == "":
            return []
        output = []
        correctdict = dict()
        tempdict = dict()
        for i in s+p:
            if i not in tempdict:
                correctdict[i] = 0
                tempdict[i] = 0
        for i in p:
            correctdict[i] += 1
        for i in s[0:len(p)]:
            tempdict[i] += 1
        if tempdict == correctdict:
            output.append(0)
        for i in range(len(s) -len(p)):
            tempdict[s[i]] -= 1
            tempdict[s[i+len(p)]] += 1
            if tempdict == correctdict:
                output.append(i +1 )
        return output

"""
使用 counter类计数
"""
class Solution02:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        res =[]
        counter_p = Counter(p)
        counter_s = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            counter_s[s[i]] += 1
            if counter_s == counter_p:
                res.append(i-len(p)+1)
            counter_s[s[i-len(p)+1]] -= 1
            if counter_s[s[i-len(p)+1]] == 0:
                del counter_s[s[i-len(p)+1]]
        return res

if __name__ == '__main__':
    S= Solution02()
    s = "cabab"
    p ="ab"
    out = S.findAnagrams(s,p)
    print(out)