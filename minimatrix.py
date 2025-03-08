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
    #print("gauss here")
    global det_num #用于记录行列式的变化
    det_num = 1
    array = change_to_stair(array) #首先化为阶梯型
    #print("point stair: ")
    #print(array)
    array = change_to_simple(array) #然后化为简化阶梯形
    #print("point simple: ")
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
        #print(f"row {x} from {array[x]}")
        for y in range(len(array[x])-1, j-1, -1):
            array[x][y] = round(array[x][y] - ((array[x][j] / array[k][j]) * array[k][y]), 8)
            #array[x][y] -= ((array[x][j] / array[k][j]) * array[k][y])
        #print(f"to {array[x]}")

    #print(f"point {k+1}:")
    #print(array)
    #print(f"row {k} from {array[k]}")
    array[k] = trans_to_one(array[k])
    #print(f"to {array[k]}")
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
        #lst[t] /= lst[s]
    return lst

def change_to_stair(array): #变为阶梯形
    for i in range(len(array)-1):
        array = switch_line(array, i) #先交换行
        array = delete_num(array,i) #再消去主元
        #print(f"stair point {i+1}:")
        #print(array)

    #print("before trans to one")
    #print(array[len(array)-1])
    array[len(array)-1] = trans_to_one(array[len(array)-1])
    #print("after trans to one")
    #print(array[len(array)-1])
    return array

def change_to_simple(array): #变为简化阶梯形
    #寻找主元
    for i in range(len(array)-1, -1, -1):
        #print(f"here comes row {i}")
        for j in range(len(array[i])):
            if abs(array[i][j]) > 1e-14:
                break

        if abs(array[i][j]) < 1e-14:
            array[i][j] = 0
            continue
    
        #消去每一列主元以上的元素
        for q in range(i-1, -1, -1):
            #print(f"row {q} from {array[q]}")
            for p in range(len(array[i])-1, j-1, -1):
                array[q][p] = round(array[q][p] - (array[q][j] / array[i][j]) * array[i][p], 8)
                #array[q][p] -= (array[q][j] / array[i][j]) * array[i][p]
            #print(f"to {array[q]}")
    return array

#为了一个test,写了一个函数
def simple_inv_gauss(matrix):
    #print("simple gauss here")
    n = len(matrix)
    for col in range(n):
        for row in range(col + 1, n):
            if matrix[row][col] != 0:
                factor = round(matrix[col][col] / matrix[row][col], 8)
                matrix[row] = [round(matrix[col][i] - factor * matrix[row][i], 8) for i in range(2*n)]
                #factor = matrix[col][col] / matrix[row][col]
                #matrix[row] = [matrix[col][i] - factor * matrix[row][i] for i in range(2*n)]
    #print("point before stair:")
    #print(matrix)


    for col in range(n-1, -1, -1):
        if matrix[col][col] == 0:
            return "Matrix is singular, no unique inverse exists."
        factor = matrix[col][col]
        matrix[col] = [round(entry / factor, 8) for entry in matrix[col]]
        #matrix[col] = [entry / factor for entry in matrix[col]]

    #print(f"point of stair: ")
    #print(matrix)
    
    for col in range(n-1, -1, -1):
        for row in range(col - 1, -1, -1):
            #print(f"col: {col}, row: {row}")
            factor = matrix[row][col]
            #print(f"factor: {factor}")
            #print(f"from {matrix[row]}")
            matrix[row] = [round(matrix[row][i] - factor * matrix[col][i], 8) for i in range(2*n)]
            #matrix[row] = [matrix[row][i] - factor * matrix[col][i] for i in range(2*n)]
            #print(f"to {matrix[row]}")
    
    #print("second point:")
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

#A = Matrix(data=[[32.447475517142976, 27.261463175942858, 23.254590200514897, 25.721887754063008,  24.54657462943868, 24.370926409925872,  25.78992739631079, 26.234079156305633, 22.961882946985956,  26.34452878027742],
# [27.261463175942858,  35.90372536371353,  23.50785371918095, 27.187726552181164,  26.25980018838251, 26.448557407834603,  30.32878519641164,   28.6776472777403,  24.16193592185215,  27.43749555582083],
# [23.254590200514897,  23.50785371918095, 26.733342745946114,  23.27695451635597, 22.006639185770677, 21.971757500224342,  23.72789848218398,  22.30206334976426, 20.482453030031763,  22.64570717985643],
# [25.721887754063008, 27.187726552181164,  23.27695451635597,  36.53256451067775,  26.76263282945961, 25.264333595618464, 30.279038109927544,  26.37246610570211,   24.1364291713755, 27.984376655947628],
# [24.54657462943868,  26.25980018838251, 22.006639185770677,  26.76263282945961,  33.88928756626949, 24.708215044912865, 27.799151949850966,  26.51581036674519, 23.288475076098464, 25.538470546403975],
# [24.370926409925872, 26.448557407834603, 21.971757500224342, 25.264333595618464, 24.708215044912865,  32.41983174849173,  27.59634084570275, 26.461004220420495, 22.017228244487754, 25.314975199626716],
# [25.78992739631079,  30.32878519641164,  23.72789848218398, 30.279038109927544, 27.799151949850966,  27.59634084570275,  38.48443299767611, 29.066214416217985, 24.168576067719524, 28.713413803020476],
# [26.234079156305633,   28.6776472777403,  22.30206334976426,  26.37246610570211,  26.51581036674519, 26.461004220420495, 29.066214416217985,   35.8985426811476, 22.061794144326456,  28.22680021821742],
# [22.961882946985956,  24.16193592185215, 20.482453030031763,   24.1364291713755, 23.288475076098464, 22.017228244487754, 24.168576067719524, 22.061794144326456, 29.272203032146408, 22.950589678581593],
# [26.34452878027742,  27.43749555582083,  22.64570717985643, 27.984376655947628, 25.538470546403975, 25.314975199626716, 28.713413803020476,  28.22680021821742, 22.950589678581593,  34.83104609504664]])

#print(A.inverse_1())
#print(A.inverse_2())