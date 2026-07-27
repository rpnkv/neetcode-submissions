class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parents = [root] if root else []
        res = []

        while parents:
            children = []
            values = []

            for parent in parents:
                values.append(parent.val)
                children += (child for child in [parent.left, parent.right] if child)
                #children += [child for child in [parent.left, parent.right] if child]

            res.append(values)
            parents = children
        
        return res
