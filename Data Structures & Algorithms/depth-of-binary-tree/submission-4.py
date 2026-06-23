# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        parents = [root] if root else []

        depth = 0

        while parents:
            depth += 1
            children = []

            for parent in parents:
                children += [child for child in [parent.left, parent.right] if child]

            parents = children
            

        return depth