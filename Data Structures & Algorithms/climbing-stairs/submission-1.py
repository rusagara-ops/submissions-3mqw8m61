class Solution:
    def climbStairs(self, n: int) -> int:
        # first check if the number of stairs we have is less than the posisble number of steps we can take
        
        if n <= 2:
            return n
        # now initialize our table
        dp = [0] * (n+1)

        # now we do the base cases
        dp[0] = 1   
        dp[1] = 1
        dp[2] = 2

        for step in range(3, n+1):
            dp[step] = dp[step-1] + dp[step-2]

        return dp[n]
