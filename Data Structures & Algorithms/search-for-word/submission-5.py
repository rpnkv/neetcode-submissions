class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols, rows, letters = len(board), len(board[0]), len(word)

        def matrix_dfs(col: int, row:int, pos: int) -> None:
            if pos == letters:
                return True

            if col < 0 or col == cols or row < 0 or row == rows:
                return
            
            if board[col][row] != word[pos]:
                return
            
            board[col][row] = '*'
            res = (
                matrix_dfs(col + 1, row, pos + 1) or
                matrix_dfs(col - 1, row, pos + 1) or

                matrix_dfs(col, row + 1, pos + 1) or
                matrix_dfs(col, row - 1, pos + 1)
            )

            board[col][row] = word[pos]
            return res

        for c in range(cols):
            for r in range(rows):
                if matrix_dfs(c, r, 0):
                    return True
        
        return False
            
