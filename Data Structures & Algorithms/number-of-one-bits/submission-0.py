class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        mask = 1

        for _ in range(33):
            if n & mask:
                count+=1
            n = n >> 1
        
        return count