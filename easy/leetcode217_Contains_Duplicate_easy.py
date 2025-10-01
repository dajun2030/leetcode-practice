def containsDuplicate(nums):
    length=len(nums)
    nums_set=set(nums)
    length_set=len(nums_set)
    if length!=length_set:
        return True
    else:
        return False

print(containsDuplicate([1,2,3,3]))