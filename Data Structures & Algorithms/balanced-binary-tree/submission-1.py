# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs_height(root):
            if not root:
                return True
            right = dfs_height(root.right)
            left = dfs_height(root.left)

            if right == -1 or left == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return dfs_height(root) != -1
        

        