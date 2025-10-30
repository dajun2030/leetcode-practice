def convertBase7(num):
    if num==0:
        return '0'
    if num<0:
        num=abs(num)
        negative=True
    else:
        negative=False

    result=[]
    while num>0:
        result.append(str(num%7))
        num//=7

    res_str=''.join(reversed(result))

    if negative:
        res_str='-'+res_str
    return res_str

print(convertBase7(-7))
