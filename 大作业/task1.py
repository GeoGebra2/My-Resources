import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设定参数
mu1 = 0
mu2 = 10 # 高斯分布的均值
sigma1 = 2
sigma2 = 2  # 高斯分布的标准差
p = 0.7  # 混合比例

# 设置随机种子以便于结果复现
#np.random.seed(42)
for sigma2 in [1,3,4,5,6]:
# 生成100个符合N(0, 1)的随机变量
    x = np.random.normal(mu1, sigma1, 5000)
    y = np.random.normal(mu2, sigma2, 5000)

    # 定义可能的值和它们的概率
    values = [0, 1]
    probabilities = [1-p, p]

    # 生成随机变量a
    a = np.random.choice(values, size = 5000, p=probabilities)

    z = x + a*y
    #print("ave: ", z.mean())
    #print("s: ", z.var())
    # 画出频率分布直方图
    #plt.hist(z, bins=70, density=True, alpha=0.6)
    sns.histplot(z,bins=30,kde=True,color='black')
    #plt.hist(U, bins=50, density=True, alpha=0.6)
    plt.title(f'Mixed Gaussian Distribution\n ($\mu_1 = {mu1}$, $\sigma_1 = {sigma1}$, $\mu_2 = {mu2}$, $\sigma_2 = {sigma2}$, $p = {p}$')
    #plt.title('Mixed Gaussian Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig(f'D:/概率论与数理统计/大作业/Task1/mu1 = {mu1}_sigma1 = {sigma1}_mu2 = {mu2}_sigma2 = {sigma2}_p = {p}$.jpg')
    plt.show()