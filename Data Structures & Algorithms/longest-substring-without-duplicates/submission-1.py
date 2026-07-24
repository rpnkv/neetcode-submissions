class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()

        l = max_len = 0

        for char in s:
            while char in c_set:
                c_set.remove(s[l])
                l += 1            

            c_set.add(char)
            max_len = max(max_len, len(c_set))
        
        return max_len
            
