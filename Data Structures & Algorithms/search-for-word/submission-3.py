class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(row: int, col: int, i: int = 0) -> bool:
            if i == len(word):
                return True

            if (
                (row < 0 or row == rows) or
                (col < 0 or col == cols)
            ):
                return False
            
            if word[i] != board[row][col]:
                return False
            
            board[row][col] = "*"
            res = (
                dfs(row - 1, col, i + 1) or
                dfs(row + 1, col, i + 1) or
                dfs(row, col - 1, i + 1) or
                dfs(row, col + 1, i + 1)
            )
            if res:
                return True
            else:
                board[row][col] = word[i]
                return False

        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col):
                    return True
                

        return False