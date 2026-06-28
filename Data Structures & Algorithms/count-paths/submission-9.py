class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = cols, n = rows

        prev = [1] * m

        for _ in range(1, n):
            curr = [1]
            for j in range(1, m):
                curr.append(curr[j - 1] + prev[j])
            
            prev = curr

        return prev[-1]
    

        
