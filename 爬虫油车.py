import requests
import csv
from time import sleep


def get_car_sales_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Referer': 'https://car.yiche.com/'
    }

    # 发现的实际API接口（可能需要定期验证）
    api_url = "https://api.yiche.com/web-sale/rank/list"

    params = {
        "level": 63,
        "energy": 9,
        "flag": 2,
        "pageIndex": 1,
        "pageSize": 100
    }

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()

        if data["StatusCode"] != 0:
            print("API返回状态码异常:", data)
            return []

        return data["Data"]["List"]

    except Exception as e:
        print("获取数据失败:", e)
        return []


def save_to_csv(data, filename="yiche_sales.csv"):
    if not data:
        return

    fields = ["排名", "车型名称", "厂商", "指导价", "近半年销量", "当月销量"]

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for item in data:
            row = {
                "排名": item["Rank"],
                "车型名称": item["Name"],
                "厂商": item["ManufacturerName"],
                "指导价": f'{item["MinPrice"]} - {item["MaxPrice"]}万' if item["MinPrice"] else "暂无报价",
                "近半年销量": item["SaleCountHalfYear"],
                "当月销量": item["SaleCount"]
            }
            writer.writerow(row)

    print(f"数据已保存到 {filename}")


if __name__ == "__main__":
    # 获取数据
    car_data = get_car_sales_data()

    if car_data:
        # 保存数据
        save_to_csv(car_data)

        # 打印前5条示例
        print("示例数据：")
        for item in car_data[:5]:
            print(f'{item["Rank"]}. {item["Name"]} | 当月销量：{item["SaleCount"]}')
    else:
        print("未能获取到有效数据")