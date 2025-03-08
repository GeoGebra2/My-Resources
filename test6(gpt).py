import numpy as np
import minimatrix as mm

m = 100
n = 10
X = np.random.rand(m, n)
w = np.random.rand(n, 1)
e = np.random.rand(m, 1)
e -= np.mean(e)  # 调整为零均值
Y = X.dot(w) + e
X_T = X.T
A = np.dot(X_T, X)
inv_A = np.linalg.inv(A)
B = np.dot(inv_A, X_T)
w_ = np.dot(B, Y)
print(w_)
print(w)
print(w - w_)