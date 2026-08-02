class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char not in pars:
                stack.append(char)
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if pair != pars[char]:
                    return False
        
        return len(stack) == 0
