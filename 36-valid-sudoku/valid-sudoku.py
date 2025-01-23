class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVals = defaultdict(list)
        colVals = defaultdict(list)
        boxVals = defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board[row])):
                #print(board[row][col])

                if board[row][col] in rowVals[row] or board[row][col] in colVals[col] or board[row][col] in boxVals[row//3, col//3]:
                    return False

                
                if board[row][col] != '.':
                    rowVals[row].append(board[row][col])
                    colVals[col].append(board[row][col])
                    boxVals[row//3, col//3].append(board[row][col])


            #print(rowVals)

        print(rowVals)
        print(colVals)
        print(boxVals)


        return True
