import turtle
# 初始化画笔 Initialize the brush
t = turtle.Turtle()
t.speed(0)  # 绘图速度最快 Set drawing speed to the fastest
t.pensize(5)  # 保持画笔粗细 Set the pen thickness
# 定义绘制单个图案的函数 Define a function to draw a single pattern
def draw_pattern(y_offset):
    # 绘制左侧曲线（起点y坐标根据偏移量调整） Draw the left curve (the starting y-coordinate is adjusted according to the offset)
    t.penup()
    t.goto(-100, -50 + y_offset)  # y轴偏移，避免图案重叠 Y-axis offset to avoid pattern overlap
    t.pendown()
    t.setheading(0)
    t.circle(100, 90)
    # 绘制右侧曲线（对称位置，同样调整y坐标） Draw the right curve (symmetric position, also adjust y-coordinate)
    t.penup()
    t.goto(100, -50 + y_offset)
    t.pendown()
    t.setheading(180)
    t.circle(-100, 90)
# 重复生成5次图案（每次向下偏移200像素，避免重叠） Repeat to generate 5 patterns (offset 200 pixels downward each time to avoid overlap)
for i in range(5):
    draw_pattern(-i * 200)  # 每次y坐标减少200，实现纵向排列 Decrease y-coordinate by 200 each time to achieve vertical arrangement
# 隐藏画笔 + 保持窗口 Hide the brush + keep the window open
t.hideturtle()
turtle.done()