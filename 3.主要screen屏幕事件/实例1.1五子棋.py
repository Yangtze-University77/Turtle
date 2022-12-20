#简易五子棋模型
#知识点:t.dot(size=None,"color")
#绘制一个直径为 size，颜色为 color 的圆点。
#如果 size 未指定，则直径取 pensize+4 和 2*pensize 中的较大值。
#---------------------------
##onscreenclick(x,y,z),x是一个函数点击屏幕运行一次
#y是点击鼠标的位置,1是左键,2是滑轮,3是右键
#-----------背景图----------
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
