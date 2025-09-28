def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    m,n=len(matrix),len(matrix[0])
    top,bottom=0,m-1
    left,right=0,n-1
    result=[]

    while top<=bottom and left<=right:
        for col in range(left,right+1):
            result.append(matrix[top][col])
        top+=1
        for row in range(top,bottom+1):
            result.append(matrix[row][right])
        right-=1

        if top<=bottom:
            for col in range(right,left-1,-1):
                result.append(matrix[bottom][col])
            bottom-=1

        if left<=right:
            for row  in range(bottom,top-1,-1):
                result.append(matrix[row][left])
            left+=1
    return result

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))