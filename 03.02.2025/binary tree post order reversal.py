# Definition for a binary tree node.
# class TreeNode(object):
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if root is None:
            return []


        result = []
        def dfs(node):
            
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result
