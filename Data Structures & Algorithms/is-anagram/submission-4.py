class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = Counter(s)

        for c in t:
            if c in cnt and cnt[c] > 0:
                cnt[c] -= 1
            else:
                return False
        
        return True
        