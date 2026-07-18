class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        c = Counter(s)

        for char in t:
            if not char in c:
                return False
            else:
                if c[char] == 1:
                    del c[char]
                else:
                    c[char] -= 1
        
        return len(c) == 0