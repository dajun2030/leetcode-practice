def threeSumClosest(nums, target):
    nums.sort()
    n=len(nums)
    closest_sum=float('inf')
    min_diff=float('inf')

    for i in range(n-2):
        left=i+1
        right=n-1

        while left<right:
            current_sum=nums[i]+nums[left]+nums[right]
            current_diff=abs(current_sum-target)
            if current_sum==target:
                return current_sum

            if current_diff<min_diff:
                min_diff=current_diff
                closest_sum=current_sum

            if current_sum<target:
                left+=1
            else:
                right-=1
    return closest_sum

print(threeSumClosest([1, 2, 3, 4, 5], 10))


