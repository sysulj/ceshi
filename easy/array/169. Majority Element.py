"""
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = list(set(nums))
        for i in tmp:
            if nums.count(i) > len(nums)/2:
                return i


""""
排序
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums)/2)]

"""
使用Counter类 统计  HashMap
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]


"""
（多数投票算法）
Boyer-Moore majority vote algorithm(摩尔投票算法) 
数组中从candidate被赋值到count减到0的那一段可以被去除，余下部分的多数元素依然是原数组的多数元素。
该算法时间复杂度为o(n)，空间复杂度为o(1)

Boyer-Moore另一个优点就是可以使用并行算法实现。 其基本思想为对原数组采用分治的方法。
    若要从一个非常大的数组中寻找多数元素，数据量非常大，那么我们可以用MapReduce的方式来解决这个问题
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate