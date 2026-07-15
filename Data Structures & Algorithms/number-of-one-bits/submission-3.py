class Solution:
    def hammingWeight(self, n: int) -> int:
        c, mask = 0, 0b01

        for _ in range(32):
            c += n & mask
            n >>= 1
        
        return c