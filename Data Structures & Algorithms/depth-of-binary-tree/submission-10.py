class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        d = deque()

        if not root:
            return 0
        else:
            d.append(root)

        depth = 0
        while d:
            depth += 1
            for _ in range(len(d)):
                node = d.pop()
                if node.left:
                    d.appendleft(node.left)
                
                if node.right:
                    d.appendleft(node.right)
            
        
        return depth