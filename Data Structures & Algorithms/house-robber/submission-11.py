class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = c = d = 0

        for n in nums:
            a, b, c, d = b, c, d, max(b,c) + n

        return max(c,d)
