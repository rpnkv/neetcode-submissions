class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * m

        for _ in range(1, n):
            curr = [1]
            
            for m_prev in prev[1:]:
                curr.append(curr[-1] + m_prev)
            
            prev = curr

        
        return prev.pop()