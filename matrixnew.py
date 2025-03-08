import random

class Matrix:
    def __init__(self,data = None,dim = None,init_value = 0) -> None:
        if data is not None:
            self.data = data
            self.dim = (len(self.data),len(self.data[0]))
        else:
            if dim is None:
                raise ValueError("Error,it cannot form a matrix.")
            else:
                self.data = [[init_value for i in range(dim[1])] for i in range(dim[0])]
                self.dim = dim
        
    
    def shape(self):
        return self.dim

    def reshape(self, newdim):
        if newdim[0] * newdim[1] != self.dim[0] * self.dim[1]:
            return "Error."
        
        tem = [0 for k in range(self.dim[0] * self.dim[1])]
        x = 0
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                tem[x] = self.data[i][j]
                x += 1

        x = 0
        new_data = []
        for i in range(newdim[0]):
            new_data.append([])

        for i in range(newdim[0]):
            for j in range(newdim[1]):
                new_data[i].append(tem[x])
                x += 1

        return Matrix(data=new_data)

    def dot(self, other):
        if self.dim[1] != other.dim[0]:
            return "Erroe. 这两个矩阵不可点乘。"
        
        result = []
        for i in range(self.dim[0]):
            result.append([])

        for i in range(self.dim[0]):
            for j in range(other.dim[1]):
                sum = 0
                for k in range(self.dim[1]):
                    sum += self.data[i][k] * other.data[k][j]
                result[i].append(sum)

        return Matrix(data=result)

    def T(self):
        result = []
        for i in range(self.dim[1]):
            result.append([])
        
        for j in range(self.dim[1]):
            for i in range(self.dim[0]):
                result[j].append(self.data[i][j])

        return Matrix(data=result)

    def sum(self, axis=None):
        if axis == None:
            sum = 0
            for i in self.data:
                for j in i:
                    sum += j
            return Matrix(data=[[sum]])

        elif axis == 0:
            result = [[0 for x in range(self.dim[1])]]
            for i in range(self.dim[1]):
                for j in range(self.dim[0]):
                    result[0][i] += self.data[j][i]
            return Matrix(data=result)

        elif axis == 1:
            result = [[0] for x in range(self.dim[0])]
            for i in range(self.dim[0]):
                for j in range(self.dim[1]):
                    result[i][0] += self.data[i][j]
            return Matrix(data=result)

        else:
            return "Error. Please input 1 or 0."

    def copy(self):
        B = Matrix(data=self.data, dim=self.dim)
        return B

    def Kronecker_product(self, other):
        result = []
        for i in range(self.dim[0] * other.dim[0]):
            result.append([])

        for i in range(self.dim[0] * other.dim[0]):
            for j in range(self.dim[1] * other.dim[1]):
                result[i].append(\
                    self.data[i // other.dim[0]][j // other.dim[1]] \
                    * other.data[i % other.dim[0]][j % other.dim[1]])
        return Matrix(data=result)

    def __getitem__(self,key):
        x = self.data
        if type(key[0]) == int and type(key[1]) == int: #单值索引
            if key[0] >= len(x) or key[1] >= len(x[0]):
                raise IndexError("Error,index out of range.")
            else:
                return x[key[0]][key[1]] 
        else: #矩阵切片
            if key[0].start == None:
                a = 0
            else:
                a = key[0].start

            if key[0].stop == None or key[0].stop > self.dim[0]:
                b = self.dim[0]
            else:
                b = key[0].stop

            if key[1].start == None:
                c = 0
            else:
                c = key[1].start

            if key[1].stop == None or key[1].stop > self.dim[1]:
                d = self.dim[1]
            else:
                d = key[1].stop

            if a >= len(x) or c >= len(x[0]):
                raise IndexError("Error,index out of range.") 
                
            ans = []
            for i in range(b - a):
                ans.append([])
                for j in range(c,d):
                    ans[i].append(x[a + i][j])
            return Matrix(data=ans)
            
            
    def __setitem__(self, key, value):
        if type(key[0]) == int and type(key[1]) == int:
            if key[0] >= self.dim[0] or key[1] >= self.dim[1]:
                raise IndexError("Error, index out of range.")
            else:
                self.data[key[0]][key[1]] = value
                return
        else:
            if key[0].start == None:
                a = 0
            else:
                a = key[0].start

            if key[0].stop == None or key[0].stop > self.dim[0]:
                b = self.dim[0]
            else:
                b = key[0].stop

            if key[1].start == None:
                c = 0
            else:
                c = key[1].start

            if key[1].stop == None or key[1].stop > self.dim[1]:
                d = self.dim[1]
            else:
                d = key[1].stop

            if a >= self.dim[0] or c >= self.dim[1]:
                raise IndexError("Error,index out of range.") 

            if value.dim != (b-a, d-c):
                return "Error. The dim of value is different from the dim of the slice."

            for i in range(value.dim[0]):
                for j in range(value.dim[1]):
                    self.data[a + i][c + j] = value.data[i][j]
            return
                
    
    def __pow__(self,n):
        a = self.data
        if len(a) != len(a[0]):
            raise ValueError("Error, this matrix cannot multiply itself.")        
        else:
            for i in range(n-1):
                a = a.dot(a)
        return Matrix(data=a)
    
    def __add__(self,other):
        if self.dim != other.dim:
            raise ValueError("Error, these two matrix cannot addup.")
        else:
            ans = []
            for i in range(self.dim[0]):
                ans.append([])
                for j in range(self.dim[1]):
                    ans[i].append(self.dim[i][j] + other.dim[i][j])
            return Matrix(data=ans)
    
    def __sub__(self,other):
        if self.dim != other.dim:
            raise ValueError("Error, these two matrix cannot do subtraction.")
        else:
            ans = []
            for i in range(self.dim[0]):
                ans.append([])
                for j in range(self.dim[1]):
                    ans[i].append(self.dim[i][j] - other.dim[i][j])
            return Matrix(data=ans)
        
    def __mul__(self,other):
        if self.dim != other.dim:
            raise ValueError("Error, these two matrix cannot do multiplication.")
        else:
            ans = []
            for i in range(self.dim[0]):
                ans.append([])
                for j in range(self.dim[1]):
                    ans[i].append(self.dim[i][j]*other.dim[i][j])
            return Matrix(data=ans)


#    def __pow__(self, n):
#        if self.dim[0] != self.dim[1]:
#            return "Error. 此矩阵不是方阵"
#
#        if n == 0:
#            result = []
#            for i in range(self.dim[0]):
#                result.append([0 for x in range(self.dim[1])])
#            for i in range(self.dim[0]):
#                result[i][i] = 1
#            return Matrix(data=result)

#        half_pow = self ** (n//2)

#        if n % 2 == 0:
#            return half_pow.dot(half_pow)
#        else:
#            return self.dot(half_pow.dot(half_pow))


    def __len__(self):
        return self.dim[0] * self.dim[1]

    def __str__(self):
        s = "["
        for i in range(self.dim[0]):
            s += "["
            for j in range(self.dim[1]):
                s = s + "{:>5}".format(str(self.data[i][j]))
            s = s + "]"
            if i < (self.dim[0] - 1):
                s += "\n "
        s += "]"
        return s
    
    def det(self):
        global det_num
        if self.dim[0] != self.dim[1]:
            return "Error. 此矩阵不是方阵."

        matrix = gauss(self.data)

        result = 1
        for i in range(len(matrix)):
            result *= matrix[i][i]
        result *= det_num
        print(det_num)

        return result

    def inverse(self):
        if self.dim[0] != self.dim[1]:
            return "Error. 此矩阵不是方阵."

        matrix = self.data
        
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                matrix[i].append(0)
            matrix[i][i + self.dim[1]] = 1
        
        matrix = gauss(matrix)

        if is_all_zero(matrix[-1]):
            return "Error. 此方阵不可逆。"

        result = []
        for i in range(len(matrix)):
            temp = [matrix[i][j] for j in range(self.dim[1], len(matrix[i]))]
            result.append(temp)

        return Matrix(data=result)

    def rank(self):
        matrix = gauss(self.data)

        for i in range(self.dim[0]):
            if is_all_zero(matrix[i]):
                break

        if i == self.dim[0] -1 and not is_all_zero(matrix[i]):
            return i + 1

        return i    
    
    def inverse1(self):
        if self.dim[0] != self.dim[1]:
            raise Exception("该矩阵非方阵")

        matrix = self.copy()
        inverse = Matrix(dim=self.dim)
        for i in range(self.dim[0]):
            inverse[i][i] = 1
        for i in range(matrix.dim[0]):
            for j in range(i, matrix.dim[0]):
                if matrix[j][i] != 0:
                    if i != j:
                        matrix[i], matrix[j] = matrix[j], matrix[i]
                        inverse[i], inverse[j] = inverse[j], inverse[i]
                    break
            if matrix[i][i] == 0:
                raise Exception("该矩阵无逆矩阵")
            for j in range(matrix.dim[0]):
                if j != i:
                    k = matrix[j][i] / matrix[i][i]
                    for p in range(matrix.dim[1]):
                        matrix[j][p] -= k * matrix[i][p]
                        inverse[j][p] -= k * inverse[i][p]
        for i in range(matrix.dim[0]):
            k = 1 / matrix[i][i]
            for j in range(matrix.dim[1]):
                inverse[i][j] *= k

        return inverse

    def rank1(self):
        matrix = self.copy
        free = 0
        rowmain = 0
        colmain = 0
        while rowmain < matrix.dim[0] and colmain < matrix.dim[1]:
            for i in range(rowmain, matrix.dim[0]):
                if matrix[i][colmain] != 0:
                    if rowmain != i:
                        matrix[rowmain], matrix[i] = matrix[i], matrix[rowmain]
                    break
            if matrix[rowmain][colmain] == 0:
                free += 1
                colmain += 1
                continue
            for i in range(colmain + 1, matrix.dim[0]):
                k = matrix[i][colmain] / matrix[rowmain][colmain]
                for j in range(matrix.dim[1]):
                    matrix[i][j] -= k * matrix[rowmain][j]
            rowmain += 1
            colmain += 1
        if matrix.dim[1] - free > matrix.dim[0]:
            free = matrix.dim[1] - matrix.dim[0]

        return matrix.dim[1] - free

########################################################################################
########################################################################################
##Gauss:
def is_all_zero(lst):
    for i in lst:
        if i != 0:
            return False
    return True

def switch_line(array, k):
    global det_num
    for i in range(k, len(array)):
        if array[i][0] != 0:
            #print(f"before array : {array}, {det_num}")
            array[k], array[i] = array[i], array[k]
            if i != k:
                det_num *= -1
            #print(f"after array : {array}, {det_num}")
            break
    return array

def delete_num(array, k):
    for j in range(len(array[k])):
        if array[k][j] != 0:
            break

    for x in range(k+1, len(array)):
        for y in range(len(array[x])-1, j-1, -1):
            if array[k][j] == 0:
                return array
            array[x][y] -= ((array[x][j] / array[k][j]) * array[k][y])
    array[k] = trans_to_one(array[k])
    return array

def trans_to_one(lst):
    global det_num
    for s in range(len(lst)):
        if lst[s] != 0:
            break

    if abs(lst[s]) < 1e-15:
        lst[s] = 0
        return lst

    #print(f"before array : {lst}, {det_num}")
    det_num *= lst[s]

    for t in range(len(lst)-1, s-1, -1):
        lst[t] /= lst[s]
    #print(f"after array : {lst}, {det_num}")
    return lst

def change_to_stair(array):
    for i in range(len(array)-1):
        array = switch_line(array, i)
        array = delete_num(array,i)

    array[len(array)-1] = trans_to_one(array[len(array)-1])
    return array

def change_to_simple(array):
    for i in range(1, len(array)):
        for j in range(len(array[i])):
            if array[i][j] != 0:
                break
        for q in range(i):
            for p in range(len(array[i])-1, j-1, -1):
                array[q][p] -= array[q][j] * array[i][p]
    return array

def gauss(array):
    global det_num
    det_num = 1
    array = change_to_stair(array)
    array = change_to_simple(array)
    return array

########################################################################################
########################################################################################

def I(n):
    ans = []
    for i in range(n):
        ans.append([])
        for j in range(n):
            ans[i].append(0) #打印出了一个n*n的零矩阵
    for i in range(n):
        ans[i][i] = 1 #将对角线上的元素改为1
    return ans
    
def narray(dim, init_value=1):
    ans = []
    for i in range(dim[0]):
        ans.append([])
        for j in range(dim[1]):
            ans[i].append(init_value)
    return Matrix(data=ans)

def arange(start,end,step):
    ans = []
    for i in range(start,end,step):
        ans.append(i)
    return Matrix(data=[ans])

def zeros(dim):
    ans = []
    for i in range(dim[0]):
        ans.append([])
        for j in range(dim[1]):
            ans[i].append(0)
    return Matrix(data=ans) 

def zeros_like(matrix):
    return Matrix(dim=matrix.dim,init_value=0)


def ones(dim):
    ans = []
    for i in range(dim[0]):
        ans.append([])
        for j in range(dim[1]):
            ans[i].append(1)
    return Matrix(data=ans)


def ones_like(matrix):
    return Matrix(dim=matrix.dim, init_value=1)

def nrandom(dim):
    matrix = []
    for i in range(dim[0]):
        matrix.append([])
        for j in range(dim[1]):
            matrix[i].append(random.uniform(-1, 1))
    return Matrix(data=matrix)


def nrandom_like(matrix):
    matrix_new = []
    for i in range(matrix.dim[0]):
        matrix_new.append([])
        for j in range(matrix.dim[1]):
            matrix_new[i].append(random.uniform(-1, 1))
        return Matrix(data=matrix_new)

#random.choice([0,1])?


#def nrandom_like(matrix):
    #return nrandom(matrix.dim)

def concatenate(items,axis=0):
    result = []
    if axis == 0:#在行上拼接
        pos = 0
        k = 0
        for x in items:
            if pos == 0:
                pos = x.dim[1]
            if pos != 0 and x.dim[1] != pos:
                raise Exception("矩阵们不匹配")
            k += x.dim[0]
        if len(result) == 0:
            result = Matrix(dim=(k,pos))
        p = 0
        for x in items:
            for i in range (x.dim[0]):
                for j in range (x.dim[1]):
                    result.data[p][j] = x.data[i][j]
                p+=1
            
    elif axis == 1:
        pos = 0
        k = 0
        for x in items:
            if pos == 0:
                pos = x.dim[0]
            if pos != 0 and x.dim[0] != pos:
                raise Exception("矩阵们不匹配")
            k += x.dim[1]
        if len(result) == 0:
            result = Matrix(dim=(pos,k))
        p = 0
        for x in items:
            for i in range(x.dim[0]):
                for j in range(x.dim[1]):
                    result.data[i][p] = x.data[i][j]
                    p+=1
    
    else:
        return "You entered the wrong axis."
    
    return result

def vectorize(func):
    def f(matrix):
        matrix_new = Matrix(dim=matrix.dim)
        for i in range(matrix.dim[0]):
            for j in range(matrix.dim[1]):
                matrix_new.data[i][j] = func(matrix.data[i][j])
        return matrix_new
    return f


if __name__ == "__main__":
    print("test here")
    pass


B = Matrix(data=[[1,2,3], [4,5,6], [7, 8, 9]])
C = Matrix(data=[[2, -1, 2], [5, -3, 3], [-1, 0, -2]])
print(B.inverse())
print(B.inverse1())
print(C.inverse())
print(C.inverse1())


