from tkinter import font
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
sns.set_style({"font.sans-serif": "SimHei"})

data = [
    ["张三", 24],
    ["李四", 18],
    ["王五", 37],
    ["小芳", 24],
    ["小红", 12],
    ["小明", 42],
    ["小华", 56],
    ["小莉", 67],
    ["小英", 45],
    ["小军", 82]
]
df = pd.DataFrame(data, columns = ["姓名", "年龄"])

sns.violinplot(data=df, y="年龄")
plt.show()