import random

class Matrix:
    def __init__(self, data=None, dim=None, init_value= 0) -> None:
        self.data = data
        self.init_value = init_value
        if self.data == None:
            self.dim = dim
            #这里有一个未完成的初始化！！！  
        else:
            self.dim = (len(self.data), len(self.data[0]))
        
    def __repr__(self) -> str:
        return self.data
    
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
        B = Matrix(data=self.data, dim=self.dim, init_value=self.init_value)
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