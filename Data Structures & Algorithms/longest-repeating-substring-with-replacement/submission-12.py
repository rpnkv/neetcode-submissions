class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len, counts = 0, 1, {}

        for r, char in enumerate(s):
            counts[char] = 1 + counts.get(char, 0)

            freq = max(counts.values())
            if r - l + 1 - freq > k:
                removing_char = s[l]
                if counts[removing_char] == 1:
                    del counts[removing_char]
                else:
                    counts[removing_char] -= 1
                l+=1
            
            max_len = max(max_len, r - l + 1)

        return max_len