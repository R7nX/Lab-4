n = int(input("Input number: "))


if n < 0:
    print ("Invalid number")
number = 1
for i in range (1,n+1):
    number = number*i
print(f"{n}!=",number)