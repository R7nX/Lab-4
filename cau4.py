n = int(input("Nhap so nguyen:"))
b = n
sum = 0
while (n > 0):
    sum = sum +n%10
    n = n//10
print (f"Sum of digit of {b}  ",sum)