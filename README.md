# 💰 黄金自动化交易监控系统 (Gold Trading Monitor)

这是一个基于 Python 的轻量级黄金行情监控与自动化交易策略系统。支持实时抓取上海黄金交易所 (SGE) 数据，提供技术指标分析，并通过 Web 界面直观展示。

## 🚀 核心功能
- **实时行情**：高频采集 AU9999 现货价格。
- **技术策略**：内置 MA (5/20) 趋势跟踪策略与 RSI 强弱指标过滤。
- **决策建议**：自动触发“金叉/死叉”信号，提供即时交易建议。
- **Web 可视化**：基于 Flask 与 Chart.js 的响应式监控面板。
- **解耦设计**：模块化架构，易于扩展更多交易品种或策略。

## 🛠️ 技术架构
- **数据层** (`data_fetcher.py`)：异步采集上海黄金交易所实时行情。
- **指标层** (`indicators.py`)：计算移动平均线 (MA) 与相对强弱指数 (RSI)。
- **策略层** (`strategy.py`)：执行多维度策略撮合逻辑。
- **执行层** (`trader.py`)：统一的下单逻辑接口。
- **表现层** (`app.py` & `templates/`)：提供监控 API 及仪表盘前端。

## 📦 快速部署

### 1. 安装依赖
确保已安装 Python 3.8+ 环境：
```bash
pip install -r requirements.txt
```

### 2. 启动系统
```bash
python app.py
```
默认访问地址：[http://localhost:5000](http://localhost:5000)

## 📁 目录说明
- `app.py` - Flask 应用主程序
- `data_fetcher.py` - SGE 接口适配层
- `indicators.py` - 技术分析工具包
- `strategy.py` - 核心交易逻辑
- `trader.py` - 交易执行
- `templates/` - Web 页面模板
- `requirements.txt` - 项目依赖清单

---
*注：本系统仅供策略研究与行情监控使用，实盘操作风险自担。*

