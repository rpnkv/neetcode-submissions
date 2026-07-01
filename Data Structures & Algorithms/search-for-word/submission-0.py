class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols, rows = len(board), len(board[0])


        def dfs(col:int, row:int, i) -> bool:
            if i == len(word):
                return True

            if c < 0 or c == cols or r < 0 or r == rows or board[col][row] != word[i] :
                return False

            board[col][row] = "*"
            res = (
                    dfs(col + 1, row, i + 1) or
                    dfs(col - 1, row, i + 1) or
                    dfs(col, row + 1, i + 1) or
                    dfs(col, row - 1, i + 1)
            )

            board[col][row] = word[i]
            return res



        for c in range(cols):
            for r in range(rows):
                if dfs(c, r, 0):
                    return True

        return False