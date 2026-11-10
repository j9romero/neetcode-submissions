# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currentMax):
            if not node:
                return 0
            
            good = 1 if node.val >= currentMax else 0 
            newMax = max(currentMax, node.val)

            return good + dfs(node.left, newMax) + dfs(node.right, newMax)
        return dfs(root, root.val)
        