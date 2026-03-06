import requests
from datetime import datetime

class GoldDataFetcher:
    def __init__(self):
        self.price_history = []

    def fetch_price(self):
        try:
            response = requests.get('https://api.gold-api.com/price/XAU', timeout=5)
            data = response.json()
            # 价格单位：美元/盎司，转换为人民币/克
            price_usd_oz = float(data['price'])
            price_cny_g = price_usd_oz * 7.2 / 31.1035

            self.price_history.append({
                'price': round(price_cny_g, 2),
                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

            if len(self.price_history) > 1000:
                self.price_history.pop(0)

            return price_cny_g
        except Exception as e:
            print(f'获取价格失败: {e}')
            return None
