import pgzrun
TITLE = "QUIZ MASTER"
WIDTH = 800
HEIGHT = 600
title_box = Rect(0,0,WIDTH,100)
question_box = Rect(0,0,600,120)
timer_box = Rect(0,0,300,120)#decides width,height
title_box.move_ip(0,0)
question_box.move_ip(0,125)
timer_box.move_ip(600,125)#decides (x,y)
answer_box1=Rect(0,0,350,100)
answer_box2=Rect(0,0,350,100)
answer_box3=Rect(0,0,350,100)
answer_box4=Rect(0,0,350,100)
answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
answer_box1.move_ip(0,255)
answer_box2.move_ip(450,255)
answer_box3.move_ip(0,395)
answer_box4.move_ip(450,395)



def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(title_box,"red")
    screen.draw.filled_rect(question_box,"orange")
    screen.draw.filled_rect(timer_box,"blue")
    for i in answer_boxes:
        screen.draw.filled_rect(i,"yellow")










pgzrun.go()