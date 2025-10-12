class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def backtrack(i, j, index):
            # 如果已经匹配完所有字符
            if index == len(word):
                return True

            # 检查边界条件和是否已访问
            if (i < 0 or i >= len(board) or
                    j < 0 or j >= len(board[0]) or
                    board[i][j] != word[index]):
                return False

            # 标记当前单元格为已访问（临时修改）
            temp = board[i][j]
            board[i][j] = '#'  # 使用特殊字符标记已访问

            # 向四个方向搜索
            found = (backtrack(i + 1, j, index + 1) or  # 下
                     backtrack(i - 1, j, index + 1) or  # 上
                     backtrack(i, j + 1, index + 1) or  # 右
                     backtrack(i, j - 1, index + 1))  # 左

            # 回溯，恢复单元格原始值
            board[i][j] = temp

            return found

        # 遍历网格中的每个单元格作为起点
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False


def test_exist():
    solution = Solution()

    test_cases = [
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], "ABCCED", True),
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], "SEE", True),
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], "ABCB", False),
        ([['A']], "A", True),
        ([['A', 'B']], "BA", True)
    ]

    print("🧪 Word Search 测试")
    print("=" * 50)

    for i, (board, word, expected) in enumerate(test_cases, 1):
        result = solution.exist(board, word)
        status = "✅" if result == expected else "❌"
        print(f"测试 {i}: word='{word}'")
        print(f"  结果: {result} {status}")
        print(f"  期望: {expected}")
        print()


# 运行测试
test_exist()