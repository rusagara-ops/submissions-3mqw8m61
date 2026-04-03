class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numset = set(nums)
        longest = 0
        length = 0

        for i in range(n):
            if (nums[i] - 1) not in numset:
                length = 1
                while (nums[i] + length) in numset:
                    length += 1
                longest = max(longest, length)

        return longest

        