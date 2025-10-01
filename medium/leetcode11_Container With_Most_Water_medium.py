def maxArea(height):
    n=len(height)
    left,right=0,n-1
    maxarea=0

    while left<right:
        current_height=min(height[left],height[right])
        width=right-left
        current_area=current_height*width
        maxarea=max(maxarea,current_area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return maxarea

print(maxArea([1,8,6,2,5,4,8,3,7]))

