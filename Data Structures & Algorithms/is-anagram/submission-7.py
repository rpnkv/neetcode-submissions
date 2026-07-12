from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s)

        for char in t:
            if not char in s_c:
                return False
            else:
                if s_c[char] == 1:
                    del s_c[char]
                else:
                    s_c[char] -= 1
        
        return True