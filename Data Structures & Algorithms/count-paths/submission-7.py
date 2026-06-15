class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * m

        for _ in range(1, n):
            curr = [prev[0]]
            for j in range(1,m):
                curr.append(prev[j] + curr[j - 1])

            prev = curr

        return prev[-1]
                
    

        
