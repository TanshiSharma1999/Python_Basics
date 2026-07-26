import random 
import math

x = random.randint(1,90)
m = random.randint(500,1000)
y = random.randint(1,10)
v = random.randint(100,400)

answer=0
c = 3
guess_count=0
while(answer!=math.floor(x/y) and guess_count!=4):
  
  print("If x => {}, y => {}".format(x,y))
  answer = int(input("What would the the quotient be if x is Divided by y? [input as integer] "))
  
  if answer == math.floor(x/y):
    print("good job! you guessed it correctly!")
  else:
    print("Try again, You have {} Tries".format(c))
    c-=1
    guess_count+=1

if(guess_count ==4):
  print("Game over!")
print("Next Question!")

guess_count=0
ans_2 = 0
d = 3
while(ans_2!=math.floor(m/v) and guess_count!=4):
  ans_2 = int(input("If a => {}, b => {} then what is a/b? [input as integer] ".format(m,v)))
  if ans_2 == math.floor(m/v):
    print("good job! you guessed it correctly!")
  else:
    print("Try again, You have {} Tries".format(d))
    d-=1
    guess_count+=1    
if(guess_count ==3):
  print("Game over!")