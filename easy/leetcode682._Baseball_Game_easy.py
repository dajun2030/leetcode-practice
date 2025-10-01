def calPoints(operations):
    stack=[]

    for ops in operations:
        if ops=="+":
            last1=stack[-1]
            last2=stack[-2]
            last=last1+last2
            stack.append(last)
        elif ops=="D":
            last=stack[-1]
            stack.append(last*2)
        elif ops=="C":
            stack.pop()
        else:
            stack.append(int(ops))
    return sum(stack)

print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))