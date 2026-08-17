class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(row, col, k):            
            if (row < 0 or row >= len(board) or
            col < 0 or col >= len(board[0]) or
            board[row][col] != word[k] or
            visited[row][col]):
                return False
            
            if k == len(word) - 1 and board[row][col] == word[k]:
                return True
            
            visited[row][col] = True

            res = (dfs(row + 1, col, k + 1) or
                  dfs(row - 1, col, k + 1) or
                  dfs(row, col + 1, k + 1) or
                  dfs(row, col - 1, k + 1))
            
            visited[row][col] = False
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False
        