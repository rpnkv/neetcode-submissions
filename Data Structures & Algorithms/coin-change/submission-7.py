from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        
        # Базовый случай: для суммы 0 нужно 0 монет
        dp[0] = 0
        
        # Перебираем все суммы от 1 до amount
        for i in range(1, amount + 1):
            # Проверяем каждую монету
            for coin in coins:
                if i - coin >= 0:
                    # Ищем минимум среди всех возможных монет
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Если значение не изменилось, значит собрать сумму невозможно
        return dp[amount] if dp[amount] != amount + 1 else -1
