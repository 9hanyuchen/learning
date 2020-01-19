'''
Function:
	简单的中秋赏月图
Author:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import time
#import pygame
import turtle


'''写诗'''
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


'''画月亮'''
def drawMoon():
	turtle.penup()
	turtle.goto(-150, 0)
	turtle.fillcolor((212, 175, 55))
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(112)
	turtle.end_fill()


'''画云'''
def drawCloud():
	turtle.penup()
	turtle.goto(-500, 200)
	turtle.fillcolor((245, 245, 245))
	turtle.pencolor((220, 220, 220))
	turtle.pensize(5)
	turtle.pendown()
	turtle.forward(250)
	def cloud(mode='right'):
		for i in range(90):
			turtle.pensize((i+1)*0.2+5)
			turtle.right(1) if mode == 'right' else turtle.left(1)
			turtle.forward(0.5)
		for i in range(90):
			turtle.pensize(90*0.2+5-0.2*(i+1))
			turtle.right(1) if mode == 'right' else turtle.left(1)
			turtle.forward(0.5)
	cloud()
	turtle.forward(100)
	cloud('left')
	turtle.forward(600)


'''画山'''
def drawMountain():
	turtle.penup()
	turtle.goto(-500, -250)
	turtle.pensize(4)
	turtle.fillcolor((36, 36, 36))
	turtle.pencolor((31, 28, 24))
	turtle.pendown()
	turtle.begin_fill()
	turtle.left(20)
	turtle.forward(400)
	turtle.right(45)
	turtle.forward(200)
	turtle.left(60)
	turtle.forward(300)
	turtle.right(70)
	turtle.forward(300)
	turtle.goto(500, -300)
	turtle.goto(-500, -300)
	turtle.end_fill()


'''初始化'''
def initTurtle():
	# pygame.mixer.init()
	# pygame.mixer.music.load('bgm.mp3')
	# pygame.mixer.music.play(-1, 20.0)
	turtle.hideturtle() 
	turtle.setup(1000, 600)
	turtle.title('中秋和皮卡丘一起赏月~')
	turtle.colormode(255)
	turtle.bgcolor((16, 78, 139))
	turtle.speed(10)


'''主函数'''
def main():
	# 初始化
	initTurtle()
	# turtle.bgpic(r'/Users/hyc/Downloads/1579424924755.gif')
	# 画月亮
	drawMoon()
	# 画云
	drawCloud()
	# 画山
	drawMountain()
	# 写诗
	writePoetry()
	turtle.done()


'''run'''
if __name__ == '__main__':
	main()