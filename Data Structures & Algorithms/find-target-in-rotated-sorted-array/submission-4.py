class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
            pivot = l
            
        def binarysearch(left,right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid -1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    return mid
            return -1

        result = binarysearch(0, l-1)
        if result != -1:
            return result

        return binarysearch(l, len(nums)-1)
