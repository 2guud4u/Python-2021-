bull = True
listy = [1, 878.8, 878.3, 8]
num = []
#assignment
for n in listy:
    num.append(n)
    i = num.index(n)
    print(i)
    bull = True
    #comparison sorting
    while bull:
        if i == 0:
            bull = False
        elif num[i] > num[i-1]:
            num[i], num[i-1] = num[i-1], num[i]
            i = i - 1
        else:
            break

print(num)



