class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m,n

        prev = [1] * cols

        for _ in range(rows - 1):
            curr = [1]
            for i in range(1, cols):
                curr.append(curr[i-1] + prev[i])
            
            prev = curr
        
        return prev[-1]

    

        
