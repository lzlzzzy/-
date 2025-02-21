import requests
from bs4 import BeautifulSoup
import pandas as pd

# 基本的URL
base_url = 'https://car.yiche.com/newcar/salesrank/?level=63&energy=9&flag=2&page={}'


# 发送GET请求的函数
def fetch_page(page_number):
    url = base_url.format(page_number)
    response = requests.get(url)
    response.encoding = 'utf-8'  # 确保正确解码中文
    return response.text


# 解析网页并提取车的信息
def parse_car_info(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 查找所有包含车信息的div
    car_items = soup.find_all('div', class_='rk-item ka')

    cars_info = []
    for car in car_items:
        car_name = car.get('data-cxname', '未找到名称')
        car_price = car.find('div', class_='rk-car-price').text.strip() if car.find('div',
                                                                                    class_='rk-car-price') else '未找到价格'
        car_sales = car.find('span', class_='rk-car-num').text.strip() if car.find('span',
                                                                                   class_='rk-car-num') else '未找到销量'

        # 保存提取的信息
        cars_info.append({
            '车名': car_name,
            '价格': car_price,
            '销量': car_sales
        })

    return cars_info


# 获取所有页面的车信息
def fetch_all_car_info(total_pages):
    all_cars_info = []

    for page in range(1, total_pages + 1):
        print(f"正在爬取第 {page} 页...")
        html = fetch_page(page)
        cars_info = parse_car_info(html)
        all_cars_info.extend(cars_info)

    return all_cars_info


# 设置总页数
total_pages = 10  # 如果页数有变化，你可以动态获取

# 获取所有页面的车信息
all_cars_info = fetch_all_car_info(total_pages)

# 将爬取的数据保存到DataFrame
df = pd.DataFrame(all_cars_info)

# 将DataFrame保存到Excel
df.to_excel('2024you.xlsx', index=False, engine='openpyxl')

print("数据已保存到 '2024you.xlsx'")
