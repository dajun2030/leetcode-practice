def dailyTemperatures(temperatures):
    n=len(temperatures)
    stack=[]
    answer=[0]*n

    for i in range(n):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            pre_index=stack.pop()
            answer[pre_index]=i-pre_index
        stack.append(i)
    return answer

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

