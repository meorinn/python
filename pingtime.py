import pandas as pd
import matplotlib.pyplot as plt

# RTTデータをCSVとして読み込む（1列目にRTT値だけ入っていると仮定）
df = pd.read_csv("ping_times.csv", names=["RTT"])

# 基本統計量
print(df.describe())

# ヒストグラム（遅延分布）
plt.hist(df["RTT"], bins=20, edgecolor='black')
plt.title("RTT Distribution")
plt.xlabel("RTT (ms)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
