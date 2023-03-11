from  turtle import*
t = Turtle()
t.color('green')
t.pensize(2)
t.hideturtle()

def circle_bottom():
    t.up()
    t.goto(0, -230)
    t.down()
    t.circle(90)

def circle_center():
    t.up()
    t.goto(0, -90)
    t.down()
    t.circle(70)

def circle_top():
    t.up()
    t.goto(0, 10)
    t.down()
    t.circle(50)  

def  nose():
    t.up()
    t.goto(0, 60)
    t.down()
    t.forward(60)
    t.right(170)
    t.forward(60)
    t.right(90)
    t.forward(11)

def  eye_left():
    t.up()
    t.goto(-10, 80)
    t.down()
    t.circle(10)

def eye_right():
    t.up()
    t.goto(30, 80)
    t.down()
    t.circle(10)

def mouth():
    t.up()
    t.goto(-10, 25)
    t.down()
    t.left(40)
    t.forward(20)
    t.right(140)
    t.forward(60)
    t.right(163)
    t.forward(46)

def button_1():
    t.up()
    t.goto(0, -50)
    t.down()
    t.circle(15)

def button_2():
    t.up()
    t.goto(0, -95)
    t.down()
    t.circle(15)

def button_3():
    t.up()
    t.goto(0, -95)
    t.down()
    t.circle(15)

def button_4():
    t.up()
    t.goto(0, -140)
    t.down()
    t.circle(15)

def left_hand():
    t.up()
    t.goto(-20, -6)
    t.down()
    t.right(13)
    t.forward(130)
    t.right(180)
    t.forward(30)
    t.right(130)
    t.forward(30)
    t.right(180)
    t.forward(30)
    t.right(270)
    t.forward(30)

def right_hand():
    t.up()
    t.goto(20, -6)
    t.down()
    t.left(210)
    t.forward(130)
    t.left(180)
    t.forward(30)
    t.left(130)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.left(270)
    t.forward(30)
    
def bucket():
    t.up()
    t.goto(-45, 93)
    t.down()
    t.right(33)
    t.forward(90)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(75)