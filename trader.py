class AutoTrader:
    def __init__(self, initial_balance=10000, leverage=1.0):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.leverage = leverage
        self.position = 0  # 持仓克数
        self.avg_cost = 0  # 平均持有成本
        self.trades = []
        self.pnl_history = []  # 记录盈亏历史

    def execute(self, signal, price):
        if signal == 'BUY' and self.balance > 0:
            # 使用杠杆计算最大可买克数
            buying_power = self.balance * self.leverage
            amount = buying_power / price
            self.position += amount
            self.avg_cost = price
            # 扣除保证金，这里简单模拟：买入后 balance 减少为 0，实际由保证金维持
            self.balance = 0 
            self.trades.append({'type': 'BUY', 'price': price, 'amount': amount, 'time': self.get_now()})
            return f'买入 {amount:.2f}克 (杠杆 {self.leverage}x) @ ¥{price:.2f}'

        elif signal == 'SELL' and self.position > 0:
            # 卖出总价
            sell_value = self.position * price
            # 计算成本
            cost_value = self.position * self.avg_cost
            # 计算盈亏 (如果是杠杆交易，盈亏直接体现在 balance 上)
            pnl = (price - self.avg_cost) * self.position
            
            # 回笼资金：初始被扣掉的保证金 + 盈亏
            self.balance = self.initial_balance + pnl
            self.initial_balance = self.balance # 更新基准余额以便下次计算
            
            amount = self.position
            self.position = 0
            self.avg_cost = 0
            self.trades.append({'type': 'SELL', 'price': price, 'amount': amount, 'time': self.get_now(), 'pnl': round(pnl, 2)})
            self.pnl_history.append({'pnl': pnl, 'time': self.get_now()})
            return f'卖出 {amount:.2f}克 @ ¥{price:.2f}, 盈亏: ¥{pnl:.2f}'

        return None

    def get_status(self):
        return {
            'balance': round(self.balance, 2),
            'position': round(self.position, 2),
            'avg_cost': round(self.avg_cost, 2),
            'leverage': self.leverage,
            'pnl_total': sum(t.get('pnl', 0) for t in self.trades),
            'trades': self.trades
        }

    def get_now(self):
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
