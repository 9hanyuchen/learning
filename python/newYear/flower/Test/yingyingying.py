import turtle


def run(angle, lenth):
    turtle.seth(angle)
    turtle.fd(lenth)


def change(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def init():
    turtle.pensize(10)
    turtle.pencolor("purple")


turtle.setup(800, 400, 200, 200)
init()
# wu
change(-350, 100)
run(0, 100)
run(-90, 70)
run(180, 100)
run(90, 70)
change(-350, 0)
run(0, 100)
change(-400, -50)
run(0, 200)
change(-300, 0)
run(-90, 50)
run(-125, 100)
change(-300, -50)
run(-55, 100)
run(0, 10)
# feng
change(-65, 70)
run(0, 130)
change(-50, 10)
run(0, 100)
change(-100, -70)
run(0, 200)
change(0, -160)
run(90, 280)
# yuan
change(125, 100)
run(-35, 40)
change(125, 25)
run(-35, 40)
change(125, -125)
run(55, 90)
change(220, 100)
run(0, 110)
change(220, 100)
run(-95, 230)
change(285, 85)
run(-145, 40)
change(250, 65)
run(0, 70)
run(-90, 80)
run(180, 70)
run(90, 80)
change(250, 25)
run(0, 70)
change(285, -15)
run(-90, 120)
run(135, 20)
change(250, -50)
run(-125, 40)
change(315, -50)
run(-55, 50)