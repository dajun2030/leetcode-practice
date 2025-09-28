def conversion(s,numRow):
    if numRow==1 or numRow>=len(s):
        return s

    rows=['']*numRow
    current_row=0
    direction=False

    for char in s:
        rows[current_row]+=char
        if current_row==0 or current_row == numRow-1:
            direction=not direction
        current_row+=1 if direction else -1
    for i in range(numRow):
        print(rows[i])
    return ''.join(rows)

print(conversion("abcdefghijklmn",3))
