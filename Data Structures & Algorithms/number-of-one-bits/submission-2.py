class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 0b1

        for _ in range(32):
            if mask & n:
                count+=1
            
            n= n >> 1
        
        return count