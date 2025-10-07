def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n=len(nums)
    if n==0:
        return 0

    left,right=0,n-1

    while left<=right:
        mid = left + (right - left) // 2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left

print(searchInsert([-4,-1,0,3,10],-1))