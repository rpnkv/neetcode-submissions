class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                operand = []
                while stack and stack[-1].isalpha():
                    operand.append(stack.pop())
                stack.pop() #remove opening bracket

                multiplier = []
                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())

                multiplier = int("".join(reversed(multiplier)))
                operand.reverse()

                stack.extend(operand * multiplier)
            else:
                stack.append(char)
            
        return "".join(stack)