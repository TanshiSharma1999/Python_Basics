# OPT+3 or Cmd+/
# Function is a reusable, set of instructions designed to perform a task
#1. print,input are built in functions
#2. User Defined Function

def areaRect():
    print("Calculating area of a Rectangle!")
    l=float(input("Enter length:"))
    h=float(input("ENter height: "))
    area=l*h
    print(f"Area of the rectangle is {area}")

def areaTri():
    print("Calculating area of a Triangle!")
    b=float(input("Enter Base:"))
    h=float(input("ENter height: "))
    area=(b*h)/2
    print(f"Area of a triangle is {area}")

def areaCircle():
    print("Calculating area of a Circle!")
    r=float(input("Enter radius: "))
    area=3.14*r*r
    print(f"Area of a circle is {area}")

def areaSquare():
    print("Calculating area of a Square!")
    l=float(input("Enter length:"))
    area=l*l
    print(f"Area of the square is {area}")

while True:
    print("*"*100)
    print("Welcome to Area Calculator!!")
    choose=input("Pick a shape Square, Rectangle, Triangle, circle or quit? ").lower()
    if choose=="square":
        areaSquare()
    elif choose =="rectangle":
        areaRect()
    elif choose=="triangle":
        areaTri()
    elif choose=="circle":
        areaCircle()
    elif choose=="quit":
        print("Bye")
        break
    else:
        print("Invalid choice! Pick a shape Square, Rectangle, Triangle, circle or quit? ")
    