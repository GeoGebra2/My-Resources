import minimatrix_1 as mm
import numpy as np

#test6
m = 1000
n = 100
X = mm.nrandom((m, n))
w = mm.nrandom((n, 1))
e = mm.nrandom((m, 1))
e = mm.zero_mean(e)
Y = X.dot(w) + e
X_T = X.T()
A = X_T.dot(X)
inv_A = A.inverse()
B = inv_A.dot(X_T)
w_ = B.dot(Y)
print(w)
print(w_)
print(w - w_)


#inv_A_1 = A.inverse_1()

#inv_A_2 = A.inverse_2()
#print("after inv2")
#print(A)
#print("\n\n\ninv1")
#print(inv_A_1)
#print("\n\n\ninv2")
#print(inv_A_2)
#B_1 = inv_A_1.dot(X_T)
#B_2 = inv_A_2.dot(X_T)
#w_1 = B_1.dot(Y)
#print("here is w_1")
#print(w_1)
#print("here is w")
#print(w)
#print("here is w - w_1")
#print(w - w_1)
#w_2 = B_2.dot(Y)
#print("here is w_2")
#print(w_2)
#print("here is w - w_2")
#print(w - w_2)
