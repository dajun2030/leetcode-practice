class MyHashSet(object):

    def __init__(self):
        self.array=[False]*100001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.array[key]=True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.array[key]=False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.array[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)