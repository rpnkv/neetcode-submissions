# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_valid = not root.left or (root.val > root.left.val and self.isValidBST(root.left))
        right_valid = not root.right or(root.val < root.right.val and self.isValidBST(root.right))

        return left_valid and right_valid


