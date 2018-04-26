# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        dict = {}
        def _findTarget(root):
            if root is None:
                return False
            if (k - root.val) in dict:
                return True
            res = False
            dict[root.val] = True
            res = res or _findTarget(root.left)
            res = res or _findTarget(root.right)
        
            return res
        return _findTarget(root)
