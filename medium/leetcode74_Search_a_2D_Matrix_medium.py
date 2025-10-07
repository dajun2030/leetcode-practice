def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 测试用例
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

test_cases = [3, 13, 1, 60, 0, 61, 20]
for target in test_cases:
    result = searchMatrix(matrix, target)
    print(f"target = {target}, found = {result}")

# 输出：
# target = 3, found = True
# target = 13, found = False
# target = 1, found = True
# target = 60, found = True
# target = 0, found = False
# target = 61, found = False
# target = 20, found = True