class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, cur):
            if cur == len(word):
                return True
            if c >= len(board[0]) or r >= len(board) or c < 0 or r < 0 or word[cur] != board[r][c] or board[r][c] == '#':
                return False
            board[r][c] = '#'
            res = (dfs(r + 1, c, cur + 1) or
                    dfs(r, c + 1, cur + 1) or
                    dfs(r - 1 , c, cur + 1) or
                    dfs(r, c - 1, cur + 1))
            board[r][c] = word[cur]
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
