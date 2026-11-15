class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        results, sol = [], []
        s1, s2 = len(board), len(board[0])
        visited = [[False for _ in range(s2)] for _ in range(s1)]

        def b(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or r >= s1 
                or c < 0 or c >= s2  
                or word[i] != board[r][c]
                or visited[r][c]
            ):
                return False

            visited[r][c] = True
            res = (b(r+1, c, i+1) or 
                    b(r-1, c, i+1) or 
                    b(r, c+1, i+1) or 
                    b(r, c-1, i+1))
            visited[r][c] = False
            return res

        for r in range(s1):
            for c in range(s2):
                if b(r, c, 0):
                    return True
        return False