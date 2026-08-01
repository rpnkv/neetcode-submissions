class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0b01
        res = carry = 0

        for pos in range(32):
            a_bit = a & mask
            b_bit = b & mask

            res_bit = a_bit ^ b_bit ^ carry 
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)

            res |= res_bit << pos

            a >>= 1
            b >>= 1
        
        if res & 0x80000000:
            res -= 0x100000000 
        
        return res
