# Definition for a binary tree node.
# class TreeNode(object):
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        l=[]
        def inorder(root):
            if root == None:
                return 
            
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)

        return l
