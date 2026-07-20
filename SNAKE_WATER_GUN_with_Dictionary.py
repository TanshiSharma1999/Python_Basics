'''
1 for snake 
2 for water
3 for gun
'''
import random

print("!!!Snake-Water-Gun!!!")
print(" Type s for snake\n Type w for water\n Type g for gun")
you=input("Enter your choice: ")
youDict={"s":1,"w":2,"g":3}
you=youDict[you]
computer=random.randint(1,3)
ComDict={1:"snake",2:"water",3:"gun"}
com=ComDict[computer]
print(f"Computer chose: {com}")
#COMPUTER
if (computer==1) and (you==2):
    print("computer wins!")
elif (computer==2) and (you==3):
    print("computer wins!")
elif (computer==3) and (you==1):
    print("computer wins!")
#TIE
elif (computer==you):
    print("Tie wins!")
#You
else:
    print("You win!")