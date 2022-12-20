import turtle as t
from random import randrange #引入随机函数randange(start,stop,step)
#意思是在[start,stop]之间生成一个以step为步长的随机整数
#-----------------------------知识点三：使用屏幕事件-----------------------------
#监听turtle.listen(xdummy=None, ydummy=None)设置'焦点'到 TurtleScreen (以便接收按键事件)。
#使用两个 Dummy 参数以便能够传递turtle.listen 给 onclick 方法

#当键盘按下并释放t.onkey(),turtle.onkeyrelease(fun, key)
#fun -- 一个无参数的函数或 `None` 
#key -- 一个字符串: 键 (例如 "a") 或键标 (例如 "space")绑定 fun 指定的函数到按键释放事件。
#如果 fun 值为 `None`，则移除事件绑定。注: 为了能够注册按键事件，TurtleScreen 必须得到焦点。
#例：
'''
def f():
    t.fd(50)
    t.lt(60)
t.listen()
t.onkey(f, 'w')
'''

#当键盘按下turtle.onkeypress(fun, key=None)绑定
#fun 指定的函数到指定键的按下事件。如未指定键则绑定到任意键的按下事件。
#注: 为了能够注册按键事件，必须得到'焦点'。

#当点击屏幕turtle.onscreenclick(fun, btn=1, add=None)
#fun -- 一个函数，调用时将传入两个参数表示在画布上点击的坐标。
#btn -- 鼠标按钮编号，默认值为 1 (鼠标左键) 2(中键) 3(右键)
#add -- `True` 或 `False` -- 如为 `True` 则将添加一个新绑定，否则将取代先前的绑定
#绑定 fun 指定的函数到鼠标点击屏幕事件。如果 fun 值为 `None`，则移除现有的绑定。
#备注：此 TurtleScreen 方法作为全局函数时只有一个名字 `onscreenclick`。
#全局函数 `onclick` 所对应的是 Turtle 方法 `onclick`。

#当达到定时turtle.ontimer(fun, t=0)fun -- 一个无参数的函数 t -- 一个数值 >= 0
#安装一个计时器，在 t 毫秒后调用 fun 函数。
#例：
'''
a=True
def f():
    if a:
        t.fd(50)
        t.lt(60)
        t.ontimer(f, 10)
f()
'''
#主循环turtle.mainloop()turtle.done()开始事件循环 - 调用 Tkinter 的 mainloop 函数。
#必须作为一个海龟绘图程序的结束语句。






