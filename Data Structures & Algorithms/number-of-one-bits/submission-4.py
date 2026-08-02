class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt, mask = 0, 0b01

        for _ in range(32):
            cnt += int(n & mask)

            n >>= 1
        
        return cnt
