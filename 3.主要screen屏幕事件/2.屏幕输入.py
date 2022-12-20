import turtle as t
import time,random
#--------------------------------知识点----------------------------------------
#文本输入turtle.textinput(title, prompt)
#作用：弹出一个对话框窗口用来输入一个字符串。
#title 为对话框窗口的标题
#prompt 为一条文本，通常用来提示要输入什么信息。
#返回输入的字符串。如果对话框被取消则返回 `None`。

#数字输入turtle.numinput(title,prompt,default=None, minval=None, maxval=None)
#作用：弹出一个对话框窗口以输入数字。
#标题(title)是对话框窗口的标题，
#提示(prompt)是主要描述要输入哪些数字信息的文本。
#默认值(default)：默认值，
#最小值(minval)：输入的最小值
#最大值(maxval)：输入的最大值数字输入必须在最小值范围内。
#如果给出这些，则为maxval。否则，将发出提示，并且对话框保持打开状态以进行更正。
#返回数字输入。如果对话框被取消，则返回`None`.
#实例一：
'''
t.shape("turtle")
direction = t.textinput('你要前进多少', '请告诉我距离')
print(direction)
number    = t.numinput('number show', 'give a number', 100, 1, 100)
print(number)
t.fd(number)
t.done()
''
#实例二：
'''
t.pu()
t.goto(450,random.randint(0,300))
speed=random.randint(1,10)
text = t.textinput('弹幕内容', '请输入弹幕内容')#文本输入turtle.textinput(标题，提示文本)
size = t.numinput('弹幕字号', '请输入弹幕字号',None,10,100)   #数字输入turtle.numinput(标题，提示文本，默认值，最小值，最大值)
t.color(t.textinput('弹幕颜色', '请输入弹幕颜色（English）'))

while True:
    if t.xcor()>-600:
        t.clear()
        t.write(text,align=('right'),font=('隶书',int(size)))
        t.goto(t.xcor()-speed,t.ycor())
        time.sleep(0.01)
    else:
        break
t.tracer(1)


