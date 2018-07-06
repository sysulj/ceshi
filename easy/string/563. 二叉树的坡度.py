"""
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

示例:

输入:
         1
       /   \
      2     3
输出: 1
解释:
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
注意:

任何子树的结点的和不会超过32位整数的范围。
坡度的值不会超过32位整数的范围。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumTilt(root)[0]

    def sumTilt(self, root):
        """

        """
        if root:
            lt, ls = self.sumTilt(root.left)
            rt, rs = self.sumTilt(root.right)
            return abs(ls - rs) + lt + rt, ls + rs + root.val
        else:
            return 0, 0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def _sum_tilt(root):
            if not root:
                return 0
            else:
                left = _sum_tilt(root.left)
                right = _sum_tilt(root.right)
                self.ans += abs(left - right)
                return root.val + left + right
        _sum_tilt(root)
        return self.ans