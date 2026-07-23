class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(row: int, col: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if row < 0 or row == rows or col < 0 or col == cols:
                return False
            
            if board[row][col] != word[i]:
                return False

            board[row][col] = "*"

            res = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
            )

            board[row][col] = word[i]
            return res

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False