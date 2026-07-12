class Solution:
    def isValid(self, s: str) -> bool:
        d = {'[':']', '(':')', '{':'}'}
        stack = []

        for char in s:
            if char in d:
                stack.append(char)
            else:
                pair = stack.pop()
                if not char == d[pair]:
                    return False
        
        return True
