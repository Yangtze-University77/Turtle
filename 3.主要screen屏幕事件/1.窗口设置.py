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
'''
t.setup(420,420,0,0)
'''
#(5)获取窗口高度和宽度
#窗口高度turtle.window_height()返回海龟窗口的高度。
#窗口宽度turtle.window_width()返回海龟窗口的宽度。
#例：
'''
print(t.window_height())
print(t.window_width())
'''
#(6)设置世界坐标系turtle.setworldcoordinates(llx, lly, urx, ury)
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
#t.reset()

t.mode( "world")
t.setworldcoordinates(-200,-200,200,200)

for _ in range(8):
    t.left(45)
    t.fd(20)
'''



