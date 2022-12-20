import turtle as t
import time
import random as r

shp=t.getshapes()
#print(shp)
#['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
t.colormode(255)
t.pensize(5)
t.screensize(800,900)
t.shape(shp[-1])
t.pu()
t.ht()
t.goto(-500,500)
t.st()
for i in range(1,10):
    t.tilt(i*8)
    t.shapesize((10-i)*2.5,(10-i)*2.5)
    t.goto(t.xcor()+45,t.ycor()-65)
for i in range(1,10):
    time.sleep(0.5)
    t.shapesize(i*2.5,i*2.5)
    R=r.randint(1,255)
    J=r.randint(1,255)
    B=r.randint(1,255)
    t.color(R,J,B)
    t.tilt(i*2)
time.sleep(2)
for i in range(1,15):
    t.tilt(i*9)
    t.shapesize((15-i)*2.5,(15-i)*2.5)
    t.goto(t.xcor()+50,t.ycor()+40)
