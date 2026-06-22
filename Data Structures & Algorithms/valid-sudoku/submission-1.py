N = M = 9


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows: defaultdict[int, set[str]] = defaultdict(set)
        columns: defaultdict[int, set[str]] = defaultdict(set)
        squares: defaultdict[tuple[int, int], set[str]] = defaultdict(set)

        for i in range(N):
            for j in range(M):
                if (val := board[i][j]) == ".":
                    continue

                square = (i // 3, j // 3)

                if val in rows[i] or val in columns[j] or val in squares[square]:
                    return False

                rows[i].add(val)
                columns[j].add(val)
                squares[square].add(val)

        return True
