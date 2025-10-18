plot_list = [[0 for i in range(10)] for j in range(10)]
# 计算y=1/x，x取1到10（避免除以0） Calculate y=1/x where x ranges from 1 to 10 (avoid division by zero)
result = [1/(i+1) for i in range(10)]
min_y = min(result)  # 计算y的最小值 Calculate the minimum value of y
max_y = max(result)  # 计算y的最大值 Calculate the maximum value of y
# 计算步长 Calculate the step size
step = (max_y - min_y) / 9
# 初始化y轴刻度 Initialize y-axis scales
for i in range(10):
    # 从上到下y值递减 y-values decrease from top to bottom
    plot_list[i][0] = step * (9 - i) + min_y
# 标记函数曲线位置 Mark the position of the function curve
for i in range(9):
    for j in range(10):
        # 当当前行y值与函数值的差小于步长时标记 Mark when the difference between current row's y-value and function value is less than step
        if abs(plot_list[i][0] - result[j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1
# 打印图表 Print the chart
for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            # 显示y轴刻度 Display y-axis scale
            line += '\t' + str(round(plot_list[i][j], 2)) + '\t'
        else:
            if plot_list[i][j] == 0:
                line += '--'
            if plot_list[i][j] == 1:
                line += '!!'  # 用!!标记函数点 Mark function points with !!
    print(line)
# 显示x轴刻度（1到10） Display x-axis scale (1 to 10)
print('\t1\t2 3 4 5 6 7 8 9 10')