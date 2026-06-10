class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parents = [root] if root else []
        res = []

        while parents:
            parent_values = []
            children = []

            for parent in parents:
                parent_values.append(parent.val)

                children += [parent.left, parent.right]

            res.append(parent_values)
            parents = [child for child in children if child is not None]
        
        return res