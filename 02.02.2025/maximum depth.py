# Definition for a binary tree node.
# class TreeNode(object):
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        leftheight=self.maxDepth(root.left)
        rightheight=self.maxDepth(root.right)
        return 1+max(leftheight,rightheight)    


        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
