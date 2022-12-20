import turtle as t
t.bgpic('迷宫图.gif')
#拖动时调用的方法
def fxn(x, y):
    t.ondrag(None) # 停止回溯     
    t.setheading(t.towards(x, y))#移动乌龟的角度和方向朝向x和y  
    t.goto(x, y)
    t.ondrag(fxn)#再次调用，如没有则只能拖一下

t.speed(0)
t.color('red','blue')
t.pensize(10)
t.penup()
t.shape('turtle')
t.shapesize(1.4)
t.goto(-380,366)
t.ondrag(fxn)#调用函数


