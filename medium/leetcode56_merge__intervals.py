def merge(intervals):
    if not intervals:
        return []

    intervals.sort( key = lambda x:x[0])
    merged=[intervals[0]]
    for i in range(1,len(intervals)):
        current_start,current_end = intervals[i]
        last_merged_start,last_merged_end = merged[-1]
        if current_start <= last_merged_end:
            merged[-1][1]=max(current_end,last_merged_end)
        else:
            merged.append(intervals[i])

    return merged
print(merge([[1,3],[2,9],[8,10],[15,18]]))