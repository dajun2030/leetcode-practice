def singleNumber(nums):
    result=0
    for num in nums:
        result^=num
    return result

print(singleNumber([4,1,2,1,2,5,6,5,6]))