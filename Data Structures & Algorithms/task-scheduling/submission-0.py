class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0

        maxheap = []

        for cnt in count.values():
            maxheap.append(-cnt)

        heapq.heapify(maxheap)

        queue = deque()

        while maxheap or queue:
            time += 1

            if maxheap:
                executedtaskcount = 1 + heapq.heappop(maxheap)
                if executedtaskcount != 0:
                    queue.append([executedtaskcount, time + n])
            else:
                time = queue[0][1]

            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])

        return time


