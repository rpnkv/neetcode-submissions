class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = 0

        def dfs(row: int, col:int):
            if row < 0 or row >= rows:
                return

            if col < 0 or col >= cols:
                return

            if grid[row][col] == '1':
                grid[row][col] = '0'
                dfs(row - 1, col)
                dfs(row + 1, col)
                dfs(row, col - 1)
                dfs(row, col + 1)
        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1

        return islands 