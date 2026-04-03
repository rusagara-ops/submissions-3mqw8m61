class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxwater = 0

        while left < right:
            if heights[left] > heights[right]:
                area = (right-left) * heights[right]
                right -= 1
            else:
                area = (right-left) * heights[left]
                left += 1

            maxwater = max(maxwater, area)

        return maxwater
