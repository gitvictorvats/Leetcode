from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        N = len(coins)
        
        # if N == 0:
        #     return 0 if amount > 0 else 1
        
        dp = [[0 for _ in range(amount + 1)] for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        def changeHelper(amount, coins, N):
            
            for i in range(1, N + 1):
                for j in range(1, amount + 1):
                    if coins[i - 1] <= j:
                        dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]

            return dp[N][amount]
        
        return changeHelper(amount, coins, N)
