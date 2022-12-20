import turtle as t
#1.退出
#退出turtle.bye()
#当点击时退出  turtle.exitonclick()
'''
t.fd(100)
t.bye()
#t.exitonclick()
'''
#2.标题
#标题turtle.title(*titlestring*)
#titlestring-- 一个字符串，显示为海龟绘图窗口的标题栏文本
#设置海龟窗口标题为 titlestring 指定的文本。
'''
import turtle as t
import random as r
#--------------------------------------
width ,height = 800,600
#t.setup(width,height)
t.title("星汉西流夜未央")#标题
t.bgcolor("black")
#t.mode("logo")
t.delay(0)              #这里要设为0，否则很卡
t.shape('circle')
t.pencolor("blue")
t.fillcolor("white")
#t.shapesize(10)
t.penup()
t.setheading(-90)
t.goto(width/2,r.randint(-height/2,height/2))
stars = []
for i in range(200):
    star = t.clone()
    s =r.random()/3    
    star.shapesize(s,s)
    star.speed(int(s*10))
    star.setx(width/2 + r.randint(1,width))
    star.sety(r.randint(-height/2,height/2))
    star.showturtle()
    stars.append(star) 
while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor()<-width/2:
            star.hideturtle()
            star.setx(width/2 + r.randint(1,width))
            star.sety( r.randint(-height/2,height/2))
            star.showturtle()
'''

















