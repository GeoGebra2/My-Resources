# 第一题
def f(n):
    if n == 0 or n == 1:
        return 1

    result = [0] * (n + 1)
    result[0] = 1
    result[1] = 1

    for i in range(2, n + 1):
        result[i] = result[result[i // 2]] + 1

    return result[n]


# 第二题
# 1）
def f1(n):
    if n == 0 or n == 1:
        return 1

    result = [0] * (n + 1)
    result[0] = 1
    result[1] = 1

    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]

    return result[n]


# 2）
def f2(n):
    if n == 0 or n == 1 or n == 2:
        return 1

    result = [0] * (n + 1)
    result[0] = 1
    result[1] = 1
    result[2] = 1

    for i in range(3, n + 1):
        result[i] = result[i - 1] + 2 * result[i - 2] - result[i - 3]

    return result[n]


# 3）
def f3(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3

    result = [0] * (n + 1)
    result[0] = 2
    result[1] = 3

    for i in range(2, n + 1):
        result[i] = result[i - 1] * result[i - 2]

    return result[n]


# 4)
def f4(m, n):
    if m == 0 or n == 0:
        return 1
    else:
        lst = [[0] * n] * m
        for i in range(m):
            lst[i][0] = 1
        for i in range(n):
            lst[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                lst[j][i] = lst[j - 1][i] + lst[j][i - 1] - lst[j - 1][i - 1]
    return lst[m - 1][n - 1]


# 第三题
def list_sum(lst):
    sum = 0
    while lst != []:
        lst0 = []
        for x in lst:
            if type(x) == int:
                sum += x
            elif type(x) == list:
                lst0 += x
        lst = lst0
    return sum


# 第四题
def count_list(lst):
    dic = {}
    while lst != []:
        lst0 = []
        for x in lst:
            if type(x) == int:
                if x in dic:
                    dic[x] += 1
                else:
                    dic[x] = 1
            elif type(x) == list:
                lst0 += x
        lst = lst0
    return dic


# 第五题
import copy


def Hadamard(k):
    if k == 0:
        return [1]
    elif k == 1:
        return [[1, 1], [1, -1]]
    else:
        k1 = [[1, 1], [1, -1]]
        i = 2
        while i <= k:
            tep = copy.deepcopy(k1)
            k1 += tep
            for j in range(2 ** (i - 1)):
                k1[j] += k1[j]
            for j in range(2 ** (i - 1), 2**i):
                tem_k = [(-1) * x for x in k1[j]]
                k1[j] += tem_k
            i += 1
    return k1


# 第六题
def Powerset(s):
    n = len(s)
    lst = []
    set_lst = list(s)
    for i in range(2**n):
        tem_lst = list(str(bin(i)))
        tem_lst.remove("0")
        tem_lst.remove("b")
        for i in range(n - len(tem_lst)):
            tem_lst.insert(0, "0")
        sub_lst = []
        for x in range(n):
            if tem_lst[x] == "1":
                sub_lst.append(set_lst[x])
        lst.append(sub_lst)
    return lst
