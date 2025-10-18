# 定义ANSI转义码（控制背景色）Define ANSI escape codes (control background color)
RED_BG = "\033[41m"    # 红色背景 Red background
WHITE_BG = "\033[47m"  # 白色背景 White background
BLUE_BG = "\033[44m"   # 蓝色背景 Blue background
RESET = "\033[0m"      # 重置颜色 Reset color
# 定义各条带宽度（比例 1:1:2:1:1）Define the width of each stripe (ratio 1:1:2:1:1)
red_stripe = " " * 10   # 红色条（10个空格，用红色背景填充）Red stripe (10 spaces, filled with red background)
white_stripe = " " * 10 # 白色条（10个空格）White stripe (10 spaces)
blue_stripe = " " * 20  # 蓝色条（20个空格，宽度是其他条的2倍）Blue stripe (20 spaces, twice the width of other stripes)
# 生成一行国旗（按顺序拼接色带）Generate one row of the flag (splice stripes in order)
def create_flag_row():
    return (
        f"{RED_BG}{red_stripe}"       # 第一条红 First red stripe
        f"{WHITE_BG}{white_stripe}"   # 第一条白 First white stripe
        f"{BLUE_BG}{blue_stripe}"     # 中间蓝 Middle blue stripe
        f"{WHITE_BG}{white_stripe}"   # 第二条白 Second white stripe
        f"{RED_BG}{red_stripe}"       # 第二条红 Second red stripe
        f"{RESET}"                    # 重置颜色 Reset color
    )
# 输出10行（形成矩形国旗）Output 10 rows (form a rectangular flag)
for _ in range(10):
    print(create_flag_row())