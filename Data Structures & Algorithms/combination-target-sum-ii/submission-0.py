class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, currsum, path):

            if currsum == target:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if currsum + candidates[i] > target:
                    break
                
                path.append(candidates[i])

                backtrack(i+1, currsum + candidates[i], path)

                path.pop()

        backtrack(0,0,[])

        return result