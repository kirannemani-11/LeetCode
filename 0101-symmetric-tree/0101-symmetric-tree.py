# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Mirror(n1,n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2 or n1.val != n2.val:
                return False
            return Mirror(n1.left, n2.right) and Mirror(n1.right, n2.left)
        return Mirror(root, root)