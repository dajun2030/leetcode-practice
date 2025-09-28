# #1. 四次交换法（分层旋转） ⭐️ 最推荐
# def rotate(matrix):
#     n=len(matrix)
#     for i in range(n//2):
#         for j in range(i,n-1-i):
#             top_left=matrix[i][j]
#             top_right=matrix[j][n-1-i]
#             bottom_right=matrix[n-1-i][n-1-j]
#             bottom_left=matrix[n-1-j][i]
#
#             matrix[i][j]=bottom_left
#             matrix[j][n-1-i]=top_left
#             matrix[n-1-i][n-1-j]=top_right
#             matrix[n-1-j][i]=bottom_right
#     return matrix


#2. 转置 + 水平翻转法 ⭐️ 最简洁
def rotate(matrix):
    n=len(matrix)
    #转置
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    #翻转
    for row in matrix:
        row.reverse()
    return matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
for row in matrix:
    print(row)


