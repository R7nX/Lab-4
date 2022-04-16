import turtle

a = int(input("Input number of side: "))

for i in range(a):
    turtle.forward(100)
    turtle.right(180 - ((a-2)*180)/a)

turtle.mainloop()
