s = 'UUDUDUD'
list1 = []
for i in s:
    list1.append(i)

result = [0]
for i in list1:
    if i == 'U':
        result.append(1)
    elif i == 'D':
        result.append(-1)


print(result)



