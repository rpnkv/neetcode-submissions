class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                operand = []
                while stack[-1].isalpha():
                    operand.append(stack.pop())
                stack.pop()

                operand.reverse()

                multiplier = []
                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())
                
                multiplier.reverse()
                multiplier = int("".join(multiplier))

                stack += operand * multiplier
            
        return "".join(stack)                