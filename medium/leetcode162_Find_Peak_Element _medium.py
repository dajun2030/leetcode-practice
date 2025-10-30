def findPeakElement(nums):
    left,right=0,len(nums)-1
    if not nums or len(nums)==0:
        return -1
    if len(nums)==1:
        return 0

    while left<right:
        mid=left+(right-left)//2

        if nums[mid]>nums[mid+1]:
            right=mid
        else:
            left=mid+1
    return left

