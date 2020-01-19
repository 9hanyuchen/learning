import  turtle
import time

def writePoetry():
	turtle.penup()
	turtle.goto(400, -150)
	turtle.pencolor((255, 255, 0))
	# 诗句
	potery = ["但\n愿\n人\n长\n久\n", "千\n里\n共\n婵\n娟\n"]
	# 诗句位置(可自行设计添加), 最好2/4句五言诗
	coordinates = [(300, -150), (200, -150), (100, -150)]
	for i, p in enumerate(potery):
		turtle.write(p, align="center", font=("STXingkai", 50, "bold"))
		if (i + 1) != len(potery):
			time.sleep(2)
			turtle.goto(coordinates[i])



turtle.hideturtle()
# turtle.setup(1000, 600)
turtle.colormode(255)
# turtle.bgcolor((16, 78, 139))
# turtle.speed(3)
writePoetry()

turtle.exitonclick()