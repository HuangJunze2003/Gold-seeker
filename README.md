# 黄金自动化交易系统

## 功能
- 实时监测上海黄金交易所AU9999价格
- 技术指标：MA5、MA20、RSI
- 交易策略：金叉买入、死叉卖出、RSI超买卖出
- Web实时监控界面

## 安装

### 方法1：使用pip（推荐）
```bash
pip install -r requirements.txt
```

### 方法2：如果conda镜像源有问题
```bash
# 切换到默认源
conda config --remove-key channels
# 或使用pip
pip install requests flask pandas numpy
```

## 运行
```bash
python app.py
```

访问 http://localhost:5000

## 文件说明
- `data_fetcher.py` - 价格数据获取
- `indicators.py` - 技术指标计算
- `strategy.py` - 交易策略
- `app.py` - Web服务器
- `templates/index.html` - 监控界面
