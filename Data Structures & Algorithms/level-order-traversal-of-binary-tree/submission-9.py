class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        d = collections.deque()

        d.append(root)

        while d:
            lvl_nodes_cnt = len(d)
            lvl_nodes = []

            for _ in range(lvl_nodes_cnt):
                node = d.popleft()
                if node:
                    lvl_nodes.append(node.val)
                    d.append(node.left)
                    d.append(node.right)
                
            if lvl_nodes:
                res.append(lvl_nodes)

        return res

        
