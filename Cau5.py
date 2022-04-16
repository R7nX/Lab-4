

for i in range(1000,9999):
    temp = 0
    x = i
    while i > 0: 
        temp = temp + i%10
        i = i // 10
    if temp == 9:
        print(x, end = " ")

            



