import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        while l <= r:
            k = (l + r)//2
            hrs = 0

            for p in piles:
                hrs += math.ceil(p / k)

            if hrs <= h:
                r = k - 1
                result = min(result, k)
            else:
                l = k + 1

        return result
