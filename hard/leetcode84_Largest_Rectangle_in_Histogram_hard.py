def largestRectangleArea(heights):
    n=len(heights)
    if n==0:
        return 0

    left=[0]*n
    right=[0]*n
    stack=[]

    for i in range(n):
        while stack and heights[stack[-1]]>=heights[i]:
            stack.pop()
        left[i]=stack[-1] if stack else -1
        stack.append(i)

    stack=[]
    for i in range(n-1,-1,-1):
        while stack and heights[stack[-1]]>=heights[i]:
            stack.pop()
        right[i]=stack[-1] if stack else n
        stack.append(i)

    max_area=0
    for i in range(n):
        width=right[i]-left[i]-1
        area=heights[i]*width
        max_area=max(max_area,area)

    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))