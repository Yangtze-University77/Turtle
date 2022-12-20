## turtle——Python海龟绘图

### 一、介绍turtle

turtle最初来自于 Wally Feurzeig, Seymour Papert 和 Cynthia Solomon 于 1967 年所创造的 Logo 编程语言。

### 二、引用turtle库

**引用turtle库的一个函数并设函数参数**

```python 
import turtle 
turtle.fd(20) 

import turtle as t #将turtle库用t代指
t.fd(20)

from turtle import*
fd(20)
```



## 玩转turtle库

### 一、认识turtle库

turtle（海龟）是Python重要的标准库之一，它能够进行基本的图形绘制，其概念诞生于1969年。turtle是最有价值的程序设计入门实践库,它是程序设计入门层面最常用的基本绘图库。

#### turtle的绘图原理：

1. 有一只海龟处于画布正中心，由程序控制在画布上游走；
2. 海龟走过的轨迹形成了绘制的图形
3. 海龟由程序控制，可改变其大小，颜色等

### 二、函数

### Turtle 方法

#### 1. 海龟动作

##### 	1.1. 移动和绘制



|    描述    | 函数                                                         | 注释                                                         |
| :--------: | :----------------------------------------------------------- | :----------------------------------------------------------- |
|    前进    | turtle.**forward**(*distance*)<br />turtle.**fd**(*distance*) | 沿画笔方向前进**distance****<br />**参数：**distance**  -- 一个数值 (整型或浮点型) |
|    后退    | turtle.**backward**(*distance*)<br />turtle.**bk**(*distance*)<br />turtle.**back**(*distance*) |                                                              |
|    右转    | turtle.**right**(*angle*)<br />turtle.**rt**(*angle*)        | 海龟右转 ***angle*** 个单位。**<br />参数：angle** -- 一个数值 (整型或浮点型)                                                                   (单位默认为角度，但可通过 [`degrees()`](#jump4) 和 [`radians()`](#jump5) 函数改变设置。) 角度的正负由海龟模式确定，参见 [`mode()`](#jump6)。 |
|    左转    | turtle.**left**(*angle*)<br />turtle.**lt**(*angle*)         | 与**right**同理                                              |
| 前往/定位  | turtle.**goto**(*x*, *y=None*)<br />turtle.**setpos**(*x*, *y=None*)<br />turtle.**setposition**(*x*, *y=None*) | <br />**<br />参数：x** -- 一个数值或数值对/向量<br />**参数：y** -- 一个数值或 `None                                    `如果 *y* 为 `None`，*x* 应为一个表示坐标的数值对或 [`Vec2D`](#jump7) 类对象 (例如 [`pos()`](#jump8) 返回的对象). |
| 设置x坐标  | turtle.**setx**(*x*)                                         | 海龟移动到一个绝对坐标。如果画笔已落下将会画线。不改变海龟的朝向。<br />**参数：x** -- 一个数值 (整型或浮点型)                                                             设置海龟的横坐标为 *x*，纵坐标保持不变。 |
| 设置y坐标  | turtle.**sety**(*y*)                                         | 设置海龟的纵坐标为 *y*，横坐标保持不变。                     |
|  画笔朝向  | turtle.**setheading**(*to_angle*)<br />turtle.**seth**(*to_angle*) | **参数：to_angle** -- 代表角度的一个数值 (整型或浮点型)      |
|  返回原点  | turtle.**home**()                                            | 海龟移至初始坐标 (0,0)，并设置朝向为初始方向 (由海龟模式确定，参见 [`mode()`](https://docs.python.org/zh-cn/3/library/turtle.html#turtle.mode)) |
|  画圆或弧  | turtle.**circle**(*radius*, *extent=None*, *steps=None*)     | **参数：radius** -- 一个数值<br />**参数：extent** -- 一个数值 (或 `None`)<br />**参数：steps** -- 一个整型数 (或 `None`)<br />绘制一个 **radius** 指定半径的圆。圆心在海龟左边 **radius**个单位；<br />**extent** 为一个夹角，用来决定绘制圆的一部分。如未指定 **extent**则绘制整个圆。如果 **extent**则以当前画笔位置为一个端点绘制圆弧。<br />如果 ***radius*** 为正值则朝逆时针方向绘制圆弧，否则朝顺时针方向。最终海龟的朝向会依据 **extent** 的值而改变。 |
|   画圆点   | turtle.**dot**(*size=None*, **color*)                        | **参数：size** -- 一个整型数 >= 1 (如果指定)<br />**参数：color** -- 一个颜色字符串或颜色数值元组<br />绘制一个直径为 **size**，颜色为 **color** 的圆点。如果 **size** 未指定，则直径取 **pensize+4** 和 **2*pensize** 中的较大值。 |
|  印海龟章  | turtle.**stamp**()                                           | 在海龟当前位置印制一个海龟形状。返回该印章的 **stamp_id**，印章可以通过调用 **clearstamp(stamp_id)** 来删除。 |
| 删一个印章 | turtle.**clearstamp**(*stampid*)                             | **参数：stampid** -- 一个整型数，必须是之前 stampid 指定的印章。<br />删除 **stampid** 指定的印章。 |
| 删所有印章 | turtle.**clearstamps**(*n=None*)                             | **参数：n** -- 一个整型数 (或 `None`)<br />删除全部或前/后 **n** 个海龟印章。如果 **n** 为 `None` 则删除全部印章，如果 **n** > 0 则删除前 **n** 个印章，否则如果 **n** < 0 则删除后 **n** 个印章。 |
|    撤销    | turtle.**undo**()                                            | 撤消 (或连续撤消) 最近的一个 (或多个) 海龟动作。可撤消的次数由撤消缓冲区的大小决定。 |
|  画笔速度  | turtle.**speed**(*speed=None*)                               | **参数：speed** -- 一个 **0-10** 范围内的整型数或速度字符串 (见下)<br />设置海龟移动的速度为 **0-10** 表示的整型数值。如未指定参数则返回当前速度。<br />如果输入数值大于 10 或小于 0.5 则速度设为 0。速度字符串与速度值的对应关系如下:<br />      "fastest":   0       最快<br />      "fast":       10      快<br />      "normal":  6       正常<br />      "slow":       3       慢<br />      "slowest":  1       最慢<br />速度值从 1 到 10，画线和海龟转向的动画效果逐级加快。<br />**注意**: **speed** = 0 表示 *没有* 动画效果。**forward/back** 将使海龟向前/向后跳跃，同样的 **left/right** 将使海龟立即改变朝向。 |



##### 	1.2 获取海龟状态



|   描述   | 函数                                        | 注释                                                         |
| :------: | :------------------------------------------ | ------------------------------------------------------------ |
|   位置   | turtle.**position**()<br />turtle.**pos**() | 返回海龟当前的坐标 (x,y) (为 [Vec2D](#jump7) 矢量类对象)。   |
| 目标方向 | turtle.**towards**(*x*,*y=None*)            | **参数：x** -- 一个数值或数值对/矢量，或一个海龟实例 <br />**参数：y** -- 一个数值——如果 *x* 是一个数值，否则为 `None`返回从海龟位置到由 (x,y)、矢量或另一海龟所确定位置的连线的夹角。 此数值依赖于海龟的初始朝向，这又取决于 "standard"/"world" 或 "logo" 模式设置。 |
|  x坐标   | turtle.**xcor**()                           | 返回海龟的 x 坐标。                                          |
|  y坐标   | turtle.**ycor**()                           | 返回海龟的 y 坐标。                                          |
|   朝向   | turtle.**heading**()                        | 返回海龟当前的朝向                                           |
|   距离   | turtle.**distance**(*x*,*y=None*)           | **参数：x** -- 一个数值或数值对/矢量，或一个海龟实例 <br />**参数：y** -- 一个数值——如果 *x* 是一个数值，否则为 `None`          返回从海龟位置到由 (x,y)，适量或另一海龟对应位置的单位距离。 |



##### 1.3. 度量单位设置

| 描述 | 函数                                   | 注释                                                         |
| :--: | :------------------------------------- | ------------------------------------------------------------ |
| 角度 | turtle.**degrees**(*fullcircle=360.0*) | **参数：fullcircle** -- 一个数值                                                                                                                        设置角度的度量单位，即设置一个圆周为多少 "度"。默认值为 360 度。 |
| 弧度 | turtle.**radians**()                   | 设置角度的度量单位为弧度。其值等于 `degrees(2*math.pi)`。    |



#### 2. 画笔控制



##### 2.1. 绘图状态

|     描述     | 函数                                                         | 注释                                                         |
| :----------: | :----------------------------------------------------------- | ------------------------------------------------------------ |
|   画笔落下   | turtle.**pendown()**<br />turtle.**pd**()<br />turtle.**down**() | 画笔落下 -- 移动时将画线。                                   |
|   画笔抬起   | turtle.**penup**()<br />turtle.**pu**()<br />turtle.**up**() | 画笔抬起 -- 移动时不画线。                                   |
|   画笔粗细   | turtle.**pensize**(*width=None*)<br />turtle.**width**(*width=None*) | **参数：width** -- 一个正数值                                                                                                                      设置线条的粗细为 **width** 或返回该值。如果 ***resizemode*** 设为 "**auto**" 并且 **turtleshape** 为多边形，该多边形也以同样组细的线条绘制。如未指定参数，则返回当前的 **pensize**。 |
|     画笔     | turtle.**pen**(*pen=None*, ***pendict*)                      | **参数：pen** -- 一个包含部分或全部下列键的字典 **参数：pendict** -- 一个或多个以下列键为关键字的关键字参数<br />返回或设置画笔的属性，以一个包含以下键值对的 "画笔字典" 表示:![image-20221126155247096](https://xingwangyue.oss-cn-hangzhou.aliyuncs.com/yue/image-20221126155247096.png)<br />此字典可作为后续调用 [`pen()`](https://docs.python.org/zh-cn/3/library/turtle.html#turtle.pen) 时的参数，以恢复之前的画笔状态。另外还可将这些属性作为关键词参数提交。使用此方式可以用一条语句设置画笔的多个属性。 |
| 画笔是否落下 | turtle.**isdown**()                                          | 如果画笔落下返回 `True`，如果画笔抬起返回 `False`。          |

##### 2.2. 颜色控制

|   描述   | 函数                      | 注释                                                         |
| :------: | :------------------------ | ------------------------------------------------------------ |
| 画笔颜色 | turtle.**pencolor**()     | **返回或设置画笔颜色。<br />允许以下四种输入格式:**                                                                                       `pencolor()`<br />        返回以颜色描述字符串或元组 (见示例) 表示的当前画笔颜色。可用作其他 **color/pencolor/fillcolor** 调用的输入。                                                                                                                                     `pencolor(colorstring)`<br />设置画笔颜色为 *colorstring* 指定的 Tk 颜色描述字符串，例如 `"red"`、`"yellow"` 或 `"#33cc8c"`。                                                                                                                                                                          `pencolor((r, g, b))`<br />设置画笔颜色为以 ***r*, *g*, *b*** 元组表示的 RGB 颜色。***r*, *g*, *b*** 的取值范围应为**0-colormode**，**colormode** 的值为 1.0 或 255                                                                                                                                           `pencolor(r, g, b)`<br />设置画笔颜色为以 ***r*, *g*, *b*** 表示的 RGB 颜色。***r*, *g*, *b*** 的取值范围应为 **0-colormode**。 |
| 填充颜色 | turtle.**fillcolor**()    | 返回或设置填充颜色。**同上**<br />如果 turtleshape 为多边形，该多边形内部也以新设置的填充颜色填充。 |
| 填充颜色 | turtle.**color**(**args*) | 返回或设置画笔颜色和填充颜色。<br />允许多种输入格式。使用如下 0 至 3 个参数:                                                     `color()`<br />返回以一对颜色描述字符串或元组表示的当前画笔颜色和填充颜色，两者可分别由 `pencolor()`]和 `fillcolor()`返回。                                                                                                                                     `color(colorstring)`, `color((r,g,b))`, `color(r,g,b)`输入格式与 `pencolor()`相同，同时设置填充颜色和画笔颜色为指定的值。                                                                                                                                  `color(colorstring1, colorstring2)`, `color((r1,g1,b1), (r2,g2,b2))`相当于`pencolor(colorstring1)` 加 `fillcolor(colorstring2)`，使用其他输入格式的方法也与之类似。 |

##### 2.3. 填充

|     描述     | 函数                    | 注释                                           |
| :----------: | :---------------------- | ---------------------------------------------- |
| 返回填充状态 | turtle.**filling**()    | 返回填充状态 (填充为 `True`，否则为 `False`)。 |
|   开始填充   | turtle.**begin_fill**() | 在绘制要填充的形状之前调用。                   |
|   结束填充   | turtle.**end_fill**()   | 填充上次调用`begin_fill()`之后绘制的形状。     |

##### 2.4. 更多绘图控制

|   描述   | 函数                                                         | 注释                                                         |
| :------: | :----------------------------------------------------------- | ------------------------------------------------------------ |
| 重置画笔 | turtle.**reset**()                                           | 从屏幕中删除海龟的绘图，海龟回到原点并设置所有变量为默认值。 |
| 清空画笔 | turtle.**clear**()                                           | 从屏幕中删除指定海龟的绘图。不移动海龟。海龟的状态和位置以及其他海龟的绘图不受影响。 |
|  写文字  | turtle.**write**(*arg*,*move=False*,*align='left'*， *font('Arial',8,'normal')*) | **参数：<br />arg**--要书写到TurtleScreen的对象<br />**move**--True/False<br />**align**--字符串"left","center"或"right"<br />**font**--一个三元组(fontname,fontsize,fonttype)(字体，字体大小，字体类型)<br />基于 *align* ("left", "center" 或 "right") 并使用给定的字体将文本 —— *arg* 的字符串表示形式 —— 写到当前海龟位置。 如果 *move* 为真值，画笔会移至文本的右下角。 默认情况下 *move* 为 `False`<br />**normal**：正常，**italic**：斜体 ，**bold**：粗体 |

#### 3. 海龟状态

##### 3.1. 可见性

|     描述     | 函数                                         | 注释                                                |
| :----------: | :------------------------------------------- | --------------------------------------------------- |
|   显示海龟   | turtle.**showturtle**()<br />turtle.**st**() |                                                     |
|   隐藏海龟   | turtle.**hideturtle**()<br />turtle.**ht**() |                                                     |
| 判断是否可见 | turtle.**isvisible**()                       | 如果海龟显示返回 `True`，如果海龟隐藏返回 `False`。 |

##### 3.2. 外观

|      描述      | 函数                                                         | 注释                                                         |
| :------------: | :----------------------------------------------------------- | ------------------------------------------------------------ |
|      形状      | turtle.**shape**(*name=None*)                                | **参数：name** -- 一个有效的形状名字符串                     |
|  大小调整模式  | turtle.**resizemode**(*rmode=None*)                          | **参数：rmode** -- 字符串 "**auto**", "**user**", "**noresize**" 其中之一<br />设置大小调整模式为以下值之一: "auto", "user", "noresize"。如未指定 *rmode* 则返回当前的大小调整模式。不同的大小调整模式的效果如下:                                                                            "**auto**": 根据画笔粗细值调整海龟的外观。                                                                                      "**user**": 根据拉伸因子和轮廓宽度 (outline) 值调整海龟的外观，两者是由 `shapesize()`设置的。                                                                                                                                                      "**noresize**": 不调整海龟的外观大小。                                                                           `resizemode("user")` 会由 `shapesize()` 带参数使用时被调用。 |
|    形状大小    | turtle.**shapesize**(*stretch_wid=None* ,*stretch_len=None*, *outline=None*) <br />turtle.**turtlesize**(*stretch_wid=None* ,*stretch_len=None*, *outline=None*) | **参数：<br />stretch_wid** -- 正数值<br />**stretch_len** -- 正数值<br />**outline** -- 正数值             <br />返回或设置画笔的属性 x/y-拉伸因子和/或轮廓。设置大小调整模式为 "user"。当且仅当大小调整模式设为 "user" 时海龟会基于其拉伸因子调整外观: *stretch_wid* 为垂直于其朝向的宽度拉伸因子，*stretch_len* 为平等于其朝向的长度拉伸因子，决定形状轮廓线的粗细。 |
|    剪切因子    | turtle.**shearfactor**(*shear=None*)                         | **参数：shear** -- 数值 (可选)                                                                                       设置或返回当前的剪切因子。根据 share 指定的剪切因子即剪切角度的切线来剪切海龟形状。*不* 改变海龟的朝向 (移动方向)。如未指定 shear 参数: 返回当前的剪切因子即剪切角度的切线，与海龟朝向平行的线条将被剪切。 |
|    设置倾角    | turtle.**settiltangle**(*angle*)       *3.1 版后已移除.*     | 旋转海龟形状使其指向 *angle* 指定的方向，忽略其当前的倾角，*不* 改变海龟的朝向 (移动方向)。 |
|      倾角      | turtle.**tiltangle**(*angle=None*)                           | **参数：angle** -- 一个数值 (可选)                                                                               设置或返回当前的倾角。如果指定 angle 则旋转海龟形状使其指向 angle 指定的方向，忽略其当前的倾角。*不* 改变海龟的朝向 (移动方向)。如果未指定 angle: 返回当前的倾角，即海龟形状的方向和海龟朝向 (移动方向) 之间的夹角。 |
|      倾斜      | turtle.**tilt**(*angle*)                                     | **参数：angle** -- 一个数值                                                                                           海龟形状自其当前的倾角转动 *angle* 指定的角度，但不改变海龟的朝向 (移动方向)。 |
|      变形      | turtle.**shapetransform**(*t11=None*, *t12=None*, *t21=None*, *t22=None*) | 设置或返回海龟形状的当前变形矩阵。如未指定任何矩阵元素，则返回以 4 元素元组表示的变形矩阵。 否则就根据设置指定元素的矩阵来改变海龟形状，矩阵第一排的值为 t11, t12 而第二排的值为 t21, t22。 行列式 t11 * t22 - t12 * t21 必须不为零，否则会引发错误。 根据指定矩阵修改拉伸因子 stretchfactor, 剪切因子 shearfactor 和倾角 tiltangle。 |
| 获取形状多边形 | turtle.**get_shapepoly**()                                   | 返回以坐标值对元组表示的当前形状多边形。这可以用于定义一个新形状或一个复合形状的多个组成部分。 |

#### 4. 使用事件

|    描述    | 函数                                           | 注释                                                         |
| :--------: | :--------------------------------------------- | ------------------------------------------------------------ |
| 当鼠标点击 | turtle.**onclick**(*fun*,*btn=1*,*add=None*)   | **参数：<br />fun** -- 一个函数，调用时将传入两个参数表示在画布上点击的坐标。 <br />**btn** -- 鼠标按钮编号，默认值为 1 (鼠标左键)   <br />**add** -- `True` 或 `False` -- 如为 `True` 则将添加一个新绑定，否则将取代先前的绑定将 **fun** 指定的函数绑定到鼠标点击此海龟事件。如果 **fun** 值为 `None`，则移除现有的绑定。 |
| 当鼠标释放 | turtle.**onrelease**(*fun*,*btn=1*,*add=None*) | **参数：<br />fun** -- 一个函数，调用时将传入两个参数表示在画布上点击的坐标。 <br />**btn** -- 鼠标按钮编号，默认值为 1 (鼠标左键)   <br />**add** -- `True` 或 `False` -- 如为 `True` 则将添加一个新绑定，否则将取代先前的绑定将 **fun** 指定的函数绑定到鼠标点击此海龟事件。如果 **fun** 值为 `None`，则移除现有的绑定。 |
| 当鼠标拖动 | turtle.**ondrag**(*fun*, *btn=1*, *add=None*)  | 与上同理                                                                                                                                                                               **注**: 在海龟上移动鼠标事件之前应先发生在此海龟上点击鼠标事件。 |

#### 5. 特殊海龟方法

|       描述       | 函数                                            | 注释                                                         |
| :--------------: | :---------------------------------------------- | ------------------------------------------------------------ |
|  开始记录多边形  | turtle.**begin_poly**()                         | 开始记录多边形的顶点。当前海龟位置为多边形的第一个顶点。     |
|  结束记录多边形  | turtle.**end_poly**()                           | 停止记录多边形的顶点。当前海龟位置为多边形的最后一个顶点。它将连线到第一个顶点。 |
|    获取多边形    | turtle.**get_poly**()                           | 返回最新记录的多边形。                                       |
|       克隆       | turtle.**clone**()                              | 创建并返回海龟的克隆体，具有相同的位置、朝向和海龟属性。     |
|   获取海龟画笔   | turtle.**getturtle**()<br />turtle.**getpen**() | 返回海龟对象自身。唯一合理的用法: 作为一个函数来返回 "匿名海龟": |
|     获取屏幕     | turtle.**getscreen**()                          | 返回作为海龟绘图场所的 `TurtleScreen`类对象。该对象将可调用 TurtleScreen 方法。 |
|  设置撤销缓冲区  | turtle.**setundobuffer**(*size*)                | 设置或禁用撤销缓冲区。<br /> 如果 **size** 为整数，则开辟一个给定大小的空撤销缓冲区。 **size** 给出了可以通过 `undo()` 方法/函数撤销海龟动作的最大次数。 如果 **size** 为 `None`，则禁用撤销缓冲区。 |
| 撤销缓冲区条目数 | turtle.**undobufferentries**()                  | 返回撤销缓冲区里的条目数。                                   |

#### 6. 复合形状

要使用由多个不同颜色多边形构成的复合海龟形状，你必须明确地使用辅助类 [`Shape`](https://docs.python.org/zh-cn/3/library/turtle.html#turtle.Shape)，具体步骤如下:

1. 创建一个空 Shape 对象，类型为 "compound"。

2. 按照需要使用 `addcomponent()` 方法向此对象添加多个部件。

   例如:

   ```python
s = Shape("compound")
   turtle.poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
   s.addcomponent(poly1, "red", "blue")
   poly2 = ((0,0),(10,-5),(-10,-5))
   s.addcomponent(poly2, "blue", "red")
   ```
   
3. 接下来将 Shape 对象添加到 Screen 对象的形状列表并使用它:

   

   ```python
   register_shape("myshape", s)
   shape("myshape")
   ```

**备注：**

[`Shape`](#jump1))类在 [`register_shape()`](#jump3) 方法的内部以多种方式使用。应用程序编写者 *只有* 在使用上述的复合形状时才需要处理 Shape 类。

### TurtleScreen/Screen 方法

#### 1、窗口控制

|               描述               |                             函数                             | 注释                                                         |
| :------------------------------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
|             背景颜色             |                 turtle.**bgcolor**(**args*)                  | **args** -- 一个颜色字符串或三个取值范围 0..colormode 内的数值或一个取值范围相同的数值3元组 |
|             背景图片             |               turtle.**bgpic**(*picname=None*)               | **picname** -- 一个字符串, gif-文件名, `"nopic"`, 或 `None`  |
|               清屏               |           turtle.**clear**()     **clearscreen**()           | **clear**()   备注：此 TurtleScreen 方法作为全局函数时只有一个名字 `clearscreen`。全局函数 `clear` 所对应的是 Turtle 方法 `clear`                                                                                            **clearscreen**()     从中删除所有海龟的全部绘图。将已清空的 TurtleScreen 重置为初始状态: 白色背景，无背景片，无事件绑定并启用追踪。 |
| 将屏幕上的所有海龟重置为初始状态 |                   turtle.**resetscreen**()                   | ` 备注:此 TurtleScreen 方法作为全局函数时只有一个名字 `resetscreen`。全局函数 `reset` 所对应的是 Turtle 方法 `reset`。` |
|             屏幕大小             | turtle.**screensize**(*canvwidth=None*, *canvheight=None*, *bg=None*) | **canvwidth** -- 正整型数，以像素表示画布的新宽度值<br />**canvheight** -- 正整型数，以像素表示画面的新高度值 <br />**bg** -- 颜色字符串或颜色元组，新的背景颜色                                             如未指定任何参数，则返回当前的 (canvaswidth, canvasheight)。否则改变作为海龟绘图场所的画布大小。不改变绘图窗口。要观察画布的隐藏区域，可以使用滚动条。通过此方法可以令之前绘制于画布之外的图形变为可见。 |
|          设置世界坐标系          |  turtle.**setworldcoordinates**(*llx*, *lly*, *urx*, *ury*)  | **llx**一个数值，画布左下角的x坐标  <br />**lly**一个数值，画布左下角的y坐标 <br />**urx**一个数值，画布右上角的x坐标 <br />**ury**一个数值，画布右上角的y坐标                                                                   设置用户自定义坐标系并在必要时切换模式为 "world"。这会执行一次 `screen.reset()`。如果 "world" 模式已激活，则所有图形将根据新的坐标系重绘。 |

#### 2、动画控制

| 描述 |                   函数                    | 注释                                                         |
| :--: | :---------------------------------------: | ------------------------------------------------------------ |
| 延迟 |      turtle.**delay**(*delay=None*)       | 设置或返回以毫秒数表示的延迟值 *delay*。(这约等于连续两次画布刷新的间隔时间。) 绘图延迟越长，动画速度越慢。 |
| 追踪 | turtle.**tracer**(*n=None*, *delay=None*) | 启用/禁用海龟动画并设置刷新图形的延迟时间。如果指定 *n* 值，则只有每第 n 次屏幕刷新会实际执行。(可被用来加速复杂图形的绘制。) 如果调用时不带参数，则返回当前保存的 n 值。第二个参数设置延迟值 |
| 更新 |            turtle.**update**()            | 执行一次 TurtleScreen 刷新。在禁用追踪时使用。               |

#### 3、使用屏幕事件

|       描述       |                             函数                             | 注释                                                         |
| :--------------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
|       监听       |       turtle.**listen**(*xdummy=None*, *ydummy=None*)        | 设置焦点到 TurtleScreen (以便接收按键事件)。使用两个 Dummy 参数以便能够传递 [`listen()`](https://docs.python.org/zh-cn/3/library/turtle.html#turtle.listen) 给 onclick 方法 |
| 当键盘按下并释放 | turtle.**onkey**(*fun*, *key*)\|**onkeyrelease**(*fun*, *key*) | **fun** -- 一个无参数的函数或 `None` <br />**key** -- 一个字符串: 键 (例如 "a") 或键标 (例如 "space")绑定 *fun* 指定的函数到按键释放事件。如果 *fun* 值为 `None`，则移除事件绑定。注: 为了能够注册按键事件，TurtleScreen 必须得到焦点。(参见 method [`listen()`](https://docs.python.org/zh-cn/3/library/turtle.html#turtle.listen) 方法。) |
|    当键盘按下    |           turtle.**onkeypress**(*fun*, *key=None*)           | 绑定 *fun* 指定的函数到指定键的按下事件。如未指定键则绑定到任意键的按下事件。注: 为了能够注册按键事件，必须得到焦点。 |
|    当点击屏幕    |     turtle.**onscreenclick**(*fun*, *btn=1*, *add=None*)     | **fun** -- 一个函数，调用时将传入两个参数表示在画布上点击的坐标。 <br />**btn** -- 鼠标按钮编号，默认值为 1 (鼠标左键) <br />**add** -- `True` 或 `False` -- 如为 `True` 则将添加一个新绑定，否则将取代先前的绑定                                                                                                                      绑定 *fun* 指定的函数到鼠标点击屏幕事件。如果 *fun* 值为 `None`，则移除现有的绑定。       备注：此 TurtleScreen 方法作为全局函数时只有一个名字 `onscreenclick`。全局函数 `onclick` 所对应的是 Turtle 方法 `onclick`。 |
|    当达到定时    |               turtle.**ontimer**(*fun*, *t=0*)               | **fun** -- 一个无参数的函数 **t** -- 一个数值 >= 0                                                                            安装一个计时器，在 *t* 毫秒后调用 *fun* 函数。 |
|      主循环      |         turtle.**mainloop**()<br />turtle.**done**()         | 开始事件循环 - 调用 Tkinter 的 mainloop 函数。必须作为一个海龟绘图程序的结束语句。如果一个脚本是在以 -n 模式 (无子进程) 启动的 IDLE 中运行时 *不可* 使用 - 用于实现海龟绘图的交互功能。 |

#### 4、设置与特殊方法

|   描述   |                             函数                             | 注释                                                         |
| :------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
| 海龟模式 |     <span id='jump6'>turtle.**mode**(*mode=None*)</span>     | 设置海龟模式 ("standard", "logo" 或 "world") 并执行重置。如未指定模式则返回当前的模式。"standard" 模式与旧的 [`turtle`](https://docs.python.org/zh-cn/3/library/turtle.html#module-turtle) 兼容。"logo" 模式与大部分 Logo 海龟绘图兼容。"world" 模式使用用户自定义的 "世界坐标系"。                                                                             **注意**: 在此模式下，如果 `x/y` 单位比率不等于 1 则角度会显得扭曲。 |
| 颜色模式 |              turtle.**colormode**(*cmode=None*)              |                                                              |
| 获取画布 |                    turtle.**getcanvas**()                    | 返回此 TurtleScreen 的 Canvas 对象。供了解 Tkinter 的 Canvas 对象内部机理的人士使用。 |
| 获取形状 |                    turtle.**getshapes**()                    | 返回所有当前可用海龟形状的列表。                             |
| 添加形状 | <span id='jump3'>turtle.**register_shape**()</span>\|**addshape**() | 调用此函数有三种不同方式:    1.*name* 为一个 gif 文件的文件名， *shape* 为 `None`: 安装相应的图像形状。备注：当海龟转向时图像形状 *不会* 转动，因此无法显示海龟的朝向!                   2.*name* 为指定的字符串，*shape* 为由坐标值对构成的元组: 安装相应的多边形形状。   3.name 是任意字符串，形状是（复合）形状对象：安装相应的复合形状。                            <br />将一个海龟形状加入 TurtleScreen 的形状列表。只有这样注册过的形状才能通过执行 `shape(shapename)` 命令来使用。 |
| 所有海龟 |                     turtle.**turtles**()                     | 返回屏幕上的海龟列表。                                       |
| 窗口高度 |                  turtle.**window_height**()                  | 返回海龟窗口的高度。                                         |
| 窗口宽度 |                  turtle.**window_width**()                   | 返回海龟窗口的宽度。                                         |



#### 5、输入方法

|   描述   |                             函数                             | 注释                                                         |
| :------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
| 文本输入 |           turtle.**textinput**(*title*, *prompt*)            | 作用：**弹出一个对话框窗口用来输入一个字符串**。<br />**title** 为对话框窗口的标题<br />**prompt** 为一条文本，通常用来提示要输入什么信息。返回输入的字符串。如果对话框被取消则返回 `None`。 |
| 数字输入 | turtle.**numinput**(*title*, *prompt*, *default=None*, *minval=None*, *maxval=None*) | 作用：**弹出一个对话框窗口以输入数字**。<br />标题(***title***)是对话框窗口的标题，提示(***prompt***)是主要描述要输入哪些数字信息的文本。<br />默认值(**default**)：默认值，<br />最小值(**minval**)：输入的最小值<br />最大值(**maxval**)：输入的最大值<br />数字输入必须在最小值范围内。如果给出这些，则为maxval。否则，将发出提示，并且对话框保持打开状态以进行更正。返回数字输入。如果对话框被取消，则返回`None`. |

```python
import turtle
turtle.shape("turtle")
direction = turtle.textinput('你要去哪', '请告诉我地点')
print(direction)
number = turtle.numinput('number show', 'give a number', 100, 1, 100)
print(number)
t.fd(number)
```



#### 6、Screen专有方法

|     描述     |                             函数                             | 注释                                                         |
| :----------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
|     退出     |                       turtle.**bye**()                       | 关闭海龟绘图窗口。                                           |
| 当点击时退出 |                   turtle.**exitonclick**()                   | 将 `bye()` 方法绑定到 Screen 上的鼠标点击事件。                                                                                                                 如果配置字典中 "using_IDLE" 的值为 `False` (默认值) 则同时进入主事件循环。注: 如果启动 IDLE 时使用了 `-n` 开关 (无子进程)，`turtle.cfg` 中此数值应设为 `True`。在此情况下 IDLE 本身的主事件循环同样会作用于客户脚本。 |
|     设置     | turtle.**setup**(*width=_CFG['width']*, *height=_CFG['height']*, *startx=_CFG['leftright']*, *starty=_CFG['topbottom']*) | 设置主窗口的大小和位置。默认参数值保存在配置字典中，可通过 `turtle.cfg` 文件进行修改。                                                                                                                                                                   **width** -- 如为一个整型数值，表示大小为多少像素，如为一个浮点数值，则表示屏幕的占比；默认为屏幕的 50%                                                                                                                                  **height** -- 如为一个整型数值，表示高度为多少像素，如为一个浮点数值，则表示屏幕的占比；默认为屏幕的 75%                                                                                                                              **startx** -- 如为正值，表示初始位置距离屏幕左边缘多少像素，负值表示距离右边缘，`None` 表示窗口水平居中                                                                                                                                             **starty** -- 如为正值，表示初始位置距离屏幕上边缘多少像素，负值表示距离下边缘，`None` 表示窗口垂直居中 |
|     标题     |               turtle.**title**(*titlestring*)                | **titlestring** -- 一个字符串，显示为海龟绘图窗口的标题栏文本                                                          设置海龟窗口标题为 *titlestring* 指定的文本。 |

## 公共类

- *class* turtle.**RawTurtle**(*canvas*)

- *class* turtle.**RawPen**(*canvas*)

  参数**canvas** -- 一个 `tkinter.Canvas` , `ScrolledCanvas` 或 `TurtleScreen`类对象创建一个海龟。海龟对象具有 "Turtle/RawTurtle 方法" 一节所述的全部方法。

- *class* turtle.**Turtle**

  RawTurtle 的子类，具有相同的接口，但其绘图场所为默认的 `Screen` 类对象，在首次使用时自动创建。

- *class* turtle.**TurtleScreen**(*cv*)

  参数**cv** -- 一个 `tkinter.Canvas` 类对象提供面向屏幕的方法例如 `setbg()` 等。说明见上文。

- *class* turtle.**Screen**

  TurtleScreen 的子类，[增加了四个方法](#6、Screen专有方法).

- *class* turtle.**ScrolledCanvas**(*master*)

  参数**master** -- 可容纳 ScrolledCanvas 的 Tkinter 部件，即添加了滚动条的 Tkinter-canvas由 Screen 类使用，使其能够自动提供一个 ScrolledCanvas 作为海龟的绘图场所。

- <span id="jump1">*class* turtle.**Shape**(*type_*, *data*)</span>

  参数**type_** -- 字符串 "polygon", "image", "compound" 其中之一实现形状的数据结构。`(type_, data)` 必须遵循以下定义:

  | type       | data                                                         |
  | ---------- | ------------------------------------------------------------ |
  | "polygon"  | 一个多边形元组，即由坐标值对构成的元组                       |
  | "image"    | 一个图片 (此形式仅限内部使用!)                               |
  | "compound" | `None` (复合形状必须使用 [`addcomponent()`](#jump2)) 方法来构建) |

  <span id='jump2'>**addcomponent**(*poly*, *fill*, *outline=None*)</span>

  - 参数

    **poly** -- 一个多边形，即由数值对构成的元组**fill** -- 一种颜色，将用来填充 *poly* 指定的多边形**outline** -- 一种颜色，用于多边形的轮廓 (如有指定)

  示例:

  

  ```
  >>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
  >>> s = Shape("compound")
  >>> s.addcomponent(poly, "red", "blue")
  >>> # ... add more components and then use register_shape()
  ```

  参见 [复合形状](#复合形状)。

- <span id='jump7'>*class* turtle.**Vec2D**(*x*, *y*)</span>

  一个二维矢量类，用来作为实现海龟绘图的辅助类。也可能在海龟绘图程序中使用。派生自元组，因此矢量也属于元组!提供的运算 (*a*, *b* 为矢量, *k* 为数值):`a + b` 矢量加法      `a - b` 矢量减法              `a * b` 内积                  `k * a` 和 `a * k` 与标量相乘               `abs(a)` a 的绝对值                          `a.rotate(angle)` 旋转



## `turtledemo` --- 演示脚本集

`turtledemo` 包汇集了一组演示脚本。这些脚本可以通过以下命令打开所提供的演示查看器运行和查看:

```
python -m turtledemo
```

此外，你也可以单独运行其中的演示脚本。例如，:

```
python -m turtledemo.bytedesign
```

`turtledemo`包目录中的内容:

- 一个演示查看器 `__main__.py`，可用来查看脚本的源码并即时运行。
- 多个脚本文件，演示 `turtle`模块的不同特性。所有示例可通过 Examples 菜单打开。也可以单独运行每个脚本。
- 一个 `turtle.cfg` 文件，作为说明如何编写并使用模块配置文件的示例模板。

演示脚本清单如下:

| 描述                                                         | 名称            | 相关特性                                               |
| :----------------------------------------------------------- | :-------------- | :----------------------------------------------------- |
| 复杂的传统海龟绘图模式                                       | bytedesign      | `tracer()`, delay, `update()`                          |
| 绘制 Verhulst 动态模型，演示通过计算机的运算可能会生成令人惊叹的结果 | chaos           | 世界坐标系                                             |
| 绘制模拟时钟显示本机的当前时间                               | clock           | 海龟作为表针, ontimer                                  |
| 试验 r, g, b 颜色模式                                        | colormixer      | `ondrag()` 当鼠标拖动                                  |
| 绘制 3 棵广度优先树                                          | forest          | 随机化                                                 |
| 绘制 Hilbert & Koch 曲线                                     | fractalcurves   | 递归                                                   |
| 文化数学 (印度装饰艺术)                                      | lindenmayer     | L-系统                                                 |
| 汉诺塔                                                       | minimal_hanoi   | 矩形海龟作为汉诺盘 (shape, shapesize)                  |
| 玩经典的“尼姆”游戏，开始时有三堆小棒，与电脑对战。           | nim             | 海龟作为小棒，事件驱动 (鼠标, 键盘)                    |
| 超极简主义绘画程序                                           | paint           | `onclick()` 当鼠标点击                                 |
| 初级技巧                                                     | peace           | 海龟: 外观与动画                                       |
| 非周期性地使用风筝和飞镖形状铺满平面                         | penrose         | `stamp()` 印章                                         |
| 模拟引力系统                                                 | planet_and_moon | 复合开关, `Vec2D` 类                                   |
| 两两相对并不断旋转舞蹈的海龟                                 | round_dance     | 复合形状, clone shapesize, tilt, get_shapepoly, update |
| 动态演示不同的排序方法                                       | sorting_animate | 简单对齐, 随机化                                       |
| 一棵 (图形化的) 广度优先树 (使用生成器)                      | tree            | `clone()` 克隆                                         |
| 简单设计                                                     | two_canvases    | 两块画布上的海龟                                       |
| 一个来自介绍海龟绘图的维基百科文章的图案                     | wikipedia       | `clone()`, `undo()`                                    |
| 另一个初级示例                                               | yinyang         | `circle()` 画圆                                        |











