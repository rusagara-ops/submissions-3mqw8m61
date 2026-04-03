class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()

            curr = stones.pop() - stones.pop()

            if curr:
                stones.append(curr)

        if stones:
            return stones[0]
        else:
            return 0
        
