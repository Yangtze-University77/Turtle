import turtle as t
  
#---------------------函数--------------------- 
def fxn1(x,y):
   t.fillcolor("blue") 
def fxn2(x,y):
   t.fillcolor("white") 
#t.setup(400,300) 
t.shape("turtle") 
t.turtlesize(5) 
t.speed(1)  
#点击发生事件 
t.onclick(fxn1)  
#松开发生事件
t.onrelease(fxn2)

#----------------------知识点-----------------------------
'''
(1)turtle.onclick(fun, btn=1, add=None)
    fun – 一个函数，调用时将传入两个参数表示在画布上点击的坐标。
    btn – 鼠标按钮编号，默认值为 1 (鼠标左键)
    add – True 或 False – 如为 True 则将添加一个新绑定，否则将取代先前的绑定

    将 fun 指定的函数绑定到鼠标点击此海龟事件。
    如果 fun 值为 None，则移除现有的绑定。

    注意: a.fun定义的函数中必须要有x和y两个变量
          b.只有点击海龟时该点击事件才会触发
(2)turtle.onrelease(fun, btn=1, add=None)

    fun – 一个函数，调用时将传入两个参数表示在画布上点击的坐标。
    btn – 鼠标按钮编号，默认值为 1 (鼠标左键)
    add – True 或 False – 如为 True 则将添加一个新绑定，否则将取代先前的绑定

    将 fun 指定的函数绑定到在此海龟上释放鼠标按键事件。
    如果 fun 值为 None，则移除现有的绑定。

(3)turtle.ondrag(fun, btn=1, add=None)

    fun – 一个函数，调用时将传入两个参数表示在画布上点击的坐标。
    btn – 鼠标按钮编号，默认值为 1 (鼠标左键)
    add – True 或 False – 如为 True 则将添加一个新绑定，否则将取代先前的绑定

    将 fun 指定的函数绑定到在此海龟上移动鼠标事件。
    如果 fun 值为 None，则移除现有的绑定。

    注: 在海龟上移动鼠标事件之前应先发生在此海龟上点击鼠标事件。
'''
#-----------------------------------------------------------------------------
'''
#例：
import turtle
from turtle import Turtle


class MyTurtle(Turtle):
    def look_back(self, x, y):
        turtle.left(180)
        turtle.forward(100)

    def look_left(self, x, y):
        turtle.right(90)
        turtle.forward(100)

    def go_back(x,y):
        turtle.goto(x,y)


my_turtle = MyTurtle()
turtle.shape("turtle")
turtle.onclick(fun=my_turtle.look_back, btn=1, add=True)
turtle.onrelease(fun=my_turtle.look_left, btn=1, add=True)
turtle.ondrag(fun=my_turtle.go_back, btn=1, add=True)

turtle.done()
'''







