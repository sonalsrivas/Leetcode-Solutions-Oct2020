class Solution:   
    def divisorGame(self, n: int) -> bool:
        # Dynamic Programming
        dp=[False]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                if i%j==0 and dp[i-j]==False:
                    dp[i]=True
        return dp[n]
