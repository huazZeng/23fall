import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("lab2\data-3.csv",names=["size", "time for naive","time for improvedstrassen"])
average_values_naive = df.groupby("size")["time for naive"].mean()

average_values_strassen=df.groupby("size")["time for naive"].mean()
average_values_strassen_improved=df.groupby("size")["time for improvedstrassen"].mean()
plt.figure(figsize=(10, 6))
plt.plot(average_values_naive.index,average_values_strassen_improved/average_values_naive, marker='o', linestyle='--')
plt.xlabel("size")
plt.ylabel("k")
plt.title("")
plt.show()
