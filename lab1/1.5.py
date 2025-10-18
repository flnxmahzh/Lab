import time

def print_thailand_flag():
    # 定义颜色代码：红色、白色、蓝色背景及重置；Define color codes: red, white, blue backgrounds and reset
    red_bg = "\033[41m"
    white_bg = "\033[107m"
    blue_bg = "\033[44m"
    reset = "\033[0m"

    # 单个像素（空格+颜色背景）；Single pixel (space + color background)
    red_pixel = red_bg + " " + reset
    white_pixel = white_bg + " " + reset
    blue_pixel = blue_bg + " " + reset

    # 国旗尺寸：宽24，高12（比例3:2）；Flag size: width 24, height 12 (ratio 3:2)
    flag_width = 24
    flag_height = 12

    # 条纹高度分配（比例1:1:2:1:1，总高度12）；Stripe height distribution (ratio 1:1:2:1:1, total height 12)
    # 红色：0-1行，白色：2-3行，蓝色：4-7行，白色：8-9行，红色：10-11行；Red: rows 0-1, White: rows 2-3, Blue: rows 4-7, White: rows 8-9, Red: rows 10-11
    for y in range(flag_height):
        line = ""
        time.sleep(0.1)  # 每行打印前的延迟；Delay before printing each line
        # 确定当前行的颜色；Determine the color of the current line
        if 0 <= y <= 1 or 10 <= y <= 11:
            pixel = red_pixel
        elif 2 <= y <= 3 or 8 <= y <= 9:
            pixel = white_pixel
        else:  # 4-7行；rows 4-7
            pixel = blue_pixel
        # 生成一行像素；Generate a line of pixels
        line += pixel * flag_width
        print(line)
        time.sleep(0.1)  # 每行打印后的延迟；Delay after printing each line
    print(reset)  # 重置终端颜色；Reset terminal color
    time.sleep(0.1)


print_thailand_flag()