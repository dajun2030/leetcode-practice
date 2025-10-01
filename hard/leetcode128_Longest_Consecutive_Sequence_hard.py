def longestConsecutive(nums):
    if not nums:
        return 0

    longest_steak=0
    num_set=set(nums)

    for num in num_set:
        if num-1 not in num_set:
            current_num=num
            current_steak=1

            while current_num+1 in num_set:
                current_num+=1
                current_steak+=1
            longest_steak=max(longest_steak, current_steak)
    return longest_steak


print(longestConsecutive([100, 4, 200, 1, 3, 2]))