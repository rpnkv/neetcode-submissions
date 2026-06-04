class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                operand = []
                while stack[-1] != '[':
                    operand.append(stack.pop())
                
                stack.pop()

                multiplier = []
                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())
                
                operand.reverse()
                multiplier.reverse()

                if len(multiplier) == 0:
                    multiplier = 1
                else:
                    multiplier = int("".join(multiplier))
                
                product = operand * multiplier
                stack += product
        
        return "".join(stack)