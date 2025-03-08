# Test code for IEEE course final project
# Fan Cheng, 2024

import minimatrix as mm

#Test your code here!
# The following code is only for your reference
# Please write the test code yourself
#test1 测试Matrix类的各个操作
mat = mm.Matrix(data=[[1, 2, 3], [6, 5, 4], [7, 8, 9]])
print("Test mat.shape() here: ")
print(mat.shape())

print("Test mat.reshape((1, 9)) here: ")
print(mat.reshape((1, 9)))
print("Test mat.reshape((9, 1)) here: ")
print(mat.reshape((9, 1)))

test_mat = mm.Matrix(data = [[2, 4, 1], [3, 2, 3], [1, 5, 4]])
print("Test mat.dot(test_mat) here: ")
print(mat.dot(test_mat))

print("Test mat.T() here: ")
print(mat.T())

print("Test mat.sum(), mat.sum(0), mat.sum(1) here: ")
print(mat.sum())
print(mat.sum(0))
print(mat.sum(1))

print("Test mat.copy() here: ")
print(mat.copy())

print("Test mat.Kronecker_product(test_mat) here: ")
print(mat.Kronecker_product(test_mat))

print("Test getitem here: ([1, 2], [0:2, 1:2], [:1, 1:], [:, :])")
print(mat[1, 2])
print(mat[0:2, 1:2])
print(mat[:1, 1:])
print(mat[:, :])

print("Test setitem here: [1, 2] = 0  [:, :] = [[2, 4, 3], [3, 3, 0], [5, 4, 1]]  [:, :] = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]")
mat[1, 2] = 0
print(mat)
mat[:, :] = mm.Matrix(data=[[2, 4, 3], [3, 3, 0], [5, 4, 1]])
print(mat)
mat[:, :] = mm.Matrix(data=[[1, 2, 3], [6, 5, 4], [7, 8, 9]])
print(mat)


print("Test **, +, -, * here: ")
print(mat ** 3)
print(mat + mat)
test_mat_2 = mm.Matrix(data=[[2,4,3], [1,7,7], [3,2,5]])
print(test_mat_2 - mat)
print(test_mat_2 * mat)

print("Test len, str here: ")
print(len(mat))
print(mat)

print("Test det, inverse, rank here: ")
print(mat.det())
print(mat.inverse())
print(mat.rank())


#test2
print("Test m24_2 here:")
m24 = mm.arange(0, 24)
print(f"hhh{m24}")
print(m24.reshape((3, 8)))
print(m24.reshape((24, 1)))
print(m24.reshape((4, 6)))

#test3
print(mm.zeros((3,3)))
print(mm.zeros_like(m24))

#test4
print(mm.ones((3,3)))
print(mm.ones_like(m24))

#test5
print(mm.nrandom((3,3)))
print(mm.nrandom_like(m24))

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
print(w_)
print(w)
print(w - w_)
