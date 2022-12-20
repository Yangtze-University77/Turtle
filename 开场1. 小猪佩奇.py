import turtle as t

#GOTO
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
#背景
def bg():
    t.speed(0)
    t.hideturtle()
    goto(-1000,-800)
    t.color("limegreen")
    t.begin_fill()
    t.goto(1000,-800)
    t.goto(1000,0)
    t.goto(-1000,0)
    t.end_fill()
    goto(-1000,800)
    t.color("deepskyblue")
    t.begin_fill()
    t.goto(1000,800)
    t.goto(1000,0)
    t.goto(-1000,0)
    t.end_fill()
    
#圆(鼻子，眼睛，腮红)
def circle(x,y,c1,c2,r):
    goto(x,y)
    t.seth(0)
    t.color(c1,c2)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    
#轮廓
def F(x,y):
    goto(x,y)
    t.color('pink1','pink')
    t.begin_fill()
    t.circle(80,150)
    t.circle(400,20)
    t.circle(42,120)
    t.seth(-30)
    t.fd(7)
    t.seth(-10)
    t.circle(38,135)
    t.circle(38,-133)
    t.seth(-30)
    t.circle(400,11)
    t.seth(-140)
    t.circle(57,125)
    t.circle(300,7)
    t.end_fill()
#耳朵
def E(x,y):
    goto(x,y)
    t.color('pink1','pink')
    t.begin_fill()
    t.seth(50)
    t.circle(60,45)
    t.circle(8,130)
    t.circle(60,45)
    t.end_fill()    
    goto(x+50,y-23)
    t.color('pink1','pink')
    t.begin_fill()
    t.seth(46)
    t.circle(60,45)
    t.circle(8,130)
    t.circle(60,45)
    t.end_fill()
    t.end_fill()
    
#嘴巴
def M(x,y):
    goto(x,y)
    t.seth(0)
    t.color('red')
    t.circle(60,25)
    t.circle(60,-25)
    t.circle(30,-60)
    
#脸
def face(x,y):
    t.seth(0)
    t.pensize(6)
    F(x,y)
    #腮红
    circle(x+34,y+45,'pink1','pink1',28)
    #眼睛
    circle(x-10,y+120,'pink1','white',15)
    circle(x-12,y+130,'black','black',3)
    circle(x-48,y+135,'pink1','white',15)
    circle(x-50,y+145,'black','black',3)
    #二师兄鼻子
    t.pensize(4)
    circle(x-100,y+160,'pink1','pink',7)    
    circle(x-100,y+164,'brown','brown',1)
    circle(x-120,y+160,'pink1','pink',7)
    circle(x-120,y+164,'brown','brown',1)
    #耳朵
    E(x-10,y+175)
    #嘴巴
    M(x-30,y+40)
    
#胳膊
def leg(x,y,a):
    goto(x,y)
    t.seth(a)
    t.color('lightpink')
    t.fd(70)
    t.fd(-20)
    t.left(45)
    t.fd(20)
    t.fd(-20)
    t.right(90)
    t.fd(20)
    
#尾巴
def tail(x,y):
    t.seth(0)
    goto(x,y)    
    t.pensize(7)
    t.circle(30,100)
    t.circle(10,180)
    t.circle(20,160)
    
#身体
def body(x,y):
    t.seth(0)
    t.pensize(7)
    goto(x,y)   #中间
    t.seth(-115)
    t.color("red",('salmon'))
    t.begin_fill()
    t.circle(500,17)
    t.seth(0)
    t.fd(200)
    t.seth(100)
    t.circle(500,17)
    t.end_fill()
    leg(x-14,y-25,165)
    leg(x+120,y-25,15)
    tail(x+145,y-100)

#鞋子
def shoe(x,y):
    t.seth(0)
    t.pensize(7)        
    goto(x,y)       #腿
    t.color("pink")
    t.fd(-10)
    t.pd()
    t.left(90)
    t.fd(12)    
    goto(x,y)       #鞋子
    t.color('gold','yellow')
    t.begin_fill()
    t.seth(0)
    t.fd(-20)
    t.right(90)
    t.fd(15)
    t.left(90)
    t.fd(-15)
    t.circle(-8,-180)
    t.fd(-35)
    t.left(90)
    t.fd(-32)
    t.end_fill()
    
#------------------------------作图--------------------------------------
bg()
body(0,0)
face(61,-13)
#face(100,50)
shoe(30,-153)
shoe(120,-153)
goto(-250,-100)
