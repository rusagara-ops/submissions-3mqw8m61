class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for (source, target, time) in times:
            graph[source].append((target, time))

        visited = set()
        minheap = [(0,k)]
        shortestdistance = {k:0}

        while minheap:
            currenttime, currentnode = heapq.heappop(minheap)

            if currentnode in visited:
                continue
            visited.add(currentnode)

            for neighbour, time in graph[currentnode]:
                newtime = time + currenttime
                if neighbour not in shortestdistance or newtime < shortestdistance[neighbour]:
                    shortestdistance[neighbour] = newtime
                    heapq.heappush(minheap, (newtime, neighbour))

        if len(shortestdistance) != n:
            return -1
        return max(shortestdistance.values())
 

                
