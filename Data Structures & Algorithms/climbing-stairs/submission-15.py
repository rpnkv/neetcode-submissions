class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2] + [None] * (n - 2)
        
        def dfs(n : int) -> int:
            if not dp[n]:
                dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            
            return dp[n]

        return dfs(n)