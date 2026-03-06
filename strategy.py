from indicators import TechnicalIndicators

class TradingStrategy:
    def __init__(self):
        self.position = None  # 'long', 'short', None
        self.entry_price = 0

    def analyze(self, prices):
        if len(prices) < 30:
            return {'signal': 'HOLD', 'reason': '数据不足'}

        price_list = [p['price'] for p in prices]
        current_price = price_list[-1]

        ma5 = TechnicalIndicators.calculate_ma(price_list, 5)
        ma20 = TechnicalIndicators.calculate_ma(price_list, 20)
        rsi = TechnicalIndicators.calculate_rsi(price_list, 14)

        signal = 'HOLD'
        reason = ''

        # 金叉买入
        if ma5 > ma20 and rsi < 70 and not self.position:
            signal = 'BUY'
            reason = f'MA5({ma5:.2f}) > MA20({ma20:.2f}), RSI={rsi:.1f}'
            self.position = 'long'
            self.entry_price = current_price

        # 死叉卖出
        elif ma5 < ma20 and self.position == 'long':
            signal = 'SELL'
            reason = f'MA5({ma5:.2f}) < MA20({ma20:.2f})'
            self.position = None

        # RSI超买卖出
        elif rsi > 80 and self.position == 'long':
            signal = 'SELL'
            reason = f'RSI超买={rsi:.1f}'
            self.position = None

        return {
            'signal': signal,
            'reason': reason,
            'price': current_price,
            'ma5': ma5,
            'ma20': ma20,
            'rsi': rsi
        }
