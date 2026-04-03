class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()

            curr = stones.pop() - stones.pop()

            stones.append(curr)

        if stones:
            return stones[0]
        else:
            return 0
        
# [2,3,6,2,4]
# [2,2,3,2]

# curr = 2