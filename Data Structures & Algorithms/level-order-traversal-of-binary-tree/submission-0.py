# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = []

        curr = [root]

        while any(map(lambda x: x is not None, curr)):
            curr_vals = []
            curr_children = []
            for node in curr:
                    if node:
                        curr_vals.append(node.val)
                        curr_children += [node.left, node.right]

            curr = curr_children
            lvls.append(curr_vals)

        return lvls