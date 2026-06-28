class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        # if we can't get the stair directly -- sum the ways to get stairs we cant step into target from

        a, b = 1, 2

        for _ in range(n - 2):
            a, b = b, a + b

        return b