*# Definition for a binary tree node.
# class TreeNode(object):
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        elif p==None or q==None or p.val!=q.val:
            return False
        return  self.isSameTree(p.left,q.left)  and self.isSameTree(p.right,q.right)
