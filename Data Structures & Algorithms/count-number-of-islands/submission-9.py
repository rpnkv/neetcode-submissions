class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols, rows = len(grid), len(grid[0])
        num = 0

        def dfs(col: int, row: int) -> None:
            if col < 0 or col == cols or row < 0 or row == rows:
                return 

            if grid[col][row] != "1":
                return
            
            grid[col][row] = "0"

            dfs(col + 1, row)
            dfs(col - 1, row)
            dfs(col, row + 1)
            dfs(col, row - 1)
        
        for c in range(cols):
            for r in range(rows):
                if grid[c][r] == "1":
                    num += 1
                    dfs(c,r)
        
        return num
            
