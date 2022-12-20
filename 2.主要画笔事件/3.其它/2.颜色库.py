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
#---------------------------------------------------------------------------
#turtle.colormode(cmode=None)
#t.colormode(255)
#参数cmode -- 数值 1.0到255 其中之一
#turtle.pencolor('red') 
#turtle.pencolor('#ff0000')#(255,0,0)十六进制转换的
for i in range(1,10):
    time.sleep(0.5)
    t.shapesize(i*2.5,i*2.5)
    R=r.randint(0,255)
    G=r.randint(0,255)
    B=r.randint(0,255)
    t.color(R,G,B)
    print(R,G,B)
