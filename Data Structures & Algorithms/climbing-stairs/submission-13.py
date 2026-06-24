class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        else:
            return 1 + self.climbStairs(n - 1)

        