# 第一题 Tower of Hanoi
def hanoi_plus(n, x, y, z):
    if n == 1:
        print(f"{n}:{x}->{y}")
        print(f"{n}:{y}->{z}")
    else:
        hanoi_plus(n - 1, x, y, z)
        print(f"{n}:{x}->{y}")
        hanoi_plus(n - 1, z, y, x)
        print(f"{n}:{y}->{z}")
        hanoi_plus(n - 1, x, y, z)


# 第二题 The Josephus Problem
# 1）
def circle_1(n):
    peo_lst = list(range(1, n + 1))
    return n if n == 1 else pop(peo_lst)


def pop(peo_lst):
    if len(peo_lst) == 1:
        return peo_lst[0]
    new_peo = [peo_lst[i] for i in range(len(peo_lst)) if i % 2 == 0]
    if len(peo_lst) % 2 == 0:
        pass
    else:
        new_peo.insert(0, peo_lst[-1])
        new_peo.pop()
    peo_lst = new_peo
    return pop(peo_lst)


# 2）
def circle_2(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return 2 * circle_2(n // 2) - 1
    return 2 * circle_2(n // 2) + 1


# 3）
def circle_3(n):
    return binary_int(n) * 2 + 1


def binary_int(n):
    return 0 if n == 1 else binary_int(n // 2) * 2 + n % 2


# 第三题 棋盘问题
def grid_cover(k: int, i: int, j: int) -> list[list[int]]:
    if k == 1:
        dic = {
            (1, 1): [[0, 4], [4, 4]],
            (1, 2): [[3, 0], [3, 3]],
            (2, 1): [[2, 2], [0, 2]],
            (2, 2): [[1, 1], [1, 0]],
        }
        return dic[(i, j)]
    else:
        if 1 <= i <= 2 ** (k - 1) and 1 <= j <= 2 ** (k - 1):
            ls1, ls2, ls3, ls4 = (
                grid_cover(k - 1, i, j),
                grid_cover(k - 1, 2 ** (k - 1), 1),
                grid_cover(k - 1, 1, 2 ** (k - 1)),
                grid_cover(k - 1, 1, 1),
            )
            return combine(4, k, ls1, ls2, ls3, ls4)
        elif 1 <= i <= 2 ** (k - 1) and 2 ** (k - 1) + 1 <= j <= 2**k:
            ls1, ls2, ls3, ls4 = (
                grid_cover(k - 1, 2 ** (k - 1), 2 ** (k - 1)),
                grid_cover(k - 1, i, j - 2 ** (k - 1)),
                grid_cover(k - 1, 1, 2 ** (k - 1)),
                grid_cover(k - 1, 1, 1),
            )
            return combine(3, k, ls1, ls2, ls3, ls4)
        elif 2 ** (k - 1) + 1 <= i <= 2**k and 1 <= j <= 2 ** (k - 1):
            ls1, ls2, ls3, ls4 = (
                grid_cover(k - 1, 2 ** (k - 1), 2 ** (k - 1)),
                grid_cover(k - 1, 2 ** (k - 1), 1),
                grid_cover(k - 1, i - 2 ** (k - 1), j),
                grid_cover(k - 1, 1, 1),
            )
            return combine(2, k, ls1, ls2, ls3, ls4)
        elif 2 ** (k - 1) + 1 <= i <= 2**k and 2 ** (k - 1) + 1 <= j <= 2**k:
            ls1, ls2, ls3, ls4 = (
                grid_cover(k - 1, 2 ** (k - 1), 2 ** (k - 1)),
                grid_cover(k - 1, 2 ** (k - 1), 1),
                grid_cover(k - 1, 1, 2 ** (k - 1)),
                grid_cover(k - 1, i - 2 ** (k - 1), j - 2 ** (k - 1)),
            )
            return combine(1, k, ls1, ls2, ls3, ls4)


def combine(n, k, lst1, lst2, lst3, lst4):
    for x in range(2 ** (k - 1)):
        lst1[x] += lst2[x]
        lst3[x] += lst4[x]
    lst = lst1 + lst3
    lst[2 ** (k - 1) - 1][2 ** (k - 1)] = n
    lst[2 ** (k - 1)][2 ** (k - 1) - 1] = n
    lst[2 ** (k - 1)][2 ** (k - 1)] = n
    return lst
