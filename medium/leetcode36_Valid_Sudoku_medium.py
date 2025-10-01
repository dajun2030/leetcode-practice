# #思路2：一次遍历
# def isValidSudoku(board):
#     rows=[set() for _ in range(9)]
#     cols=[set() for _ in range(9)]
#     boxes=[set() for _ in range(9)]
#
#     for i in range(9):
#         for j in range(9):
#             num=board[i][j]
#
#             if num==".":
#                 continue
#
#             box_index=(i//3)*3+j//3
#
#             if (num in rows[i] or num in cols[j] or num in boxes[box_index] ):
#                 return False
#
#             rows[i].add(num)
#             cols[j].add(num)
#             boxes[box_index].add(num)
#     return True

#思路1：三次独立遍历
def isValidSudoku(board):
    for i in range(9):
        seen=set()
        for j in range(9):
            num=board[i][j]
            if num=='.':
                continue
            if num in seen:
                return False
            seen.add(num)

    for j in range(9):
        seen=set()
        for i in range(9):
            num=board[i][j]
            if num=='.':
                continue
            if num in seen:
                return False
            seen.add(num)

    for box_row in range(3):
        for box_col in range(3):
            seen=set()
            for i in range(box_row*3,box_row*3+3):
                for j in range(box_col*3,box_col*3+3):
                    num=board[i][j]
                    if num=='.':
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
    return True




