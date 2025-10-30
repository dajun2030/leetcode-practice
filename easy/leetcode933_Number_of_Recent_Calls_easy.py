from collections  import deque
class RecentCounter(object):

    def __init__(self):
        self.q=deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)                    # 新请求入队
        while self.q[0]<t-3000:             # 移除过期请求
            self.q.popleft()
        return len(self.q)                  # 移除过期请求
