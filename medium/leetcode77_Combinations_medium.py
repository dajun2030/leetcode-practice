# class Solution:
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         def backtrack(start, path):
#             if len(path)==k:
#                 result.append(path[:])
#                 return
#
#             for i in range(start,n+1):
#                 path.append(i)
#                 backtrack(i+1,path)
#                 path.pop()
#
#         result=[]
#         backtrack(1,[])
#         return result

####################################################
def combine(n, k):
    result = []

    def backtrack(start, path):
        # 如果路径长度等于k，说明找到一个组合
        if len(path) == k:
            result.append(path[:])
            return

        # 从start开始遍历到n
        for i in range(start, n + 1):
            # 选择当前数字
            path.append(i)
            # 递归探索后续数字（从i+1开始，避免重复）
            backtrack(i + 1, path)
            # 回溯，撤销选择
            path.pop()

    backtrack(1, [])
    return result


# 测试
print("组合结果 n=4, k=2:", combine(4, 2))