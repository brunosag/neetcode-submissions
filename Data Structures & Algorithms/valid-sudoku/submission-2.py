SQUARE_SIZE = 3
BOARD_SIZE = 3
N = M = SQUARE_SIZE * BOARD_SIZE
N_SQUARES = BOARD_SIZE**2


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * N
        columns = [0] * M
        squares = [0] * N_SQUARES

        for i in range(N):
            for j in range(M):
                if (val := board[i][j]) == ".":
                    continue

                num = 1 << int(val) - 1
                square = (i // SQUARE_SIZE) * SQUARE_SIZE + (j // SQUARE_SIZE)

                if rows[i] & num or columns[j] & num or squares[square] & num:
                    return False

                rows[i] |= num
                columns[j] |= num
                squares[square] |= num

        return True
