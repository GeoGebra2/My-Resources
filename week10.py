import numpy as np
import matplotlib.pyplot as plt

samplesize = 100
# （1）产生50个随机样本，样本容量为10
samples = np.array([np.random.poisson(lam = 2, size = samplesize) for _ in range(50)])

# （2）计算样本均值
sample_means = np.mean(samples, axis = 1)

# 画出50个样本均值的频率直方图
plt.hist(sample_means, bins = 10)
plt.xlabel('Sample Means')
plt.ylabel('Frequency')
plt.title('Histogram of 50 Sample Means from Poisson(2)' + f'(n = {samplesize})')
plt.show()