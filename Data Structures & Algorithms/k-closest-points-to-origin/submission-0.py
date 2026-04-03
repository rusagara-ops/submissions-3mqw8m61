import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tuples = []

        for point in points:
            dist = (point[0])**2 + (point[1])**2
            tuples.append((dist, point))
        
        heapq.heapify(tuples)
        result = []

        for _ in range(k):
            dist,point = heapq.heappop(tuples)
            result.append(point)

        return result


