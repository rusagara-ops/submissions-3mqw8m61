class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, currsum, currpath):

            if currsum == target:
                result.append(currpath[:])

            if currsum > target:
                return

            for i in range(start, len(nums)):
                number = nums[i]
                currpath.append(number)
                backtrack(i, currsum + number, currpath)

                currpath.pop()
        
        backtrack(0,0,[])
        return result