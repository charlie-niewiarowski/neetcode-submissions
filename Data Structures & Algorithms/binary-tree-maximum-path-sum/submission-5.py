# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')

        def dfs(root):
            nonlocal maxPath
            if not root:
                return 0

            # Recurse down and clamp negatives to 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # Calculate path sum through this node
            current = root.val + left + right
            maxPath = max(maxPath, current)

            # Return best single-branch path to parent
            return root.val + max(left, right)
        
        dfs(root)
        return maxPath

