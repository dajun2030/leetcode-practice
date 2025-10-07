#二分查找法
# def isPerfectSquare(num):
#     if num == 0 or num == 1:
#         return True
#     left, right = 2, num
#     while left <= right:
#         mid=left + (right - left) // 2
#         if mid**2==num:
#             return True
#         elif mid**2<num:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False

#数学法
def isPerfectSquare(num):
    sum = 0
    i=1
    while sum <num:
        sum+=i
        i+=2
        if sum==num:
            return True
    return False


test_cases = [1, 4, 9, 16, 14, 25, 100, 99, 10000, 2147395600]
results = []

for num in test_cases:
    result = isPerfectSquare(num)
    results.append((num, result))
    print(f"num = {num}, isPerfectSquare = {result}")
print(results)