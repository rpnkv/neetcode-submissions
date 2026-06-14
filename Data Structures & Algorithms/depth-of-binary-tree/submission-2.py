# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr_depth = 0
        parents = [root] if root else []

        while parents:
            curr_depth += 1
            next_level = [child for parent in parents for child in [parent.left, parent.right] if child]
            parents = next_level

        
        return curr_depth