# def romanToInt(s: str) -> int:
#     romedic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#     total=0
#     n=len(s)
#
#     for i in range(n-1):
#         current_value=romedic[s[i]]
#         next_value=romedic[s[i+1]]
#         if current_value>=next_value:
#             total+=current_value
#         else:
#             total-=current_value
#     total+=romedic[s[-1]]
#     return total

def romanToInt(s: str) -> int:
    # 先替换所有特殊情况
    special_replacements = {
        'IV': 'IIII',
        'IX': 'VIIII',
        'XL': 'XXXX',
        'XC': 'LXXXX',
        'CD': 'CCCC',
        'CM': 'DCCCC'
    }

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # 替换所有特殊情况为等价的加法形式
    for special, replacement in special_replacements.items():
        s = s.replace(special, replacement)

    # 现在只需要简单相加
    return sum(roman_map[char] for char in s)

print(romanToInt("LVIII"))



