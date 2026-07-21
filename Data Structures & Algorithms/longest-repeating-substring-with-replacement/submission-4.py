class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len, counts = 0, 0, {}

        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            
            freq_cnt = max(counts.values())
            while (r - l + 1) - freq_cnt > k:
                counts[s[l]] -= 1
                l+=1

                freq_cnt = max(counts.values())
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
