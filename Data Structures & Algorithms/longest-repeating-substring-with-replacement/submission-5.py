class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest, cnt = 0, 0, {}

        for r, char in enumerate(s):
            cnt[char] = cnt.get(char, 0) + 1

            freq = max(cnt.values())
            while (r - l + 1) - freq > k:
                if cnt[s[l]] == 1:
                    del cnt[s[l]]
                else:
                    cnt[s[l]] -= 1
                l+=1

                freq = max(cnt.values())
            
            longest = max(longest, r - l + 1)
        
        return longest