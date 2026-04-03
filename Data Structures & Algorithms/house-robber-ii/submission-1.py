class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def robthese(houses):

            if len(houses) == 1:
                return houses[0]
            if len(houses) == 2:
                return max(houses[0], houses[1])


            dp = [0] * len(houses)

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):

                dp[i] = max(dp[i-1], dp[i-2]+houses[i])
            return dp[-1]

        return max(robthese(nums[:-1]), robthese(nums[1:]))
                

        