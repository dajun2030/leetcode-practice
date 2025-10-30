def addBinary(a, b):
    i,j=len(a)-1,len(b)-1
    carry=0  #进位
    result=[]

    while i>=0 or j>=0 or carry:
        # 获取当前位的数字，如果索引越界则为0
        digit_a=int(a[i]) if i>=0 else 0
        digit_b=int(b[j]) if j>=0 else 0

        # 计算当前位的和（包括进位）
        total=digit_a+digit_b+carry
        #当前位的结果
        current_digit=total%2
        #更新进位
        carry=total//2

        result.append(str(current_digit))
        i-=1
        j-=1
        # 反转结果，因为是从低位到高位添加的
    return ''.join(reversed(result))
print(addBinary("1010", "1011"))
##############################################################
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry, val = val // 2, val % 2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]

