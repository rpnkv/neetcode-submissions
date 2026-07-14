class Counter:
    def __init__(self):
        self.d = {}
        self.total_chars = 0
        
    def add(self, char: s) -> None:
        if not char in self.d:
            self.d[char] = 0

        self.d[char] += 1
        self.total_chars += 1
    
    def delete(self, char: s) -> None:
        if self.d[char] == 1:
            del self.d[char]
        else:
            self.d[char] -= 1
        self.total_chars -= 1

    def non_freq_count(self) -> int:
        freq_count = max(self.d.values())
        return self.total_chars - freq_count

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()
        l, max_len = 0, 0

        for r,char in enumerate(s):
            c.add(char)

            while c.non_freq_count() > k:
                c.delete(s[l])
                l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len

            
