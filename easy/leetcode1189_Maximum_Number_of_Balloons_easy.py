# def maxNumberOfBalloons(text: str):
#     target='balloon'
#     need={}
#     for char in target:
#         need[char]=need.get(char,0)+1
#
#     have={}
#     for char in text:
#         have[char]=have.get(char,0)+1
#
#     result=float('inf')
#     for char in need:
#         if char not in have:
#             return 0
#         count=have[char]//need[char]
#         if count<result:
#             result=count
#     return result

#解法1：手动计数 + 直接计算
# def maxNumberOfBalloons(text: str):
#     countb=counta=countl=counto=countn=0
#     for char in text:
#         if char=="b":
#             countb+=1
#         elif char=="a":
#             counta+=1
#         elif char=="l":
#             countl+=1
#         elif char=="o":
#             counto+=1
#         elif char=="n":
#             countn+=1
#
#     result=min(countb,counta,countl//2,counto//2,countn)
#     return result

#解法2：数组计数法
# def maxNumberOfBalloons(text: str):
#     count=[0]*26
#     for char in text:
#         index=ord(char)-ord('a')
#         count[index]+=1
#
#     result=min(count[1],count[0],count[11]//2,count[14]//2,count[13])
#     return result

#解法3：消耗模拟法
def maxNumberOfBalloons(text: str):
    from collections import defaultdict
    counts=defaultdict(int)
    for char in text:
        if char in 'balon':
            counts[char]+=1

    instanses=0
    while True:
        if (counts['b']>=1 and counts['a']>=1 and counts['l']>=2 and
                counts['o']>=2 and counts['n']>=1):
            counts['b']-=1
            counts['a']-=1
            counts['l']-=2
            counts['o']-=2
            counts['n']-=1
            instanses += 1
        else:
            break
    return instanses

print(maxNumberOfBalloons("balloonballoonballoonballoonballoonballoon"))