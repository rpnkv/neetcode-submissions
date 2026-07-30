class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len, most_freq_cnt, cnt = 0, 0, 0, {}

        for r, char in enumerate(s):
            cnt[char] = cnt.get(char, 0) + 1

            most_freq_cnt = max(cnt.values())
            if (r - l + 1) - most_freq_cnt > k:
                if cnt[s[l]] == 1:
                    del cnt[s[l]]
                else:
                    cnt[s[l]] -= 1
                l+=1
            
            max_len = max(r - l + 1, max_len)

        return max_len