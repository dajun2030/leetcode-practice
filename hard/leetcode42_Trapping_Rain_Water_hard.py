def trap(height):
    if not height:
        return 0

    n=len(height)
    left,right=0,n-1
    left_max=right_max=0
    water=0

    while left<right:
        if height[left]<height[right]:
            if height[left]>=left_max:
                left_max=height[left]
            else:
                water+=left_max-height[left]
            left+=1
        else:
            if height[right]>=right_max:
                right_max=height[right]
            else:
                water+=right_max-height[right]
            right-=1
    return water


if __name__ == "__main__":
    # 测试序列
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    # 计算实际结果
    result = trap(heights)
    print(f"输入数组: {heights}")
    print(f"实际结果: {result}")