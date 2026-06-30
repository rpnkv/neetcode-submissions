class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b, c, d = [0] * 4

        for n in nums:
            a, b, c, d = b, c, d, n + max(b, c)

        return max(c,d)