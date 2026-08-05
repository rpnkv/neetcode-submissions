class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win, l, max_len = set(), 0, 0 

        for r, char in enumerate(s):
            while char in win:
                win.remove(s[l])
                l += 1
            win.add(char)

            max_len = max(max_len, len(win))
        
        return max_len

            

