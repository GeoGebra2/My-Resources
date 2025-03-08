# Assignment 6
# Problem 1 - 6
from typing import Union

# P1
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return f(f(n // 2)) + 1

# Test
print(f(0))
print(f(1))
print(f(2))


# P2
# 1)
# Loop
def loop_2_1(n):
    if n <= 1:
        return 1
    prev, current = 1, 1
    for i in range(2, n + 1):
        prev, current = current, prev + current 
    return current

# Test
for i in range(10):
    print(f"a_{i} = {loop_2_1(i)}")
print(f"a_{100} = {loop_2_1(100)}")

# Recursion
answer_2_1 = dict()
def recursion_2_1(n):
    res = answer_2_1.get(n, None)
    if res:
        return res 
    if n <= 1:
        res = 1
    else:
        res = recursion_2_1(n - 2) + recursion_2_1(n - 1)
    answer_2_1[n] = res 
    return res

# Test
for i in range(10):
    print(f"a_{i} = {recursion_2_1(i)}")
print(f"a_{100} = {recursion_2_1(100)}")

# 2)
# Loop 
def loop_2_2(n):
    if n <= 2:
        return 1 
    n0, n1, n2 = 1, 1, 1
    for i in range(3, n + 1):
        n0, n1, n2 = n1, n2, n2 + 2 * n1 - n0 
    return n2

# Test
for i in range(10):
    print(f"a_{i} = {loop_2_2(i)}")
print(f"a_{100} = {loop_2_2(100)}")

# Recursion
answer_2_2 = dict()
def recursion_2_2(n):
    res = answer_2_2.get(n, None)
    if res:
        return res 
    if n <= 2:
        res = 1
    else:
        res = recursion_2_2(n - 1) + 2 * recursion_2_2(n - 2) - recursion_2_2(n - 3)
    answer_2_2[n] = res 
    return res

# Test
for i in range(10):
    print(f"a_{i} = {recursion_2_2(i)}")
print(f"a_{100} = {recursion_2_2(100)}")

# 3) 略，同 1) 2)

# 4)
# Loop
n = 100
f = [[0 for __ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    f[i][0], f[0][i] = 1, 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        f[i][j] = f[i][j - 1] + f[i - 1][j] - f[i - 1][j - 1]

# Test
for i in range(3):
    for j in range(3):
        print(f[i][j], end=' ')
    print()
print(f'f[{n}][{n}] = {f[n][n]}')

# Recursion
n = 100
answer_2_4 = dict()
def recursion_2_4(n, m):
    res = answer_2_4.get((n, m), None)
    if res:
        return res 
    if n == 0 or m == 0:
        res = 1
    else:
        res = recursion_2_4(n, m - 1) + recursion_2_4(n - 1, m) - recursion_2_4(n - 1, m - 1)
    answer_2_4[(n, m)] = res 
    return res 

# Test
for i in range(3):
    for j in range(3):
        print(recursion_2_4(i, j), end=' ')
    print()
print(f'f[{n}][{n}] = {recursion_2_4(n, n)}')


# P3
def list_sum(lst: list) -> Union[int, float]:
    summ = 0
    for item in lst:
        if isinstance(item, list):
            summ += list_sum(item)
        else:
            summ += item 
    return summ 

# Test
print(list_sum([]))
print(list_sum([1, 2, 3]))
print(list_sum([[[1]]]))
print(list_sum([1, 2, [3, 4], [5, 6]]))


# P4
def count(lst: list[Union[int, list]]) -> dict[int, int]:
    res = dict()
    for item in lst:
        if isinstance(item, list):
            sub_count = count(item)
            for number, times in sub_count.items():
                res[number] = res.get(number, 0) + times
        else:
            res[item] = res.get(item, 0) + 1
    return res 

# Test
print(count([1, 2, 3, 4, 5, 6, [3, 4, 5, 6], [5, 6]]))
print(count([[[1, 1, 2], 1, 1, 2], 1, 1, 2]))


# P5 
def Hadamard(k: int) -> list[list[int]]:
    if k == 1:
        return [[1]]
    sub = Hadamard(k - 1)
    n = len(sub)
    matrix = [[0 for _ in range(n * 2)] for __ in range(n * 2)]
    for i in range(n):
        for j in range(n):
            matrix[i][j], matrix[i][j + n], matrix[i + n][j], matrix[i + n][j + n] = \
                sub[i][j], sub[i][j], sub[i][j], -sub[i][j]
    return matrix

# Test
def print_matrix(mat):
    for line in mat:
        for item in line:
            print(item, end=' ')
        print()

print_matrix(Hadamard(1))
print()
print_matrix(Hadamard(3))
print()
print_matrix(Hadamard(4))
print()


# P6
def Powerset(S: set) -> list[set]:
    if len(S) == 0: # empty set is the only subset of empty set
        return [set()]
    ele = next(iter(S)) # take one element from S, or ele = min(S) is also ok
    subsets = Powerset(S - {ele})
    return subsets + [subset | {ele} for subset in subsets]

# Test
print(Powerset({}))
print(Powerset({1}))
print(Powerset({1, 2, 3}))
print(Powerset({1, (2, 3)}))
