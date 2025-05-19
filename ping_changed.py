import re
import pandas as pd
import matplotlib.pyplot as plt

# ping結果のテキストを貼り付け
# ここにterminalの生データをコピペする
ping_output = """(
)"""

# icmp_seqとtimeを抽出する
pattern = r"icmp_seq=(\d+).*?time=([\d\.]+) ms"
matches = re.findall(pattern, ping_output)

# データフレーム化
data = pd.DataFrame(matches, columns=["icmp_seq", "time"])
data["icmp_seq"] = data["icmp_seq"].astype(int)
data["time"] = data["time"].astype(float)

# CSVに保存
data.to_csv("ping_data.csv", index=False)
print("ping_data.csv に保存しました。")

# 外れ値（2秒以上）を除外
df = pd.read_csv("ping_data.csv")
# filtered_df = df[df["time"] < 5]
filtered_df = df

# 平均と分散の計算
# 外れ値除去後の平均と分散
mean_time_filtered = filtered_df["time"].mean()
var_time_filtered = filtered_df["time"].var()

print(f"外れ値除去後の平均応答時間: {mean_time_filtered:.3f} ms")
print(f"外れ値除去後の分散: {var_time_filtered:.6f}")

# グラフ描画
plt.figure(figsize=(10, 6))
plt.plot(filtered_df["icmp_seq"], filtered_df["time"], label="Ping Time (ms)")
plt.axhline(y=mean_time_filtered, color='r', linestyle='--', label=f"Mean = {mean_time_filtered:.3f} ms")
plt.title("Ping Time vs ICMP Sequence")
plt.xlabel("ICMP Sequence")
plt.ylabel("Time (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("ping_graph.png")
plt.show()
