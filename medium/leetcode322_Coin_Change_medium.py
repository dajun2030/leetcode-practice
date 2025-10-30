# def coinChange(coins, amount):
#     # dp[i]表示凑成金额i所需的最小硬币数
#     dp=[float('inf')]*(amount+1)
#     dp[0]=0
#
#     #遍历所有金额
#     for i in range(amount+1):
#         #尝试所有硬币
#         for coin in coins:
#             #如果当前金额大于等于硬币币值
#             if i>=coin:
#                 dp[i]=min(dp[i],dp[i-coin]+1)
#
#     return dp[amount] if dp[amount]!=float('inf') else -1


def coinChange_tutor_simple():
    coins = [1, 2, 5]
    amount = 11

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    print(f"目标: 用硬币{coins}凑出{amount}元")
    print(f"初始化: dp[0]=0")

    for i in range(1, amount + 1):
        print(f"\n计算金额{i}:")
        for coin in coins:
            if i >= coin:
                remain = i - coin
                new_count = dp[remain] + 1
                if new_count < dp[i]:
                    dp[i] = new_count
                    print(f"  用{coin}元 → dp[{remain}]+1={new_count}")

        if dp[i] == float('inf'):
            print(f"  无法凑出")
        else:
            print(f"  最少需要: {dp[i]}个硬币")

    result = dp[amount] if dp[amount] != float('inf') else -1
    print(f"\n凑出{amount}元需要: {result}个硬币")
    return result


coinChange_tutor_simple()