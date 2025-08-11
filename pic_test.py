import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import ta  # 技術分析工具包

# 下載台積電歷史資料（Yahoo 股票代碼為 2330.TW）
#df = yf.download("2330.TW", start="2024-08-01", end="2025-08-01")
df = yf.download("2330.TW", start="2025-01-01", end="2025-08-30")

# 計算移動平均線
df["MA5"] = df["Close"].rolling(window=5).mean()
df["MA20"] = df["Close"].rolling(window=20).mean()

close_price = df['Close'].squeeze()
#print(close_price)

# 計算 RSI (14)
rsi_14 = ta.momentum.RSIIndicator(close_price, window=14)
df["RSI_14"] = rsi_14.rsi()
rsi_6 = ta.momentum.RSIIndicator(close_price, window=6)
df["RSI_6"] = rsi_6.rsi()
print(df["RSI_14"])
print(df["RSI_6"])



# ========== 繪圖 ==========
plt.figure(figsize=(14, 8))

# 第一張子圖：股價與均線
plt.subplot(2, 1, 1)
plt.plot(df.index, df["Close"], label="Close", color="black")
plt.plot(df.index, df["MA5"], label="MA5", color="blue")
plt.plot(df.index, df["MA20"], label="MA20", color="red")
plt.title("(2330.TW)")
plt.legend()
plt.grid(True)

# 第二張子圖：RSI
plt.subplot(2, 1, 2)
plt.plot(df.index, df["RSI_14"], label="RSI (14)", color="purple")
plt.plot(df.index, df["RSI_6"], label="RSI (6)", color="red")
plt.axhline(70, color='red', linestyle='--', linewidth=1)
plt.axhline(50, color='orange', linestyle='-', linewidth=1)
plt.axhline(30, color='green', linestyle='--', linewidth=1)

#你可以強調 RSI 的超買超賣區域：
plt.fill_between(df.index, 70, 100, color='red', alpha=0.1)
plt.fill_between(df.index, 0, 30, color='green', alpha=0.1)

plt.title("RSI")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("plot.png") 
plt.show()


df.to_excel("2330_TW_technical_analysis.xlsx")

