def merge_the_tools(string, k):
    n = len(string)
    if n == 0 or k <= 0: return []
    results = []

    for i in range(0, n, k):
        block = string[i:i + k]
        seen = set()
        res = []
        for ch in block:
            if ch not in seen:
                seen.add(ch)
                res.append(ch)
        print(''.join(res))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)