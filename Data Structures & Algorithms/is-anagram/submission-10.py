class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)

        return c1 == c2

        