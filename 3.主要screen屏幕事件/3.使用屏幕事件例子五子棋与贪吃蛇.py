import turtle as t
from random import randrange #引入随机函数randange(start,stop,step)

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
'''
#例2.——贪吃蛇
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
    t.update()             
 
#t.setup(420,420,300,300) #setup意思是建立画布的大小
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

