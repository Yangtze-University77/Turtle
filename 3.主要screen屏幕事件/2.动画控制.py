import turtle as t

#-----------------------------知识点二：动画控制--------------------------------
#延迟turtle.delay(delay=None)设置或返回以毫秒数表示的延迟值
#delay(这约等于连续两次画布刷新的间隔时间。)绘图延迟越长，动画速度越慢。

#追踪turtle.tracer(n=None, delay=None)
#启用/禁用海龟动画并设置刷新图形的延迟时间。
#如果指定 n 值，则只有每第 n 次屏幕刷新会实际执行。
#(可被用来加速复杂图形的绘制。) 如果调用时不带参数，则返回当前保存的 n 值。
#第二个参数设置延迟值
#例：
'''
#t.tracer(8, 25)
#t.tracer(1,250)
#t.tracer(1, 0)
t.delay(100)
dist = 2
for i in range(200):
    t.fd(dist)
    t.rt(90)
    dist += 2
    print(dist)
'''
#更新turtle.update() 执行一次 TurtleScreen 刷新。在禁用追踪时使用。
#开启/关闭作图过程展示。
#将tracer()属性调为关闭（False或者0）后，执行作图代码时，窗口并不会出现任何东西，
#保持开始作图之前的画面，直到执行turtle.update()刷新画面。
#图画在后台内存中画好，然后执行刷新命令时，将内存读取到画面窗口中。
'''
t.tracer(0)
dist = 2
for i in range(200):
    t.fd(dist)
    t.rt(90)
    dist += 2
    print(dist)
    if i%50==0:
        t.update()
'''



