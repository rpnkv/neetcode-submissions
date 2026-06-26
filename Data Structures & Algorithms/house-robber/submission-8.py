class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b,c,d,e = 0,0,0,0,0

        for n in nums:
            a, b, c, d, e = b, c, d, e, n + max(b,c,d)

        return e