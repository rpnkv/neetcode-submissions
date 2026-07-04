class Solution:
    def isValid(self, s: str) -> bool:
        left = {'{':'}', '(':')', '[':']'}
        right = {v:k for k, v in left.items()}

        stack = []

        for c in s:
            if c in left:
                stack.append(c)
            else:
                if stack[-1] != right[c]:
                    return False
                
                stack.pop()

        return True