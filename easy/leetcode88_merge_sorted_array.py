def merge(nums1, m, nums2, n):
    i,j,k=m-1,n-1,m+n-1

    while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i-=1

        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1

    while j>=0:
        nums1[k] = nums2[j]
        j-=1
        k-=1



# 测试
def test_merge():
    # 测试用例1
    nums1 = [1, 2, 3, 4, 5, 6]
    m = 3
    nums2 = [7, 8, 9]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)  # 输出: [1,2,2,3,5,6]

    # 测试用例2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(nums1)  # 输出: [1]

    # 测试用例3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)  # 输出: [1]


if __name__ == "__main__":
    test_merge()
