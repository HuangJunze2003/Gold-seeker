from flask import Flask, render_template, jsonify
from data_fetcher import GoldDataFetcher
from strategy import TradingStrategy
from trader import AutoTrader
import threading
import time

app = Flask(__name__)

# 配置区域: 模式选择
# 0: 模拟自动交易 (支持杠杆统计)
# 1: 金融平台真实秒级交易
MODE = 0 
LEVERAGE = 100.0 # 模拟模式下的杠杆

fetcher = GoldDataFetcher()
strategy = TradingStrategy()
trader = AutoTrader(initial_balance=10000, leverage=LEVERAGE) # 可在此传入杠杆

# 真实交易实例 (需传入真实 API Key)
from real_trader_broker import RealBroker
real_broker = RealBroker(api_key="YOUR_API_KEY", secret="YOUR_SECRET")

def update_data():
    while True:
        fetcher.fetch_price()
        analysis = strategy.analyze(fetcher.price_history)
        
        signal = analysis['signal']
        price = analysis.get('price', 0)
        
        if signal != 'HOLD':
            if MODE == 0:
                # 模拟交易逻辑 (trader.py 已支持杠杆和盈亏统计)
                result = trader.execute(signal, price)
                if result:
                    print(f"[模拟交易] {result} - {analysis['reason']}")
            
            elif MODE == 1:
                # 真实秒级交易逻辑 (real_trader_broker.py)
                print(f"[真实策略触发] {signal} @ {price}")
                order_res = real_broker.execute_order(signal, "XAUCNY", price, 10.0)
                if order_res.get('status') == 'success':
                    print(f"[真实成交] {signal} 成功: ID {order_res.get('order_id')}")
        
        time.sleep(10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    analysis = strategy.analyze(fetcher.price_history)
    return jsonify({
        'history': fetcher.price_history[-50:],
        'analysis': analysis,
        'trader': trader.get_status()
    })

if __name__ == '__main__':
    threading.Thread(target=update_data, daemon=True).start()
    app.run(debug=True, port=5000)
