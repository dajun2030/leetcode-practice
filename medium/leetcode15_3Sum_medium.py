def threeSum(nums):
    nums.sort()
    n=len(nums)
    result=[]

    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        if nums[i]>0:
            break

        left=i+1
        right=n-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total==0:
                result.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1

            elif total<0:
                left+=1
            else:
                right-=1

    return result

if __name__ == "__main__":
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [-2, 0, 1, 1, 2],
        [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    ]

    for i, nums in enumerate(test_cases):
        print(f"测试用例 {i + 1}: {nums}")
        result = threeSum(nums)
        print(f"结果: {result}")
        print()


