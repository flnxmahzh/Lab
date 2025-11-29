# 1. 导入必要模块 Import necessary modules
import tkinter as tk  # 图形界面核心 Core of graphical interface
import random  # 生成随机字符 Generate random characters
import pygame  # 播放背景音乐 Play background music
from PIL import Image, ImageTk  # 处理背景图片（支持png）Process background images (supports png)

# 2. 初始化pygame音乐模块（播放背景音乐）Initialize pygame music module (for playing background music)
pygame.mixer.init()

# 3. 定义字符权重计算函数：A=1，B=2…Z=26 Define function to calculate character weight: A=1, B=2…Z=26
def get_char_weight(char):
    return ord(char) - ord('A') + 1  # ord('A')=65，计算字符ASCII码差值得到权重 ord('A')=65, calculate ASCII code difference to get weight

# 4. 生成单个区块的函数（参数：区块长度、平均值区间）Function to generate a single block (parameters: block length, average value range)
def generate_block(block_length, min_avg, max_avg):
    while True:  # 循环直到生成符合平均值要求的区块 Loop until a block meeting the average requirement is generated
        # 生成指定长度的随机大写字母（A-Z）Generate random uppercase letters (A-Z) of specified length
        block_chars = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(block_length)]
        # 计算区块总权重 Calculate total weight of the block
        total_weight = sum(get_char_weight(c) for c in block_chars)
        # 计算区块平均值 Calculate average weight of the block
        avg_weight = total_weight / block_length
        # 判断平均值是否在指定区间，符合则返回区块字符串 Check if the average is within the specified range, return the block string if yes
        if min_avg <= avg_weight <= max_avg:
            return ''.join(block_chars)

# 5. 生成完整密钥的函数（格式：XXXXX-XXXX-XXXX）Function to generate a complete key (format: XXXXX-XXXX-XXXX)
def generate_full_key():
    # 生成3个区块：长度5、4、4，平均值10-15 Generate 3 blocks: lengths 5, 4, 4, average 10-15
    block1 = generate_block(5, 10, 15)
    block2 = generate_block(4, 10, 15)
    block3 = generate_block(4, 10, 15)
    # 拼接成最终密钥格式 Concatenate into the final key format
    full_key = f"{block1}-{block2}-{block3}"
    # 更新密钥显示框（清空原有内容，插入新密钥）Update key display box (clear original content and insert new key)
    key_display.delete(0, tk.END)
    key_display.insert(0, full_key)

# 6. 简单动画函数（让标题文字左右移动）Simple animation function (make title text move left and right)
def animate_title():
    global title_x, title_dir  # 全局变量：标题x坐标、移动方向 Global variables: title x-coordinate, movement direction
    # 更新x坐标（dir=1向右，dir=-1向左）Update x-coordinate (dir=1 for right, dir=-1 for left)
    title_x += title_dir * 2
    # 碰到窗口边界则反向 Reverse direction when hitting window boundary
    if title_x > 300 or title_x < 0:
        title_dir *= -1
    # 重新设置标题位置 Reset title position
    title_label.place(x=title_x, y=10)
    # 每隔20毫秒重复调用（形成动画）Repeat call every 20 milliseconds (to form animation)
    root.after(20, animate_title)

# 7. 创建主窗口 Create main window
root = tk.Tk()
root.title("Генератор игровых ключей — Вариант6（游戏密钥生成器 变体6）")  # 窗口标题 Window title
root.geometry("450x300")  # 窗口大小：宽450，高300 Window size: width 450, height 300

# 8. 加载并设置背景图片（groundphoto.png）Load and set background image (groundphoto.png)
try:
    # 打开背景图片，调整大小适配窗口 Open background image and resize to fit window
    bg_image = Image.open("groundphoto.png")
    bg_image = bg_image.resize((450, 300), Image.Resampling.LANCZOS)  # 适配窗口尺寸 Fit window size
    bg_photo = ImageTk.PhotoImage(bg_image)
    # 创建背景标签（铺满窗口）Create background label (cover the window)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    # 图片加载失败时用灰色背景兜底 Use gray background as fallback if image loading fails
    bg_label = tk.Label(root, bg="#333333")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 9. 播放背景音乐（music.mp3，循环播放）Play background music (music.mp3, loop playback)
try:
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)  # -1表示无限循环 -1 means infinite loop
except:
    print("⚠️ 背景音乐加载失败：请确保music.mp3文件在同一文件夹 ⚠️ Background music loading failed: please ensure music.mp3 is in the same folder")

# 10. 创建动画标题（全局变量初始化）Create animated title (initialize global variables)
title_x = 0  # 初始x坐标 Initial x-coordinate
title_dir = 1  # 初始移动方向（向右）Initial movement direction (to the right)
title_label = tk.Label(root, text="游戏密钥 Game Keygen", font=("Arial", 16, "bold"), fg="red", bg="white")
title_label.place(x=title_x, y=10)

# 11. 创建密钥显示框（只读样式，方便复制）Create key display box (read-only style for easy copying)
key_display = tk.Entry(root, font=("Arial", 14), width=25, justify="center")
key_display.place(x=75, y=80)

# 12. 创建生成密钥按钮（点击调用生成函数）Create generate key button (call generate function on click)
generate_btn = tk.Button(root, text="生成密钥,Generate key", font=("Arial", 12), command=generate_full_key)
generate_btn.place(x=180, y=130)

# 13. 启动动画和主循环 Start animation and main loop
animate_title()  # 启动标题动画 Start title animation
root.mainloop()  # 保持窗口显示，等待用户操作 Keep window displayed and wait for user operations

# 14. 关闭pygame（窗口关闭后停止音乐）Close pygame (stop music after window is closed)
pygame.mixer.quit()