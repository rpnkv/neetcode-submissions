class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parents = [root]
        res = []

        while all(parents):
            parent_values = []
            children = []

            for parent in parents:
                parent_values.append(parent.val)

                children += [parent.left, parent.right]

            res.append(parent_values)
            parents = children
        
        return res