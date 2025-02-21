

import matplotlib.pyplot as plt

# 数据
months = ['4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月','12月']
sales_volume = [7058, 8646, 13120, 14296, 13111, 13559, 20726, 23156, 25815]  # 销售量
total_sales = [7058, 15704, 43120, 30000, 56231, 69790, 90516, 113672, 139487]  # 总销售量

# 创建折线图
plt.figure(figsize=(8, 6))
plt.plot(months, sales_volume, label='销售量', marker='o', color='b', linestyle='-', markersize=6)
plt.plot(months, total_sales, label='总销售量', marker='o', color='r', linestyle='-', markersize=6)
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 添加标题和标签
plt.title('小米SU7汽车销售量与总销售量折线图', fontsize=14)
plt.xlabel('月份', fontsize=12)
plt.ylabel('数量', fontsize=12)

# 添加图例
plt.legend()

# 显示图形
plt.grid(True)
plt.show()
