"""
219. Contains Duplicate II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: [1,2,3,1], k = 3
输出: true
示例 2:

输入: [1,0,1,1], k = 1
输出: true
示例 3:

输入: [1,2,1], k = 0
输出: false

"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, num in enumerate(nums):
            if num in d and (i - d[num] <=k):
                return True
            d[num] = i
        return False


"""

"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        n = 0
        for num in nums:
            if num in d and (n -d[num] <= k):
                return True
            d[num] = n
            n += 1
        return False