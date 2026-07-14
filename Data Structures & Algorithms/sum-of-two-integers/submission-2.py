class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        mask = 0b01

        carry = 0

        for pos in range(33):
            a_bit = a & mask
            b_bit = b & mask

            if not (a | b | carry):
                break

            x = a_bit ^ b_bit ^ carry
            carry = (a_bit or b_bit) and (a_bit or carry)

            x <<= pos
            a >>= 1
            b >>= 1
            res |= x

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res