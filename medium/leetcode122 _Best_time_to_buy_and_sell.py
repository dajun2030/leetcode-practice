# def maxProfit(prices) -> int:
#     max_profit = 0
#     for i in range(0,len(prices)-1):
#         if prices[i+1]>prices[i]:
#             max_profit += prices[i+1] - prices[i]
#     return max_profit



#波峰波谷法
def maxProfit(prices) -> int:
    n=len(prices)
    if n == 0: return 0
    profit=0
    i=0

    while i<n-1:
        while i<n-1 and prices[i]>=prices[i+1]:
            i+=1
        buy=prices[i]
        while i<n-1 and prices[i]<=prices[i+1]:
            i+=1
        sell=prices[i]
        profit+=sell-buy

    return profit

print(maxProfit([7,1,5,3,6,4]))