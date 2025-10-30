def minCostToMoveChips(position):
    even_count=0
    odd_count=0

    for po in position:
        if po%2==0:
            even_count+=1
        else:
            odd_count+=1
    return min(even_count,odd_count)

print(minCostToMoveChips([2,2,2,3,3]))