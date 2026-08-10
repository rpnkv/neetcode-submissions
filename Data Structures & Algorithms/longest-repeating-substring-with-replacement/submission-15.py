class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win, l, max_len = {}, 0, 0

        for r, char in enumerate(s):
            win[char] = win.get(char, 0) + 1

            freq = max(win.values())
            if (r - l + 1) - freq > k:
                candidate = s[l]
                if win[candidate] == 1:
                    del win[candidate]
                else:
                    win[candidate] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len