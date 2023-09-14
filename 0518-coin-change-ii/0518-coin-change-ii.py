
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def chnageHelper(amount,coins,N,memo):

            

            # base condition

            if amount==0 :
                return 1
            
            if N==0 :
                return 0

            if memo[N][amount]!=-1:

                return memo[N][amount]
            
            # include case

            if (coins[N-1]<=amount):

                include= chnageHelper(amount-coins[N-1],coins,N,memo)
                exclude= chnageHelper(amount,coins,N-1,memo)

                memo[N][amount]=include + exclude
                return memo[N][amount]


            else:
                exclude= chnageHelper(amount,coins,N-1,memo)
                memo[N][amount]=exclude
                return memo[N][amount]
        
        
        N=len(coins)
        memo=[[-1 for _ in range(amount+1)] for _ in range(N+1)]
        return chnageHelper(amount,coins,N,memo)


            
