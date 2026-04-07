import turtle,random,time
t = turtle.Turtle()
s = turtle.Screen()
s.setup(400,400)

def jump(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()

jump(0,-200)
turtle.write("Happy Easter",font=("Comic",30,"bold"),align="center")  
time.sleep(5)
turtle.clear()
turtle.hideturtle()
t.speed(0)
jump(-100,-20)
t.begin_fill()
t.setheading(270)
t.color('turquoise')
t.circle(100,180)
t.circle(200,45)
t.circle(60,90)
t.circle(200,45)
t.end_fill()


for i in range(20):
  jump(random.randint(-70,70),random.randint(-80,80))
  t.color('orange')
  t.dot(random.randint(1,10))

for i in range(20):
  jump(random.randint(-70,70),random.randint(-80,80))
  t.color('red')
  t.dot(random.randint(1,10))
for i in range(20):
  jump(random.randint(-70,70),random.randint(-80,80))
  t.color('gold')
  t.dot(random.randint(1,10))
for i in range(40):
  jump(random.randint(-70,70),random.randint(-80,80))
  t.color('blue')
for i in range(40):
  jump(random.randint(-70,70),random.randint(-80,80))
  t.color('green')  
  t.dot(random.randint(1,10))  

