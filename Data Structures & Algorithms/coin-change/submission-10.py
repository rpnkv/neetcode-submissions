class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        options = {0:0}

        for a in range(1, amount + 1):
            for c in coins:
                if c > a:
                    continue
                
                target = a - c

                if target in options:
                    options[a] = min(
                        options[target] + 1,
                        options.get(a, math.inf)
                    )
        
        return options.get(amount, -1)