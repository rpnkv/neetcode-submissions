class Solution:
    def climbStairs(self, n: int) -> int:
        prev = [0, 1]

        for _ in range(n):
            prev[0], prev[1] = prev[1], (prev[0] + prev[1])


        return prev[1]