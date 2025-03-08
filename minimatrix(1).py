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
            return "Error. 这两个矩阵不可点乘。"
        
        result = []
        for i in range(self.dim[0]):
            result.append([])

        for i in range(self.dim[0]):
            for j in range(other.dim[1]):
                sum = 0
                for k in range(self.dim[1]):
                    #sum += self.data[i][k] * other.data[k][j]
                    sum = round(sum + self.data[i][k] * other.data[k][j], 8)
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
        a = self.copy()
        if a.dim[0] != a.dim[1]:
            raise ValueError("Error, this matrix cannot multiply itself.")        
        else:
            for i in range(n-1):
                a = a.dot(a)
        return a
    
    def __add__(self,other):
        if self.dim != other.dim:
            raise ValueError("Error, these two matrix cannot addup.")
        else:
            ans = []
            for i in range(self.dim[0]):
                ans.append([])
                for j in range(self.dim[1]):
                    ans[i].append(self.data[i][j] + other.data[i][j])
            return Matrix(data=ans)
    
    def __sub__(self,other):
        if self.dim != other.dim:
            raise ValueError("Error, these two matrix cannot do subtraction.")
        else:
            ans = []
            for i in range(self.dim[0]):
                ans.append([])
                for j in range(self.dim[1]):
                    ans[i].append(self.data[i][j] - other.data[i][j])
            return Matrix(data=ans)
        
    def __mul__(self,other):
        if self.dim != other.dim:
            raise ValueError("Error, these two matrix cannot do multiplication.")
        else:
            ans = []
            for i in range(self.dim[0]):
                ans.append([])
                for j in range(self.dim[1]):
                    ans[i].append(self.data[i][j]*other.data[i][j])
            return Matrix(data=ans)


    def __len__(self):
        return self.dim[0] * self.dim[1]

    def __str__(self):
        s = "["
        max_length = max(len(str(self.data[i][j])) for i in range(self.dim[0]) for j in range(self.dim[1]))
        for i in range(self.dim[0]):
            s += "["
            for j in range(self.dim[1]):
                s = s + "{:>{}}".format(str(self.data[i][j]), max_length+1) ###changed!!!
            s = s + "]"
            if i < (self.dim[0] - 1):
                s += "\n "
        s += "]"
        return s
    
    def det(self):
        global det_num
        if self.dim[0] != self.dim[1]:
            return "Error. 此矩阵不是方阵."

        matrix = []
        for i in range(self.dim[0]):
            matrix.append([])
            for j in range(self.dim[1]):
                matrix[i].append(self.data[i][j])
        
        matrix = gauss(matrix)

        result = 1
        for i in range(len(matrix)):
            result *= matrix[i][i]
            result = round(result, 8)  ##############ROUND HERE
        result *= det_num
        result = round(result, 8)  ##############ROUND HERE

        if result == 0: #避免出现-0这样奇奇怪怪的东西
            return 0

        return result

    def inverse(self):
        if self.dim[0] != self.dim[1]:
            return "Error. 此矩阵不是方阵."

        matrix = []
        for i in range(self.dim[0]):
            matrix.append([])
            for j in range(self.dim[1]):
                matrix[i].append(self.data[i][j]) ##here change

        identity = I(self.dim[0])
        matrix = [matrix[i] + identity[i] for i in range(self.dim[0])]
        
        matrix = simple_inv_gauss(matrix)

        if matrix[self.dim[0] - 1][self.dim[1] - 1] == 0:
            return "Error. 此方阵不可逆。"

        result = [row[self.dim[0]:] for row in matrix]
        return Matrix(data=result)
    
    def inverse_2(self):
        if self.dim[0] != self.dim[1]:
            return "Error. 此矩阵不是方阵."

        matrix = []
        for i in range(self.dim[0]):
            matrix.append([])
            for j in range(self.dim[1]):
                matrix[i].append(self.data[i][j]) ##here change

        identity = I(self.dim[0])
        matrix = [matrix[i] + identity[i] for i in range(self.dim[0])]
        
        matrix = gauss(matrix)

        if matrix[self.dim[0] - 1][self.dim[1] - 1] == 0:
            return "Error. 此方阵不可逆。"

        result = [row[self.dim[0]:] for row in matrix]
        return Matrix(data=result)
    

    def rank(self):
        matrix = []
        for i in range(self.dim[0]):
            matrix.append([])
            for j in range(self.dim[1]):
                matrix[i].append(self.data[i][j])

        matrix = gauss(matrix)

        for i in range(self.dim[0]):
            if is_all_zero(matrix[i]):
                break

        if i == self.dim[0] -1 and not is_all_zero(matrix[i]):
            return i + 1

        return i    

########################################################################################
########################################################################################
##Gauss:
#高斯消元主函数
def gauss(array):
    global det_num #用于记录行列式的变化
    det_num = 1
    array = change_to_stair(array) #首先化为阶梯型
    array = change_to_simple(array) #然后化为简化阶梯形
    return array


def is_all_zero(lst): #判断某一行是否全为零
    for i in lst:
        if abs(i) > 1e-14:
            return False
    return True

def switch_line(array, k): #用于判断某行第k个元素是否为零，若是，则通过行交换将其变为非零
    global det_num
    for i in range(k, len(array)):
        if abs(array[i][0]) > 1e-14:
            array[k], array[i] = array[i], array[k] 
            if i != k:
                det_num *= -1
            break
    return array

def delete_num(array, k): #将某列在k行一下的元素全变为零
    #寻找主元
    for j in range(len(array[k])):
        if array[k][j] != 0:
            if abs(array[k][j]) < 1e-14:
                array[k][j] = 0
                continue
            else:
                break

    if array[k][j] == 0:
        return array

    #消去j列k行之下的元素
    for x in range(k+1, len(array)):
        for y in range(len(array[x])-1, j-1, -1):
            array[x][y] = round(array[x][y] - ((array[x][j] / array[k][j]) * array[k][y]), 8)

    array[k] = trans_to_one(array[k])
    return array

def trans_to_one(lst): #将某行主元化为1
    global det_num
    #寻找主元
    for s in range(len(lst)):
        if lst[s] != 0:
            if abs(lst[s]) < 1e-14:
                lst[s] = 0
                continue
            else:
                break

    #判断是否此行全为零
    if lst[s] == 0: #注：用极小数是为了防止浮点数造成的误差
        return lst

    det_num *= lst[s]

    #主元化为1
    for t in range(len(lst)-1, s-1, -1):
        lst[t] = round(lst[t] / lst[s], 8)
    return lst

def change_to_stair(array): #变为阶梯形
    for i in range(len(array)-1):
        array = switch_line(array, i) #先交换行
        array = delete_num(array,i) #再消去主元

    array[len(array)-1] = trans_to_one(array[len(array)-1])
    return array

def change_to_simple(array): #变为简化阶梯形
    #寻找主元
    for i in range(len(array)-1, -1, -1):
        for j in range(len(array[i])):
            if abs(array[i][j]) > 1e-14:
                break

        if abs(array[i][j]) < 1e-14:
            array[i][j] = 0
            continue
    
        #消去每一列主元以上的元素
        for q in range(i-1, -1, -1):
            for p in range(len(array[i])-1, j-1, -1):
                array[q][p] = round(array[q][p] - (array[q][j] / array[i][j]) * array[i][p], 8)
    return array

#为了一个test,写了一个函数
def simple_inv_gauss(matrix):
    n = len(matrix)
    for col in range(n):
        for row in range(col + 1, n):
            if matrix[row][col] != 0:
                factor = round(matrix[col][col] / matrix[row][col], 8)
                matrix[row] = [round(matrix[col][i] - factor * matrix[row][i], 8) for i in range(2*n)]

    for col in range(n-1, -1, -1):
        if matrix[col][col] == 0:
            return "Matrix is singular, no unique inverse exists."
        factor = matrix[col][col]
        matrix[col] = [round(entry / factor, 8) for entry in matrix[col]]
        
    for col in range(n-1, -1, -1):
        for row in range(col - 1, -1, -1):
            
            factor = matrix[row][col]
            
            matrix[row] = [round(matrix[row][i] - factor * matrix[col][i], 8) for i in range(2*n)]
            
    return matrix

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

def arange(start,end,step=1):
    ans = [[]]
    for i in range(start,end,step):
        ans[0].append(i)
    return Matrix(data=ans)

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
            random_number = round(random.uniform(0, 1), 8)
            matrix[i].append(random_number) ###changed back!!!!
    return Matrix(data=matrix)


def nrandom_like(matrix):
    return nrandom(matrix.dim)

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

def zero_mean(e):
    sum = 0
    for i in range(e.dim[0]):
        sum += e.data[i][0]
    average = sum/e.dim[0]
    for i in range(e.dim[0]):
        e.data[i][0] -= average
    return e


if __name__ == "__main__":
    print("test here")
    pass

