class Solution:
    def findCircleNum(self, isConnected):
        """
        并查集版本
        """
        # 第1-3行：基础检查
        n = len(isConnected)
        if n == 0:
            return 0

        # 第4-5行：初始化并查集
        parent = list(range(n))  # 每个城市的父节点初始为自己
        # 💡 parent[i] 表示城市 i 的父节点

        # 第6行：初始化连通分量数量
        count = n  # 初始时每个城市都是一个独立的连通分量

        # 第7-14行：遍历所有边
        for i in range(n):  # 遍历矩阵的上三角（避免重复）
            for j in range(i + 1, n):  # j 从 i+1 开始
                # 第8行：检查是否相连
                if isConnected[i][j] == 1:
                    # 第9-13行：合并操作
                    root_i = self.find(parent, i)  # 找到 i 的根
                    root_j = self.find(parent, j)  # 找到 j 的根

                    if root_i != root_j:  # 如果不在同一个集合
                        parent[root_i] = root_j  # 合并集合
                        count -= 1  # 连通分量减少1

        # 第15行：返回结果
        return count

    def find(self, parent, i):
        """
        查找根节点（带路径压缩）
        """
        # 第19-22行：路径压缩
        if parent[i] != i:  # 如果 i 不是根节点
            parent[i] = self.find(parent, parent[i])  # 递归查找并压缩路径
        return parent[i]  # 返回根节点