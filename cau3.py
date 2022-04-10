a = int(input("Enter your number: "))
p = 0 

for i in range(1, a+1):
    if a%i == 0:
        p = p+1

if p == 2: 
    print("Day la so nguyen to")
else:
    print("Day khong phai la so nguyen to")