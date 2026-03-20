

#function is a set of instruction created to execute a task

def AreaRect(l,w):#create a function
  area=l*w
  print(area)

def AreaSq(l):
  area=l*l
  print(area)
  
def AreaCir(r):
  area=r*r*3.14
  print(area)

def AreaTri(b,h):
  area=(b*h)/2
  print(area)

while True:
  shape=input("Enter the shape to find its area(Square,Rectangle,circle,triangle or 'exit' to end): ").lower().strip()
  if shape=="exit":
    print("Thankyou!")
    exit
  elif shape=="rectangle":
    l=int(input("Enter the length of rectangle: "))
    w=int(input("Enter the width of rectangle: "))
    AreaRect(l,w)
  elif shape=="square":
    l=int(input("Enter the length of square: "))
    AreaSq(l)
  elif shape=="circle":
    r=int(input("Enter the radius of circle: "))
    AreaCir(r)
  elif shape=="triangle":
    b=int(input("Enter the base of triangle: "))
    h=int(input("Enter the height of triangle: "))
    AreaTri(b,h)      