class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
                continue

            operand = []
            while stack and stack[-1].isalpha():
                operand.append(stack.pop())
            stack.pop()

            multiplier_str = []
            while stack and stack[-1].isdigit():
                multiplier_str.append(stack.pop())

            multiplier = int("".join(reversed(multiplier_str)))

            stack += reversed(operand * multiplier)
        
        return "".join(stack)
