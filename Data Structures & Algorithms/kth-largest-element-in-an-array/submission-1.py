import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(-num)

        heapq.heapify(heap)

        result = []

        for _ in range(k):
            result.append(-(heapq.heappop(heap)))
        
        return result[-1]

