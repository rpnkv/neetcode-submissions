class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        mask = 0b01

        carry = place = 0

        while a or b or carry:
            a_bit = a & mask
            b_bit = b & mask

            if a_bit & b_bit & carry:
                carry = 0b01
                res_mask = 0b01
            elif a_bit & b_bit:
                carry = 0b01
                res_mask = 0b00
            elif (a_bit | b_bit) & carry:
                carry = 0b01
                res_mask = 0b00
            elif a | b_bit | carry:
                carry = 0b00
                res_mask = 0b01
            else:
                carry = 0b00
                res_mask = 0b00

            res_mask <<= place

            res |= res_mask

            a >>= 1
            b >>= 1
            place += 1

        return res