class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        d = deque()

        if root:
            d.append(root)

        depth = 0
        while d:
            depth += 1
            for _ in range(len(d)):
                if d[-1].left:
                    d.appendleft(d[-1].left)
                
                if d[-1].right:
                    d.appendleft(d[-1].right)
                d.pop()
        
        return depth