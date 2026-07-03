class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = {}

        for s_char in s:
            if s_char not in s_counts:
                s_counts[s_char] = 1
            else:
                s_counts[s_char] += 1
        
        for t_char in t:
            if t_char in s_counts and s_counts[t_char] > 0:
                s_counts[t_char] -= 1
            else:
                return False


        return True