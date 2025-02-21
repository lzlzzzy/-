import requests
from bs4 import BeautifulSoup
import pandas as pd  # 导入 pandas 用于保存到 Excel

# 目标网页 URL
base_url = 'https://price.pcauto.com.cn/top/k0.html'

# 用于存储所有抓取到的车辆信息
all_car_info = []

# 循环抓取每一页
page_number = 1
while True:
    print(f"正在抓取第 {page_number} 页...")

    # 拼接当前页的 URL
    url = base_url if page_number == 1 else f'https://price.pcauto.com.cn/top/k0-p{page_number}.html'

    # 发送 GET 请求
    response = requests.get(url)

    # 设置编码格式
    response.encoding = response.apparent_encoding

    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到包含车信息的 <ul class="listA"> 元素
    car_list = soup.find('ul', class_='listA')

    # 如果没有找到该列表，说明已经没有更多的车了
    if not car_list:
        print("没有更多的页面了")
        break

    # 提取车名、价格和热度
    car_info = []

    # 遍历所有 <li> 元素
    for item in car_list.find_all('li'):
        # 获取车辆名称
        car_name = item.find('p', class_='sname').text.strip()

        # 获取价格范围
        price_range = item.find('p', class_='col col1 price').text.strip().replace('官方价：', '')

        # 获取热度
        hotness = item.find('span', class_='fl red rd-mark').text.strip().replace('热度', '')

        # 保存提取的汽车信息
        car_info.append({
            'name': car_name,
            'price': price_range,
            'hotness': hotness
        })

    # 将当前页的车辆信息添加到总数据中
    all_car_info.extend(car_info)

    # 查找是否有“下一页”的链接
    next_page = soup.find('a', class_='next')

    # 如果没有“下一页”按钮，则退出循环
    if not next_page:
        print("已经抓取完所有页面。")
        break

    # 增加页数，继续抓取下一页
    page_number += 1

# 打印所有车辆信息
for car in all_car_info:
    print(f"车名: {car['name']}, 价格范围: {car['price']}, 热度: {car['hotness']}")

# 将抓取到的汽车信息保存到 Excel 文件 "duizhangde.xlsx"
# 将抓取到的汽车信息保存到 Excel 文件 "duizhangde.xlsx"
df = pd.DataFrame(all_car_info)
df.to_excel('duizhangde.xlsx', index=False)

print("数据已成功保存到 'duizhangde.xlsx'.")
