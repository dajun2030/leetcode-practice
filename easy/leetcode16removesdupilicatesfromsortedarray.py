def removeDuplicates(nums) :
    slow=0
    for fast in range(1, len(nums)):
        if nums[slow]!=nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
    return slow+1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4,4,55,6,7,8,8,8,8,8,9]))