def analyze_sequence():
    # 读取sequence.txt文件中的数字序列；Read the number sequence from the sequence.txt file
    with open('sequence.txt', 'r') as f:
        # 读取并转换为浮点数，忽略空行；Read and convert to floating-point numbers, ignoring empty lines
        sequence = [float(line.strip()) for line in f if line.strip()]

    # 数据过滤：舍去负数，只保留非负数，再分为大于5和小于5的数；Filter data: discard negative numbers, keep only non-negative numbers, then split into numbers greater than 5 and less than 5
    non_negative = [x for x in sequence if x >= 0]  # 舍去负数；Discard negative numbers
    greater_5 = [x for x in non_negative if x > 5]  # 大于5的非负数；Non-negative numbers greater than 5
    less_5 = [x for x in non_negative if x < 5]  # 小于5的非负数；Non-negative numbers less than 5

    # 计算统计数据；Calculate statistical data
    total_valid = len(greater_5) + len(less_5)
    if total_valid == 0:
        greater_percent = 0.0
        less_percent = 0.0
    else:
        greater_percent = (len(greater_5) / total_valid) * 100
        less_percent = (len(less_5) / total_valid) * 100

    # 创建柱状图（每个方块代表5%）；Create bar chart (each block represents 5%)
    greater_bars = "▇" * int(greater_percent // 5)
    less_bars = "▇" * int(less_percent // 5)

    # 输出结果；Output results
    print("Диаграмма распределения неотрицательных значений (больше 5 и меньше 5)")
    print("=" * 60)
    print(f"Больше 5                {greater_bars} {greater_percent:.1f}% ({len(greater_5)} шт.)")
    print(f"Меньше 5                {less_bars} {less_percent:.1f}% ({len(less_5)} шт.)")
    print("=" * 60)
    print(f"Всего valid данных: {total_valid}")
    print(f"Отброшено данных: {len(sequence) - total_valid}")


# 运行分析；Run the analysis
analyze_sequence()