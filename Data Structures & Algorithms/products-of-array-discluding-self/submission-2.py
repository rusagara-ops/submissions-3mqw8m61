class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        results = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            results[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums)-1, -1,-1):
            results[i] *= right
            right *= nums[i]
        
        return results
