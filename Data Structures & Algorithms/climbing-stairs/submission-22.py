class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1:1, 2:2}
        
        def dfs(n: int) -> int:
            if n not in dp:
                dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

            return dp[n]
        
        return dfs(n)

        
        