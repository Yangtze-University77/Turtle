#弹幕大师
import turtle,time,random
t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11=turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen()
turtle.hideturtle()
turtle.tracer(0)

#数据列表
file=open('conf.txt','r')
tx=file.read().split()
print(tx)
color=['red','black','blue','yellow','purple','orange','pink','gold','green','lime']
pen=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
txt=['','','','','','','','','','']
t_s=['','','','','','','','','','']
t_sp=['','','','','','','','','','']                                
file.close()

#设定笔的格式
for i  in range(len(pen)):
    txt[i]=tx[random.randint(0,len(tx)-1)]                                      #随机一条弹幕
    t_c=pen[i].color(color[random.randint(0,len(color)-1)])         #随机颜色
    pen[i].goto(random.randint(-400,400),random.randint(0,300))
    t_s[i]=random.randint(15,50)                                                    #随机大小          
    t_sp[i]=random.randint(25,40)                                                    #随机速度
#自定义弹幕
def danmu(x,y):
    t11.goto(450,random.randint(0,300))
    speed=random.randint(1,10)
    text = turtle.textinput('弹幕内容', '请输入弹幕内容')                         #文本输入
    size = turtle.numinput('弹幕字号', '请输入弹幕字号',None,10,100)   #数字输入
    t11.color(turtle.textinput('弹幕颜色', '请输入弹幕颜色（English）'))
    while True:
        #写字幕
        for i in range(len(pen)):
            t11.clear()
            pen[i].clear()
            pen[i].write(txt[i],align=('right'),font=('隶书',t_s[i]))
            #当手动输入弹幕的运行
            t11.write(text,align=('right'),font=('隶书',int(size)))
            time.sleep(0.01)
        #移动与刷新位置
        for i in range(len(pen)):
            if pen[i].xcor()>-600:                         
                pen[i].goto(pen[i].xcor()-t_sp[i],pen[i].ycor())

                #自定义弹幕的移动
                t11.goto(t11.xcor()-speed,t11.ycor())
            else:
                pen[i].goto(800,random.randint(50,300))
                #重新设置字幕，大小，速度
                txt[i]=tx[random.randint(0,len(tx)-1)]
                t_s[i]=random.randint(15,50)                                                             
                t_sp[i]=random.randint(5,20)
#点击调用弹幕函数
turtle.onscreenclick(danmu)            

    
