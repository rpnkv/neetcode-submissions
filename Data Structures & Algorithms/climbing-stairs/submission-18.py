class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 0

        for _ in range(n):
            a, b = b, 1 + b

        return b