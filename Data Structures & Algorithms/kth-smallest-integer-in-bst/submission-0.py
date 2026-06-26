# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        def dfs(root):
            nonlocal i
            if not root:
                return 
            
            x = dfs(root.left)
            if x:
                return x

            i += 1

            if (i == k):
                return root.val

            y = dfs(root.right)
            if y:
                return y
        
        return dfs(root)
            