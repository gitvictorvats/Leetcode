class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m= len(text1)
        n=len(text2)

        memo=[[-1 for _ in range(m+1)] for _ in range(n+1)]

        def lcsHelper(text1,text2,m,n,memo):

            if m==0 or n==0 :
                return 0
            
            if memo[n][m]!=-1:
                return memo[n][m]

            if(text1[m-1]==text2[n-1]):

                memo[n][m]=1+ lcsHelper(text1,text2,m-1,n-1,memo)
                return memo[n][m]
            
            else:

                memo[n][m]=max(lcsHelper(text1,text2,m-1,n,memo),lcsHelper(text1,text2,m,n-1,memo))
                return memo[n][m]
        
        return lcsHelper(text1,text2,m,n,memo)
                
                
        