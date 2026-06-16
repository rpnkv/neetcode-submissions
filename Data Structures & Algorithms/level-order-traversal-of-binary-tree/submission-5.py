class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parents = [root] if root else []
        res = []

        while parents:
            # children = [child for parent in parents for child in [parent.left, parent.right] if child]
            children = []
            current = []
            for parent in parents:
                current.append(parent.val)
                children.extend([child for child in [parent.left, parent.right] if child])

            res.append(current)
            parents = children
        
        return res

