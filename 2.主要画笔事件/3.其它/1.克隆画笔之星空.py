import turtle as t
import random as r
#-------------------------知识点------------------------------
#t.clone()
#克隆创建并返回海龟的克隆体，具有相同的位置、朝向和海龟属性。
t.reset()
#从屏幕中删除海龟的绘图，海龟回到原点并设置所有变量为默认值。
#-----------------------------------------------------------------------------
width ,height = 800,600
#t.setup(width,height)
#t.title("星汉西流夜未央")
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

t.reset()
t.goto(0,-22)
t.left(100)
print(t.position())#获取画笔位置
print(t.heading())
t.reset()
print(t.position())
print(t.heading())

while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor()<-width/2:
            star.hideturtle()
            star.setx(width/2 + r.randint(1,width))
            star.sety( r.randint(-height/2,height/2))
            star.showturtle()
    
