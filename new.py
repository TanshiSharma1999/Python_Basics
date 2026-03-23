import pgzrun
import random

WIDTH=600
HEIGHT=400
TITLE="Gen Alpha Words Matrix"

myColor = ["pink", "cyan", "yellow", "orange"]
myColor2 = ["Brown", "Black", "Red", "Navy"]
myemo= ["Skibidi", "Rizz", "Gyatt", "Sigma","Pookie"]
def draw():
    screen.fill(random.choice(myColor))
    
    Eid_list = []

    for i in range(5):
        rowList = []
        for m in range(5):
            rowList.append(random.choice(myemo))
        Eid_list.append(rowList)

    for i in range(5):
        for j in range(5):
            screen.draw.text(
                Eid_list[i][j],
                (50 + j * 100, 50 + i * 60),  # position (x, y)
                color=random.choice(myColor2)
            )

pgzrun.go()