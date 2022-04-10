n = int(input("N: "))


print("Dãy số nguyên tố: ", end = "")

for snt in range(1, n+1): 
    p = 0 
    for i in range(1, snt+1):
        if snt%i == 0: 
            p = p+1
    if p == 2: 
        if n%2 == 0: 
            if snt < (n-1):
                print(snt, end = ", ")
            else: 
                print(snt)
        else:
            if snt < (n):
                print(snt, end = ", ")
            else: 
                print(snt) 