def numRescueBoats(people, limit):
    """
    使用贪心算法和双指针解决救生艇问题

    算法核心思想：
    1. 将所有人按体重从小到大排序，便于系统性地进行配对
    2. 使用双指针策略：左指针指向最轻的人，右指针指向最重的人
    3. 尽量让最轻和最重的人配对坐船，这样可以最大化利用每艘船的载重能力
    4. 如果配对失败（体重和超限），则让最重的人单独坐船

    参数:
    people: 列表，包含每个人的体重，people[i]表示第i个人的体重
    limit: 整数，每艘船的最大承载重量

    返回:
    整数，表示运送所有人所需的最小船数
    """
    people.sort()
    left,right=0,len(people)-1
    boats=0

    while left<=right:
        if people[left]+people[right]<=limit:
            left+=1
            right -= 1
        else:
            right-=1
        boats+=1
    return boats
