class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest, cnt = 0, 0, {}

        for r, char in enumerate(s):
            cnt[char] = cnt.get(char, 0) + 1

            freq_cnt = max(cnt.vals())
            while (r - l + 1) - freq_cnt > k:
                cnt[s[l]] -= 1
                l+=1
                freq_cnt = max(cnt.vals())
            
            longest = max(longest, r - l + 1)
        
        return longest