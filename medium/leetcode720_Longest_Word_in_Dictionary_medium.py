class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end=True

    def search_all_prefixes(self,word):
        node=self.root
        for char in word:
            if char not in node.children or not node.children[char].is_end:
                return []
            node=node.children[char]
        return True

class Solution:
    def longestWord(self,words):
        trie=Trie()
        for word in words:
            trie.insert(word)
        longest_word=''

        for word in words:
            if trie.search_all_prefixes(word):
                if len(word)>len(longest_word):
                    longest_word=word
                elif len(word)==len(longest_word) and word<longest_word:
                    longest_word=word
        return longest_word


def main():
    solution = Solution()

    # 测试用例1
    words1 = ["w", "wo", "wor", "worl", "world"]
    print("测试用例1:")
    print(f"输入: {words1}")
    result1 = solution.longestWord(words1)
    print(f"输出: '{result1}'")
    print("预期: 'world'")
    print()

    # 测试用例2
    words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print("测试用例2:")
    print(f"输入: {words2}")
    result2 = solution.longestWord(words2)
    print(f"输出: '{result2}'")
    print("预期: 'apple'")
    print()

    # 测试用例3
    words3 = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "e"]
    print("测试用例3:")
    print(f"输入: {words3}")
    result3 = solution.longestWord(words3)
    print(f"输出: '{result3}'")
    print("预期: 'yodn'")


if __name__ == "__main__":
    main()


