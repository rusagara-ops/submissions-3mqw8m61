class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        minutes = 0
        fresh = 0

        def rot(r,c):
            if (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                grid[r][c] = 2
                queue.append((r,c))
                return 1
            return 0
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                fresh -= rot(r+1,c)
                fresh -= rot(r-1,c)
                fresh -= rot(r,c+1)
                fresh -= rot(r,c-1)
            minutes += 1

        if fresh == 0:
            return minutes
        return -1

            



