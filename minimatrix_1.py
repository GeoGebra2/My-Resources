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
        if self.dim[0] != self.dim[1]:
            raise Exception("该矩阵非方阵")
        matrix = self.copy()
        times = 0
        for i in range(matrix.dim[1]):
            for j in range(i,matrix.dim[0]):
                if matrix.data[j][i] != 0:
                    if i != j:
                        matrix.data[i],matrix.data[j]=matrix.data[j],matrix.data[i]
                        times+=1
                    break
            if matrix.data[i][i] == 0:
                return 0
            for j in range(i+1,matrix.dim[0]):
                k = matrix.data[j][i] / matrix.data[i][i]
                for z in range(matrix.dim[1]):
                    matrix.data[j][z] -= k *matrix.data[i][z]
        sum = 1
        for i in range(matrix.dim[0]):
            sum*=matrix.data[i][i]
        if times % 2 == 1:
            sum*=-1
        return sum


    def inverse(self):
        if self.dim[0] != self.dim[1]:
            raise Exception("该矩阵非方阵")
        
        matrix = self.copy()
        inverse = Matrix(dim=self.dim)
        for i in range(self.dim[0]):
            inverse.data[i][i] = 1
        for i in range (matrix.dim[0]):
            for j in range(i,matrix.dim[0]):
                if matrix.data[j][i] != 0:
                    if i != j:
                        matrix.data[i],matrix.data[j] = matrix.data[j],matrix.data[i]
                        inverse.data[i],inverse.data[j] = inverse.data[j],inverse.data[i]
                    break
            if matrix.data[i][i] == 0:
                raise Exception("该矩阵无逆矩阵")
            for j in range(matrix.dim[0]):
                if j != i:
                    k = matrix.data[j][i] / matrix.data[i][i]
                    for p in range(matrix.dim[1]):
                        matrix.data[j][p]-= k*matrix.data[i][p]
                        inverse.data[j][p]-= k*inverse.data[i][p]
        for i in range(matrix.dim[0]):
            k = 1/matrix.data[i][i]
            for j in range(matrix.dim[1]):
                inverse.data[i][j]*=k
        
        return inverse

    def rank(self):
        matrix = self.copy()
        free = 0
        rowmain= 0
        colmain = 0
        while rowmain < matrix.dim[0] and colmain < matrix.dim[1]:
            for i in range (rowmain ,matrix.dim[0]):
                if matrix.data[i][colmain] != 0:
                    if rowmain != i:
                        matrix.data[rowmain],matrix.data[i] = matrix.data[i],matrix.data[rowmain]
                    break
            if matrix.data[rowmain][colmain] == 0:
                free += 1
                colmain += 1
                continue
            for i in range(colmain+1,matrix.dim[0]):
                k = matrix.data[i][colmain] / matrix.data[rowmain][colmain]
                for j in range(matrix.dim[1]):
                    matrix.data[i][j]-= k*matrix.data[rowmain][j]
            rowmain += 1
            colmain += 1
        if matrix.dim[1] - free >matrix.dim[0]:
            free = matrix.dim[1] - matrix.dim[0]
        
        return matrix.dim[1] - free

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
            matrix[i].append(random.uniform(0, 1))
    return Matrix(data=matrix)


def nrandom_like(matrix):
    matrix_new = []
    for i in range(matrix.dim[0]):
        matrix_new.append([])
        for j in range(matrix.dim[1]):
            matrix_new[i].append(random.uniform(0, 1))
        return Matrix(data=matrix_new)



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


A = Matrix(data=[[32.447475517142976, 27.261463175942858, 23.254590200514897, 25.721887754063008,  24.54657462943868, 24.370926409925872,  25.78992739631079, 26.234079156305633, 22.961882946985956,  26.34452878027742],
 [27.261463175942858,  35.90372536371353,  23.50785371918095, 27.187726552181164,  26.25980018838251, 26.448557407834603,  30.32878519641164,   28.6776472777403,  24.16193592185215,  27.43749555582083],
 [23.254590200514897,  23.50785371918095, 26.733342745946114,  23.27695451635597, 22.006639185770677, 21.971757500224342,  23.72789848218398,  22.30206334976426, 20.482453030031763,  22.64570717985643],
 [25.721887754063008, 27.187726552181164,  23.27695451635597,  36.53256451067775,  26.76263282945961, 25.264333595618464, 30.279038109927544,  26.37246610570211,   24.1364291713755, 27.984376655947628],
 [24.54657462943868,  26.25980018838251, 22.006639185770677,  26.76263282945961,  33.88928756626949, 24.708215044912865, 27.799151949850966,  26.51581036674519, 23.288475076098464, 25.538470546403975],
 [24.370926409925872, 26.448557407834603, 21.971757500224342, 25.264333595618464, 24.708215044912865,  32.41983174849173,  27.59634084570275, 26.461004220420495, 22.017228244487754, 25.314975199626716],
 [25.78992739631079,  30.32878519641164,  23.72789848218398, 30.279038109927544, 27.799151949850966,  27.59634084570275,  38.48443299767611, 29.066214416217985, 24.168576067719524, 28.713413803020476],
 [26.234079156305633,   28.6776472777403,  22.30206334976426,  26.37246610570211,  26.51581036674519, 26.461004220420495, 29.066214416217985,   35.8985426811476, 22.061794144326456,  28.22680021821742],
 [22.961882946985956,  24.16193592185215, 20.482453030031763,   24.1364291713755, 23.288475076098464, 22.017228244487754, 24.168576067719524, 22.061794144326456, 29.272203032146408, 22.950589678581593],
 [26.34452878027742,  27.43749555582083,  22.64570717985643, 27.984376655947628, 25.538470546403975, 25.314975199626716, 28.713413803020476,  28.22680021821742, 22.950589678581593,  34.83104609504664]])

print(A.inverse())
#print(A.inverse_2())


