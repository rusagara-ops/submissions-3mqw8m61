class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = set(nums)
        if len(nums) != len(lst):
            return True
        return False