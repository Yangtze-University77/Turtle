import turtle as t
import time
import random as r

#--------------------------印章与撤销---------------------------------------
#印章——turtle.stamp()
#(1)turtle.stamp()  在海龟当前位置印制一个海龟形状。返回该印章的 stamp_id
#(2)turtle.clearstamp(stampid),删除stampid指定的印章
#   参数：stampid-- 一个整型数，必须是之前 stampid 指定的印章。
#(3)turtle.clearstamps(n=None)删除全部或前/后n个海龟印章。如果n为 `None`
#   则删除全部印章，如果n>0则删除前n个印章，否则如果 n<0 则删除后n个印章。
'''
shp=t.getshapes()
for i in range(7):
    t.shape(shp[i])
    id=t.stamp()
    t.fd(100)
    t.left(180-180*5/7)

t.fd(100)
#t.clearstamp(id)

t.clearstamps()
for i in range(7*3+1):
    t.undo()
'''
#撤销——turtle.undo()
#(1)turtle.undo(),撤消(或连续撤消)最近的一个 (或多个) 海龟动作。
#   可撤消的次数由撤消缓冲区的大小决定。
#(2)设置撤销缓冲区——turtle.setundobuffer(size)设置或禁用撤销缓冲区。
#   如果size为整数，则开辟一个给定大小的空撤销缓冲区。
#   size 给出了可以通过 undo()方法/函数撤销海龟动作的最大次数。
#   如果size为None则禁用撤销缓冲区。
#(3)返回撤销缓冲区里的条目数turtle.undobufferentries()
#例：
'''
t.speed(10)
#t.setundobuffer(20)
print(t.undobufferentries())
for i in range(50):
    t.fd(10+i*3)
    t.left(90)
print(t.undobufferentries())
#t.setundobuffer(None)

print(t.undobufferentries())
for i in range(t.undobufferentries()):
    t.undo()
'''

#-------------------画笔——海龟-------------------------
'''
#(1)海龟内置图形
shp=t.getshapes()
print(shp)
#['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
t.pensize(4)
for i in range(len(shp)):
    t.speed(8)
    t.shape(shp[i])#上面的名字
    t.circle(60)
    t.clear()
    print(t.get_shapepoly())
    time.sleep(0)

''' 

#(2)海龟外观改变
#a.形状
#   turtle.shape(name=None)
#   name -- 一个有效的形状名字符串，如上
#b.大小调整模式
#   turtle.resizemode(rmode=None)
#
#   rmode -- 字符串 "auto", "user", "noresize"
#   其中之一设置大小调整模式为以下值之一: "auto", "user", "noresize"。
#   如未指定rmode则返回当前的大小调整模式，不同的大小调整模式的效果如下:
#   "auto": 根据画笔粗细值调整海龟的外观。
#   "user": 根据拉伸因子和轮廓宽度 (outline) 值调整海龟的外观，两者是由 shapesize() 设置的。
#   "noresize": 不调整海龟的外观大小。                                                                                      "**user**": 根据拉伸因子和轮廓宽度 (outline) 值调整海龟的外观，两者是由 `shapesize()`设置的。                                                                                                                                                      "**noresize**": 不调整海龟的外观大小。
#   注：resizemode("user") 会由shapesize()带参数使用时被调用。
#例如：-----------------------
'''
t.resizemode('noresize')
t.pensize(5)
t.fd(100)

t.resizemode('auto')
t.pensize(20)
t.fd(100)
'''
#-------------------------------------------------------------------------------
#c.形状大小
#   turtle.shapesize(stretch_wid=None,stretch_len=None,outline=None*)
#
#   返回或设置画笔的属性 x/y-拉伸因子和/或轮廓。设置大小调整模式为 "user"。
#   当且仅当大小调整模式设为 "user" 时海龟会基于其拉伸因子调整外观:
#   stretch_wid为垂直于其朝向的宽度拉伸因子，
#   stretch_len为平等于其朝向的长度拉伸因子，决定形状轮廓线的粗细
#   outline确定形状轮廓的宽度
#例如：------------------------
'''
print(t.shapesize())
t.shape('turtle')
#t.shape('circle')
t.resizemode('user')
t.color('red','blue')
t.shapesize(5,5,5)
t.shapesize(5,10,1)
t.shapesize(10,5,1)
t.shapesize(5,5,5)
'''
#---------------------------------------------------------------------------------
#d.倾角
#   turtle.tiltangle(angle=None)
#
#   设置或返回当前的倾角。
#   如果指定 angle 则旋转海龟形状使其指向 angle 指定的方向，忽略其当前的倾角。
#   不改变海龟的朝向 (移动方向)。
#   如果未指定angle: 返回当前的倾角，
#                    即海龟形状的方向和海龟朝向 (移动方向) 之间的夹角。
'''
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
'''
#e.变形
#   turtle.shapetransform(t11=None,t12=None,t21=None,t22=None)
#
#   设置或返回海龟形状的当前变形矩阵。如未指定任何矩阵元素，
#   则返回以 4 元素元组表示的变形矩阵。 否则就根据设置指定元素的矩阵来改变海龟形状，
#   矩阵第一排的值为 t11, t12 而第二排的值为 t21, t22。
#   行列式 t11 * t22 - t12 * t21 必须不为零，否则会引发错误。
#   根据指定矩阵修改拉伸因子 stretchfactor, 剪切因子 shearfactor 和倾角 tiltangle。

#(3)获取多边形
#a.turtle.get_shapepoly()
#返回以坐标值对元组表示的当前形状多边形。
#这可以用于定义一个新形状或一个复合形状的多个组成部分。

#一、开始记录多边形 turtle.begin_poly()
#   开始记录多边形的顶点。当前海龟位置为多边形的第一个顶点。

#二、结束记录多边形 turtle.end_poly()
#   停止记录多边形的顶点。当前海龟位置为多边形的最后一个顶点。
#   它将连线到第一个顶点。

#三、获取多边形 turtle.get_poly()
#   返回最新记录的多边形。
#四、注册/添加形状register_shape(name,shape)
#调用此函数有三种不同方式:
#   1.name为指定的字符串，shape为由坐标值对构成的元组:安装相应的多边形形状。

#   2.name 是任意字符串，形状是（复合）形状对象：安装相应的复合形状。
#   turtle.Shape(type_, data)
#参数type_ -- 字符串 "polygon", "image", "compound" 其中之一实现形状的数据结构。
#`(type_, data)` 必须遵循以下定义:
#   type                                        data
#"polygon"          一个多边形元组，即由坐标值对构成的元组                       
#"image"              一个图片 (此形式仅限内部使用!)                               
#"compound"      `None` (复合形状必须使用addcomponent()方法来构建) 

#   3.name为一个 gif 文件的文件名，shape为None: 安装相应的图像形状。
#   备注：当海龟转向时图像形状 *不会* 转动，因此无法显示海龟的朝向!   
#例如：
#1.五角星
'''
t.begin_poly()
for i in range(5):
    t.fd(40)
    t.left(180-36)
t.end_poly()
t.clear()
t.pu()
a=t.get_poly()
print(a)
t.register_shape('shape1',a)
t.shape('shape1')
t.fd(100)
for i in range(50):
    t.left(20)
'''
#2.复合图形
'''
s = t.Shape("compound")
poly1 = ((0,0),(100,-50),(0,100),(-100,-50))
s.addcomponent(poly1, "red", "blue")
poly2 = ((0,0),(100,-50),(-100,-50))
s.addcomponent(poly2, "blue", "red")
t.register_shape("myshape", s)
t.shape("myshape")
'''
#3.狼羊菜1
'''
t0,t1,t2,t3=t.Pen(),t.Pen(),t.Pen(),t.Pen()

t.register_shape('狼.gif')#注册图形
t.register_shape('羊.gif')
t.register_shape('菜.gif')
t.register_shape('农夫.gif')

t1.shape('狼.gif')#使用
t1.pu()
t1.fd(-300)
t1.fd(600)

t2.pu()
t2.fd(200)
t2.shape('羊.gif')

t3.pu()
t3.fd(-200)
t3.shape('菜.gif')

t0.pu()
t0.left(90)
t0.fd(150)
t0.shape('农夫.gif')
'''
#4.狼羊菜2
'''
#------------画河------------
def river(x,y):
    t.speed(0)
    t.color('deepskyblue')
    t.begin_fill()
    t.goto(x,y)
    t.goto(-x,y)
    t.goto(-x,-y)
    t.goto(x,-y)
    t.goto(x,y)
    t.end_fill()
#-------------移动程序---------
def control(n,x,y):# n为画笔序号  
    p[n].goto(x,y)   
  
#---------------------设定----------------------
#从原岸回对岸    
def go():    
    global index,n#设置全局变量global,每次操作会改变，用于减少重复
    for i in range(3):
        if a[i]==1 and index != i:#先判断是否为在此岸并且不为已移动过的
            a[i]-=1                           #先减去再进行判断是否要带走
            if  not(a[1]==1 and a[0]+a[2]==1):#意思为：如果带走后是可共存状态
                b[i]+=1
                index=i
                print("带走%s"%c[i])
                n+=1
                for j in range(100):        #前进    
                    control(3,X[0]+j*8,Y[i])#船
                    control(i,X[0]+j*8,Y[i])#被选到的东西
                return 1  #如果成功运行则带一个走，返回函数值，因为只能带一个
            else:
                a[i]+=1   #与上面对应相当于先拿出来再判断，如果不行最后再拿回来
    
#从对岸回原岸                
def back():
    global index,n
    if  (b[1]==1 and b[0]+b[2]==1):#判断对岸是否合理，意思为如果为不可共存状态
        for j in range(3):         #那么就带走
            if b[j]==1 and j!=index:
                b[j]-=1 
                a[j]+=1
                index=j
                print("带回%s"%c[j])
                n+=1
                for i in range(100):#后退
                    control(3,X[1]-i*8,Y[j])#船
                    control(j,X[1]-i*8,Y[j])#被选到的事物
    else:
        if b[0]+b[1]+b[2]==3:      #判断对岸是否完成
            print("已全部送到对岸，任务完成")
        else:
            print("独自回去")
#创建存储列表，可在进行移动后显示两岸都有什么
def things(A):
    d=[]
    for i in range (3):
        if A[i]==1:#如果两个列表中有值为1，则把对应的c列表中狼羊菜加入
            d.append(c[i])
    return d   
#----------------------------------主程序----------------------------------------
#-------------初级移动-----------  
river(200,500)
p=[t.Pen() for i in range(4)]#创建画笔
gif=['狼.gif','羊.gif','菜.gif','渔船.gif']#四事物的图像
X=[-400,400]         #四个的横坐标
Y=[-200,0,200,0]#四个的纵坐标
for i in range(4):#设置画笔形状为四种图像
    t.register_shape(gif[i])
    p[i].shape(gif[i])
    p[i].pu()
    p[i].goto(X[0],Y[i])    
#-------------初始赋值-----------
#分别为狼羊菜状态，0变1为过河了
a=[1,1,1,1]#原岸
b=[0,0,0,0]#对岸
c=['狼','羊','菜']#建立狼羊菜用于后面print
index=0#作为指示值，并在下面设置全局变量global减少重复
n=-1   #用于计算走了多少步
#-------------运行程序-----------------
while True:#完成条件：b[0]+b[1]+b[2]==3前一直循环
    print("原岸上有",things(a),end=' ')
    print("对岸上有",things(b))
    go()
    back()
    if b[0]+b[1]+b[2]==3:
        break
print("一共需要",n,"步")
'''
