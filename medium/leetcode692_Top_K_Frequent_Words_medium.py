#最小堆法
import heapq  # 导入堆队列算法模块，提供最小堆实现
from collections import Counter  # 导入计数器，用于快速统计频率

def topKFrequent(words, k):
    # 步骤1：使用Counter统计每个单词的出现频率
    # Counter会自动创建一个字典，键是单词，值是出现次数
    # 例如：words = ["i","love","i"] → freq = {'i':2, 'love':1}
    freq = Counter(words)

    # 步骤2：构建最小堆来找到前k个最频繁的单词
    # 堆（heap）是一种特殊的二叉树结构，最小堆的根节点总是最小的元素
    heap = []  # 初始化一个空列表作为堆

    # 遍历频率字典中的每个单词和对应的出现次数
    for word, count in freq.items():
        # 将元素推入堆中，每个元素是一个元组 (-count, word)
        # 使用 -count 的原因：
        # - Python的heapq模块只提供最小堆实现
        # - 我们需要频率高的单词在堆顶，所以用负号将问题转化为"找最小值"
        # - 例如：count=4 → -count=-4，在最小堆中-4比-3小，所以会排在前面
        heapq.heappush(heap, (-count, word))
        # 此时堆会根据元组的第一个元素(-count)进行排序
        # 频率相同的情况下，会比较第二个元素word（字典序）

    # 步骤3：从堆中提取前k个最频繁的单词
    result = []  # 初始化结果列表

    # 循环k次，每次从堆中弹出最小的元素（即频率最高的单词）
    for _ in range(k):
        # heapq.heappop(heap) 弹出并返回堆中最小的元素
        # 返回的是元组 (-count, word)，我们只需要单词部分，所以取索引[1]
        popped_element = heapq.heappop(heap)  # 返回例如 (-2, 'i')
        word_only = popped_element[1]  # 提取单词 'i'
        result.append(word_only)

    # 返回包含前k个最频繁单词的列表
    return result

print(topKFrequent(["i","love","leetcode","i","love","coding"], 2))
print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 1))

#哈希表+排序法
# def topKFrequent(words, k):
#     freq={}
#     for word in  words:
#         freq[word]=freq.get(word,0)+1
#
#     sorted_words=sorted(freq.keys(),key=lambda x:(-freq[x],x))
#     return sorted_words[:k]
#
# print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 2))