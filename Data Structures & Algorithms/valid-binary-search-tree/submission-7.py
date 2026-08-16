# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, floor, ceil) -> bool:
            if not root:
                return True

            if root.val <= floor or root.val >= ceil:
                return False
            
            return (
                validate(root.left, floor = floor, ceil = root.val) and
                validate(root.right, floor = root.val, ceil = ceil)
            )

        return validate(root, -math.inf, math.inf)