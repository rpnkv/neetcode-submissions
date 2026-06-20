class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                multiplying = []
                while stack and stack[-1] != '[':
                    multiplying.append(stack.pop())
                stack.pop()
                
                multiplying.reverse()

                multiplier = []
                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())

                multiplier = int("".join(reversed(multiplier)))

                stack += multiplying * multiplier
        
        return "".join(stack)