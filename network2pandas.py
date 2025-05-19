import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み
# ここにcsvファイル名を入れる
df = pd.read_csv('ping_results_complete.csv')

# time_ms 列の平均と分散の計算
mean_time = df['time_ms'].mean()
var_time = df['time_ms'].var()

print(f"平均応答時間: {mean_time:.3f} ms")
print(f"応答時間の分散: {var_time:.6f} ms^2")

# グラフの描画
plt.figure(figsize=(10, 5))
plt.plot(df['icmp_seq'], df['time_ms'], marker='o', linestyle='-', label='Ping time')
plt.axhline(mean_time, color='red', linestyle='--', label=f'Mean: {mean_time:.3f} ms')
plt.title('Ping応答時間 (icmp_seq vs time_ms)')
plt.xlabel('icmp_seq')
plt.ylabel('time (ms)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
