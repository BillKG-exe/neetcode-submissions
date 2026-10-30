class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}

        for i in range(len(board)):
            s = set()
            t = set()

            for j in range(len(board)):
                if board[i][j] != ".":
                    box = (i // 3, j // 3)

                    if box not in boxes:
                        boxes[box] = set()

                    if board[i][j] in boxes[box]:
                        return False

                    boxes[box].add(board[i][j])

                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in t:
                        return False
                    else:
                        t.add(board[j][i])                    

        return True