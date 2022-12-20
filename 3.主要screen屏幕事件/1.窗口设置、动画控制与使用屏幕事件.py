import turtle as t
from random import randrange #引入随机函数randange(start,stop,step)
#意思是在[start,stop]之间生成一个以step为步长的随机整数

#-----------------------------知识点一：窗口设置--------------------------------
#1.背景
#(1)背景颜色turtle.bgcolor(args)
#args -- 一个颜色字符串或三个取值范围
#0..colormode 内的数值或一个取值范围相同的数值3元组
#例：
#t.bgcolor('red')

#(2)背景图片turtle.bgpic(picname=None)
#picname -- 一个字符串, gif-文件名, `"nopic"`, 或 `None`
#例：
#t.bgpic('迷宫图.gif')

#(3)清屏turtle.clear()     clearscreen()clear()
#clearscreen()     从中删除所有海龟的全部绘图。
#将已清空的 TurtleScreen 重置为初始状态: 白色背景，无背景片，无事件绑定并启用追踪。
#将屏幕上的所有海龟重置为初始状态turtle.resetscreen()`
#备注:此 TurtleScreen 方法作为全局函数时只有一个名字 `resetscreen`。
#全局函数 `reset` 所对应的是 Turtle 方法 `reset`。`

#(3)屏幕大小turtle.screensize(canvwidth=None, canvheight=None, bg=None)
#canvwidth -- 正整型数，以像素表示画布的新宽度值
#canvheight -- 正整型数，以像素表示画面的新高度值
#bg -- 颜色字符串或颜色元组，新的背景颜色
#如未指定任何参数，则返回当前的 (canvaswidth, canvasheight)。
#否则改变作为海龟绘图场所的画布大小。不改变绘图窗口。
#要观察画布的隐藏区域，可以使用滚动条。
#通过此方法可以令之前绘制于画布之外的图形变为可见。
#注：画布大小不小于窗口大小，如小于则为窗口大小
#例：
'''
print(t.screensize())
t.screensize(2000,1000,'red')
t.fd(1000)
print(t.screensize())
'''
#(4)#turtle.setup（width,height,startx,starty)
#作用：设置主窗体的大小和位置。
#width：窗口宽度，如果值是整数，表示像素(其实也就是距离)值；如果值是小数，表示窗口宽度与屏幕的比例。
#height：窗口高度，如果值是整数，表示像素值；如果值是小数，表示窗口高度与屏幕的比例。
#startx：窗口左侧与屏幕左侧的像素距离，如果值是None，窗口位于屏幕水平中央。
#starty：窗口顶部与屏幕顶部的像素距离，如果值是None，窗口位于屏幕垂直中央。
#左侧和右侧分别指的是海龟图的上侧与下侧

#例：
#t.setup(420,420,0,0)


#(5)设置世界坐标系turtle.setworldcoordinates(llx, lly, urx, ury)
#llx一个数值，画布左下角的x坐标
#lly一个数值，画布左下角的y坐标
#urx一个数值，画布右上角的x坐标
#ury一个数值，画布右上角的y坐标
#设置用户自定义坐标系并在必要时切换模式为 "world"。这会执行一次 `screen.reset()`。
#如果 "world" 模式已激活，则所有图形将根据新的坐标系重绘。
#补充：海龟模式turtle.mode()
#设置海龟模式 ("standard", "logo" 或 "world") 并执行重置。
#如未指定模式则返回当前的模式。
#"standard" 模式与旧的turtle 兼容。
#"logo" 模式与大部分 Logo 海龟绘图兼容。模式
#"standard"初始海龟朝向朝右 正数角度(东)逆时针
#"logo"初始海龟朝向朝上 正数角度(北)顺时针
#"world" 模式使用用户自定义的 "世界坐标系"。
#注意**: 在此模式下，如果 `x/y` 单位比率不等于 1 则角度会显得扭曲。
#例：
'''
for _ in range(8):
    t.left(45)
    t.fd(20)
t.reset()
t.mode( "world")
t.setworldcoordinates(-200,-200,200,200)

for _ in range(8):
    t.left(45)
    t.fd(20)
'''
#-----------------------------知识点二：动画控制--------------------------------
#延迟turtle.delay(delay=None)设置或返回以毫秒数表示的延迟值
#delay(这约等于连续两次画布刷新的间隔时间。)绘图延迟越长，动画速度越慢。

#追踪turtle.tracer(n=None, delay=None)
#启用/禁用海龟动画并设置刷新图形的延迟时间。
#如果指定 n 值，则只有每第 n 次屏幕刷新会实际执行。
#(可被用来加速复杂图形的绘制。) 如果调用时不带参数，则返回当前保存的 n 值。
#第二个参数设置延迟值

#更新turtle.update() 执行一次 TurtleScreen 刷新。在禁用追踪时使用。
#开启/关闭作图过程展示。
#将tracer()属性调为关闭（False或者0）后，执行作图代码时，窗口并不会出现任何东西，
#保持开始作图之前的画面，直到执行turtle.update()刷新画面。
#图画在后台内存中画好，然后执行刷新命令时，将内存读取到画面窗口中。

#-----------------------------知识点三：使用屏幕事件-----------------------------
#监听turtle.listen(xdummy=None, ydummy=None)设置'焦点'到 TurtleScreen (以便接收按键事件)。
#使用两个 Dummy 参数以便能够传递turtle.listen 给 onclick 方法

#当键盘按下并释放t.onkey(),turtle.onkeyrelease(fun, key)
#fun -- 一个无参数的函数或 `None` 
#key -- 一个字符串: 键 (例如 "a") 或键标 (例如 "space")绑定 fun 指定的函数到按键释放事件。
#如果 fun 值为 `None`，则移除事件绑定。注: 为了能够注册按键事件，TurtleScreen 必须得到焦点。

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
    
#主循环turtle.mainloop()turtle.done()开始事件循环 - 调用 Tkinter 的 mainloop 函数。
#必须作为一个海龟绘图程序的结束语句。


#例1——五子棋
'''
import turtle as t
t1,t2=t.Pen(),t.Pen() #2只画笔的设置
t.ht();t1.ht();t2.ht()
t.pensize(4) 
t.bgcolor("pink") #背景颜色
t.tracer(0)  #不显示海龟
locate=[[],[]]  #建立一个空列表,第一个装世界横坐标,第二个纵坐标
#-------------------------
for i in range(35):
    locate[1].append(445-60*i)
    t.up();t.goto(-1000,445-60*i);t.down()
    t.goto(1000,445-60*i)
for i in range(35):
    locate[0].append(-1000+60*i)
    t.up();t.goto(-1000+60*i,455);t.down()
    t.goto(-1000+60*i,-455)
t.tracer(1) #最后显示海龟
#-------------------------
def t11(x,y):
    ls=[[],[]]         #根据两点距离的几何意义(绝对值)判断距离
    l=int(x);t=int(y)  #因为onscreenclilk返回的数为浮点,因此需要转化
    for k in range(35):#添加距离,让棋子落到最近点
        ls[0].append([abs(l-locate[0][k]),locate[0][k]])#添加locate[0][k]是为了最后导出最近点
        ls[1].append([abs(t-locate[1][k]),locate[1][k]])
    #print(ls[0])      #测试使用
    #高级选择法排序,将最小的绝对值排到最前面方便最后的输出
    for i in range(34):
        j=i
        k=i
        for a in range(i+1,35):
            if(ls[0][j][0]>ls[0][a][0]):
                j=a
            if(ls[1][k][0]>ls[1][a][0]):
                k=a
        if j!=i:
            ls[0][i],ls[0][j]=ls[0][j],ls[0][i]
            ls[1][i],ls[1][k]=ls[1][k],ls[1][i]
    #print(ls[1])
    t1.up();
    t1.goto(ls[0][0][1],ls[1][0][1]) #因为最前面就是最近点,直接导出就行
    t1.dot(60,"black")               #以海龟坐标为圆心画直径为60的圆
def t22(x,y):
    ls=[[],[]]
    l=int(x);t=int(y)
    for k in range(35):
        ls[0].append([abs(l-locate[0][k]),locate[0][k]])
        ls[1].append([abs(t-locate[1][k]),locate[1][k]])
    #print(ls[0])
    #高级选择法排序
    for i in range(34):
        j=i
        k=i
        for a in range(i+1,35):
            if(ls[0][j][0]>ls[0][a][0]):
                j=a
            if(ls[1][k][0]>ls[1][a][0]):
                k=a
        if j!=i:
            ls[0][i],ls[0][j]=ls[0][j],ls[0][i]
            ls[1][i],ls[1][k]=ls[1][k],ls[1][i]
    #print(ls[1])
    t2.up();
    t2.goto(ls[0][0][1],ls[1][0][1])
    t2.dot(60,"white")
t.onscreenclick(t11,1)
t.onscreenclick(t22,3)
'''
#例2.——贪吃蛇

'''
#def 
def square(x,y,size,color_name): #square目的是为了画苹果和蛇,蛇是有多个正方形链接而成
    t.up()
    t.goto(x,y)
    t.color(color_name)
    t.begin_fill() 
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.end_fill()
t.hideturtle() 
snack=[[0,0],[10,0],[20,0],[30,0]]#规定初始蛇的串联坐标

apple_x=randrange(-20,20)*10 #规定苹果的坐标,随机出现
apple_y=randrange(-20,20)*10
aim_x=0#蛇身体改变的控制坐标
aim_y=10
def change(x,y):
    global aim_x,aim_y #用全局变量时时改变蛇的位置状态
    aim_x=x
    aim_y=y
def inside():
    if -210<=snack[-1][0]<=200 and -210<=snack[-1][1]<210 : #规定界，出界蛇消失,游戏结束
        return True
    else:
        ('GAMEOVER')
        return False
def gameLoop ():
    global apple_x,apple_y #全局变量改变苹果位置,使苹果被吃掉后能再出现
    t.clear()
    snack.append([snack[-1][0]+aim_x,snack[-1][1]+aim_y]) #将数据加入蛇的身体列表中
#在此说明蛇吃苹果原理:他会先把x,y引入列表,然后删除列表第一位数组,一直这样循环往复,
#如果吃到苹果就不会删除,吃不到就会删除,但是吃不到苹果时，引入的数组和删除的相互抵消,
#长度不变,吃到苹果后长度增加,蛇的长度以及位置变化主要由:
#1.snack.append([snack[-1][0]+aim_x,snack[-1][1]+aim_y])  2.snack.pop(0) 3.square(snack[n][0],snack[n][1],10,"black")
#这三部分组成
    if not inside(): #可蛇是否可见
        return
    if snack[-1][0]!=apple_x or snack[-1][1]!=apple_y :
        snack.pop(0) #pop是列表中的删除函数,删除第0个位置的数组
    else:
        apple_x=randrange(-20,20)*10 #随机产生苹果
        apple_y=randrange(-20,20)*10
    for n in range(len(snack)): #改变蛇的长度和位置
        square(snack[n][0],snack[n][1],10,"black")
        #这里是用正方形组连成蛇的身体
    square(apple_x,apple_y,10,"red")
    t.ontimer(gameLoop,200)#延迟200毫秒后执行
    t.update()             #
 
#t.setup(420,420,0,0) #setup意思是建立画布的大小
#turtle.setup（width,height,startx,starty)
#作用：设置主窗体的大小和位置。
#width：窗口宽度，如果值是整数，表示像素(其实也就是距离)值；如果值是小数，表示窗口宽度与屏幕的比例。
#height：窗口高度，如果值是整数，表示像素值；如果值是小数，表示窗口高度与屏幕的比例。
#startx：窗口左侧与屏幕左侧的像素距离，如果值是None，窗口位于屏幕水平中央。
#starty：窗口顶部与屏幕顶部的像素距离，如果值是None，窗口位于屏幕垂直中央。
#左侧和右侧分别指的是海龟图的上侧与下侧

t.tracer(False) #这里False 与True 其实就是我们平常用的1 和 0
t.listen()#listen的功能就是让以下的onkey案件可以发生使turtle程序可以接受按键发送的指令

#lambda的定义是定义一个匿名表达式,例如lambda a,b:a+b,就是返回a+b的一个值
#lambda可以用于简单函数的打包（其内容只能有一个代码块)
#关于onkey中为什么要用lambda是因为当一个打包程序中存在变量时(f(x)中的x即为变量)
#onkey中的第一个变量无法识别,也就是无法返回其内容,这时候就要借助lambda返回结果
t.onkey(lambda :change(0,10),"w")
t.onkey(lambda :change(0,-10),"s")
t.onkey(lambda :change(10,0),"d")
t.onkey(lambda :change(-10,0),"a")
#onkey的解释:onkey()必须要搭配listen进行使用,onkey(funcation,key)
#funcation就是你定义的按键函数,意思就是按键之后该怎么运行
#key就是你需要设置的按键
gameLoop()

'''



