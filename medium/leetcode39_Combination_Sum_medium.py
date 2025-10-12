class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()                       # 先排序，可提前剪枝

        def backtrack(start, path, current_sum):
            if current_sum == target:           # 收集答案
                result.append(path[:])
                return
            if current_sum > target:            # 超和，直接剪掉
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                current_sum += candidates[i]
                backtrack(i, path, current_sum) # 关键点：从 i 开始，允许复用
                path.pop()
                current_sum -= candidates[i]

        backtrack(0, [], 0)
        return result