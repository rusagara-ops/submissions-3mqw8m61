class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(row,col):
            if 0 <= row < rows and 0 <= col < cols:

                if grid[row][col] != "1":
                    return
                
                grid[row][col] = "0"

                for dr,dc in ((0,1), (1,0),(-1,0), (0,-1)):
                    nr = dr + row
                    nc = dc + col
                    dfs(nr,nc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row,col)

        return count