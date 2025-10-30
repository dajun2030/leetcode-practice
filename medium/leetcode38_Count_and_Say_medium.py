class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = "1"  # 序列从 "1" 开始
        for i in range(n-1):
            seq = self.getNext(seq)  # 生成下一项
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            count = 1
            # 统计连续相同数字的数量
            while i < len(seq) - 1 and seq[i] == seq[i+1]:
                count += 1
                i += 1
            # 将计数和数字添加到新序列中
            next_seq += str(count) + seq[i]
            i += 1
        return next_seq

solution=Solution()
print(solution.countAndSay(4))
print(solution.countAndSay(5))
print(solution.countAndSay(6))
print(solution.countAndSay(7))