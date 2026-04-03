class Solution:
    def rob(self, nums: List[int]) -> int:
        # since here they are asking for the max maount, we are going to use the max

        if len(nums) <= 2:
            return max(nums)
        # initialize our table
        dp = [0] * (len(nums))

        # basecases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for money in range(2, len(nums)):
            dp[money] += max(dp[money-1], dp[money-2]+nums[money])

        return dp[len(nums)-1]
