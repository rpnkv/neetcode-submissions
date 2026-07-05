class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands, rows, cols = 0, len(grid), len(grid[0])

        def dfs(row:int, col:int)->None:
            if (
                row < 0 or row == rows or
                col < 0 or col == cols
            ): 
                return 
            
            if grid[row][col] == '0':
                return

            grid[row][col] = '0'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)

        return islands