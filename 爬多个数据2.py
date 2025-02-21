from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd  # 导入 pandas 库

# 设置 Selenium WebDriver
driver = webdriver.Chrome()  # 或者你可以选择其他浏览器的 WebDriver

# 目标网页 URL
url = 'https://price.pcauto.com.cn/price/q-rl41_42_43_9998.html'

# 打开网页
driver.get(url)

# 等待页面加载
time.sleep(5)

# 模拟滚动
# 滚动 5 次，每次滚动一段距离
# 修改滚动方式，增加等待时间
for _ in range(69):  # 尝试滚动更多次
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 增加延时，确保页面加载足够的内容


# 获取页面的 HTML
html = driver.page_source

# 解析页面内容
soup = BeautifulSoup(html, 'html.parser')

# 找到包含车信息的所有 <a> 元素
car_elements = soup.find_all('a', class_='flex w-full flex-col items-center')

# 用于存储提取到的车辆信息
car_info = []

# 遍历每一个车的元素，提取车名和价格范围
for car in car_elements:
    # 获取车辆名称
    car_name = car.find('div', class_='relative -mt-2 max-w-full overflow-hidden text-ellipsis whitespace-nowrap text-base text-[#333] hover:text-orange')
    if car_name:
        car_name = car_name.text.strip()

    # 获取价格范围
    price_range = car.find('div', class_='mt-1 mb-[6px] max-w-full overflow-hidden text-ellipsis whitespace-nowrap text-base font-semibold text-orange')
    if price_range:
        price_range = price_range.text.strip()

    # 将车名和价格范围保存到列表
    car_info.append({
        'name': car_name,
        'price': price_range
    })

# 将数据存储到 pandas DataFrame
df = pd.DataFrame(car_info)

# 保存为 Excel 文件
df.to_excel('700shuju.xlsx', index=False, engine='openpyxl')  # 设置文件名和保存方式

# 打印保存成功的消息
print("数据已保存到 '700shuju.xlsx'")

# 关闭浏览器
driver.quit()