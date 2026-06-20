class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        
        return 1 + self.climbStairs(n - 1)