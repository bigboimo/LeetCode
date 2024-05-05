class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = defaultdict(list)
        hashRow = defaultdict(list)
        hashCol = defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]

                if val == ".":
                    continue

                if val in hashCol[col] or val in hashRow[row] or val in hashmap[row//3, col//3]:
                    print(hashmap)
                    print(hashCol)
                    print(hashRow)
                    return False

                hashCol[col].append(val)
                hashRow[row].append(val)
                hashmap[row//3, col//3].append(val)

        return True

