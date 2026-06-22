N = M = N_DIGITS = 9
N_QUADRANTS = (N // 3) * (M // 3)


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [[False] * N_DIGITS for _ in range(N)]
        column = [[False] * N_DIGITS for _ in range(M)]
        quadrant = [[False] * N_DIGITS for _ in range(N_QUADRANTS)]

        for i in range(N):
            for j in range(M):
                if (char := board[i][j]) == ".":
                    continue

                num = int(char) - 1
                q = (i // 3) * 3 + (j // 3)

                if row[i][num] or column[j][num] or quadrant[q][num]:
                    return False

                row[i][num] = column[j][num] = quadrant[q][num] = True

        return True
