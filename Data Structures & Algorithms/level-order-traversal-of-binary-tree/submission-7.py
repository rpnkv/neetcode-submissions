from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parents = [root] if root else []

        res = []

        while parents:
            children = []
            lvl_res = []
            
            for parent in parents:
                lvl_res.append(parent.val)
                children += [child for child in [parent.left, parent.right] if child]
            
            res.append(lvl_res)
            parents = children

        return res