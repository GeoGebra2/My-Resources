#初始化和输出规范化
def str_to_list(s: str) -> list:
    s = list(s)
    s.reverse()
    if s[-1] == "+":
        s.pop()
    return s


def list_to_str(lst: list) -> str:
    temp = [str(x) for x in lst[::-1]]
    return "".join(temp)


#大整数乘法
#############################################################################################################
#############################################################################################################


def is_neg(lst: list) -> bool:  # 判断正负
    if lst[-1] == "-":
        return True
    return False


def compare(s: list, t: list) -> int:
    if len(s) < len(t):
        return -1

    if len(s) > len(t):
        return 1

    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) > int(t[i]):
            return 1
        if int(s[i]) < int(t[i]):
            return -1
    return 0


def add_positive(s: list, t: list) -> list:
    p = [0] * (max(len(s), len(t)))

    for i in range(len(p)):
        if i < len(s):
            p[i] += int(s[i])
        if i < len(t):
            p[i] += int(t[i])

    for i in range(len(p) - 1):
        p[i + 1] += p[i] // 10
        p[i] %= 10

    return p


def normal_sub(s: list, t: list) -> list:
    if compare(s, t) == 0:
        return "0"

    p = [0] * len(s)

    for i in range(len(p)):
        p[i] += int(s[i])
        if i < len(t):
            p[i] -= int(t[i])

    for i in range(len(p) - 1):
        if p[i] < 0:
            p[i] += 10
            p[i + 1] -= 1

    if p[-1] == 0:
        p.pop()
    return p


def add_pos_and_neg(s: list, t: list) -> list:
    t.pop()
    if compare(s, t) == -1:
        s.append("-")
        p = add_pos_and_neg(t, s)
        p.append("-")
        return p

    return normal_sub(s, t)


def add_negative(s: list, t: list) -> list:
    s.pop()
    t.pop()
    p = add_positive(s, t)
    p.append("-")
    return p


def add(str1: str, str2: str) -> str:
    lst1 = str_to_list(str1)
    lst2 = str_to_list(str2)

    neg_1 = is_neg(lst1)
    neg_2 = is_neg(lst2)

    if neg_1 and neg_2:
        result = add_negative(lst1, lst2)
    elif (not neg_1) and neg_2:
        result = add_pos_and_neg(lst1, lst2)
    elif neg_1 and (not neg_2):
        result = add_pos_and_neg(lst2, lst1)
    else:
        result = add_positive(lst1, lst2)

    return list_to_str(result)


#大整数减法
#############################################################################################################
#############################################################################################################


def change_to_negative(st: str) -> str:  # 变减为加
    s = str_to_list(st)
    if s[-1] != "-":
        return "-" + st
    s.pop()
    return list_to_str(s)


def sub(str1: str, str2: str) -> str:
    neg_str2 = change_to_negative(str2)
    return add(str1, neg_str2)


#大整数乘法
##############################################################################################################
##############################################################################################################


def mul_ten(s: list, t: int, k: int) -> str:
    p = [0] * len(s)

    for i in range(len(p)):
        p[i] += int(s[i]) * t

    for i in range(len(p) - 1):
        p[i + 1] += p[i] // 10
        p[i] %= 10

    return list_to_str(([0] * k) + p)


def mul(str1: str, str2: str) -> str:
    lst1 = str_to_list(str1)
    lst2 = str_to_list(str2)

    neg_1 = is_neg(lst1)
    neg_2 = is_neg(lst2)

    if neg_1:
        lst1.pop()
    if neg_2:
        lst2.pop()

    result = "0"

    for i in range(len(lst2)):
        result = add(mul_ten(lst1, int(lst2[i]), i), result)

    if (neg_1 and (not neg_2)) or ((not neg_1) and neg_2):
        result = "-" + result

    return result


#大整数除法
###################################################################################################################
###################################################################################################################


def div(str1: str, str2: str) -> str:
    lst1 = str_to_list(str1)
    lst2 = str_to_list(str2)

    if str2 == "0":
        return "Error. Division by zero."
    if str1 == "0":
        return "0", "0"
    if compare(lst1, lst2) == -1:
        return "0", str1

    result = 0

    while compare(lst1, lst2) != -1:
        count = 1
        templst2 = lst2
        while compare(lst1, ["0"] + templst2) != -1:
            templst2 = ["0"] + templst2
            count *= 10

        while compare(lst1, templst2) != -1:
            lst1 = normal_sub(lst1, templst2)
            result += count

    return str(result), list_to_str(lst1)


#大整数求幂
##################################################################################################################
##################################################################################################################


def pow(str1: str, n: int) -> str:
    if n == 0:
        return "1"
    t = pow(str1, n // 2)
    if n % 2 == 0:
        return mul(t, t)
    return mul(mul(t, t), str1)


# TEST
###################################################################################################################

#print(div("153", "3"))
print(div("99050", "123"))