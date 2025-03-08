import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设定参数
mu1, mu2 = 0, 10  # 高斯分布的均值
sigma1, sigma2 = 2, 2  # 高斯分布的标准差
p = 0.7  # 混合比例
n = 1000

# 设置随机种子以便于结果复现
#np.random.seed(42)

# 生成100个符合N(0, 1)的随机变量
for n in [2,3,4,5,10,20,50,100,5000]:
    for mu2 in [10,50,100,1000]:
        values = [0, 1]
        probabilities = [1-p, p]
        EZ = mu1 * (1 - p) + p*(mu1 + mu2)
        DZ = (sigma1**2) + p * (sigma2**2) + p * (1-p) * (mu2)**2
        U = []
        for i in range(1000):
            x = np.random.normal(mu1, sigma1, n)
            y = np.random.normal(mu2, sigma2, n)
            a = np.random.choice(values, size = n, p=probabilities)
            z = x + a*y
            U1 = (z.sum() - n * EZ) / (n * DZ)**0.5
            U.append(U1)

        U = np.array(U)

        # 画出频率分布直方图
        sns.histplot(U,bins=30,kde=True,color='black')
        #plt.hist(U, bins=50, density=True, alpha=0.6)
        plt.title(f'Mixed Gaussian Distribution\n ($\mu_1 = {mu1}$, $\sigma_1 = {sigma1}$, $\mu_2 = {mu2}$, $\sigma_2 = {sigma2}$, $p = {p}$, $n = {n}$)')
        plt.xlabel('U Value')
        plt.ylabel('Frequency')
        plt.savefig(f'D:/概率论与数理统计/大作业/Task1/mu1 = {mu1}_sigma1 = {sigma1}_mu2 = {mu2}_sigma2 = {sigma2}_p = {p}_n = {n}.jpg')

        plt.show()