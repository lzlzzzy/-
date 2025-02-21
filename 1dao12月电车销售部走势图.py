import matplotlib.pyplot as plt

# 数据
months = list(range(8, 14))  # 7月到12月
values = [
    1973420,
    2087800,
    2213320,
    2560510,
    2386920,
    1614090,
]

# 创建折线图
plt.figure(figsize=(10, 6))  # 设置图形大小
plt.plot(months, values, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)  # 绘制折线图

# 添加标题和标签
plt.title('Monthly Data Trend (July to December)', fontsize=16)  # 图形标题
plt.xlabel('Month', fontsize=14)  # x轴标签
plt.ylabel('Value', fontsize=14)  # y轴标签

# 设置x轴刻度
plt.xticks(months, [f'{i}' for i in months])  # 显示7到12月

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.6)

# 添加数据标签
for i, v in enumerate(values):
    plt.text(i + 7, v + 10000, f'{v:,}', ha='center', fontsize=10)  # 在每个数据点上显示数值，格式化为千分位

# 显示图形
plt.tight_layout()  # 自动调整布局
plt.show()