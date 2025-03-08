import copy
import random

clause_num = int(input("Please enter the number of the clause: "))  # 输入行数（多少个子句）
colume_num = int(
    input("Please enter the number of the literals in a clause: ")
)  # 输入列数（每个子句多少个变元）

# 输入所有子句并将其储存在一个二维列表中
print(
    "Please enter the clauses and divide the literals with ' ' (space) and divide the clauses with ', '."
)
clause_input = input()
clause_input_copy = clause_input
clause_list = clause_input.split(", ")
for i in range(len(clause_list)):
    tem = [int(x) for x in clause_list[i].split()]
    clause_list[i] = tem

# 确定总变元数
find_max = []
for i in range(clause_num):
    tem_list = [abs(x) for x in clause_list[i]]
    find_max.append(max(tem_list))
literal_num = max(find_max)

# 构造字典储存每个变元的真值，未赋值时初始化为-1
literal_dic = {}
for i in range(1, literal_num + 1):
    literal_dic[i] = -1


# 进行Pure Literal Elimination
def pure_literal_eli(dic, str1, n):
    for i in range(1, n + 1):
        if (str(i) in str1 and str(-i) not in str1) or (
            str(i) not in str1 and str(-i) in str1
        ):
            dic = delete(dic, i)
    return dic


def delete(dic, j):
    for x in dic:
        if j in x:
            x.remove(j)
    return dic


clause_list = pure_literal_eli(clause_list, clause_input_copy, literal_num)


# DPLL主函数
def SAT(dic, lst):
    if is_conflict(dic, lst):  # 冲突检测
        return False
    else:
        lst = unate_pro(dic, lst)  # 进行Unate Propagation
        if lst == []:
            return True  # 检测是否遍历完毕
        elif is_unite_propagation(dic, lst):  # 赋值推导
            unite_dic = unite_pro(dic, lst)
            return SAT(dic | unite_dic, lst)
        else:
            choose_lst = [x for x in dic if dic[x] == -1]  # 随机抽取一个变元进行真值赋值
            new_assign = choose_assign(choose_lst)
            return SAT(dic | {new_assign: True}, lst) or SAT(
                dic | {new_assign: False}, lst
            )


# 冲突检测函数
def is_conflict(dic, lst):
    for i in range(len(lst)):
        if not is_full(lst[i], dic):
            pass
        else:
            tem_dic = {}
            for x in lst[i]:
                if x > 0:
                    tem_dic[x] = dic[abs(x)]
                elif x < 0:
                    tem_dic[x] = not dic[abs(x)]
            if True not in tem_dic.values():
                return True
    return False


def is_full(lst, dic):
    for x in lst:
        if dic[abs(x)] == -1:
            return False
    return True


# Unate Propagation函数
def unate_pro(dic, lst):
    copy_lst = copy.deepcopy(lst)
    for i in range(len(copy_lst)):
        for x in copy_lst[i]:
            if (dic[abs(x)] == True and x > 0) or (dic[abs(x)] == False and x < 0):
                copy_lst[i] = -2
    tem_lst = [j for j in copy_lst if j != -2]
    return tem_lst


# 赋值推导函数
def is_unite_propagation(dic, lst):
    for i in range(len(lst)):
        tem = 0
        for x in lst[i]:
            if dic[abs(x)] == -1:
                tem += 1
        if tem == 1:
            return True
    return False


def unite_pro(dic, lst):
    tep_dic = {}
    for i in range(len(lst)):
        tem_lst = []
        for x in lst[i]:
            if dic[abs(x)] == -1:
                tem_lst.append(x)
        if len(tem_lst) == 1:
            if tem_lst[0] > 0:
                tep_dic[tem_lst[0]] = True
            elif tem_lst[0] < 0:
                tep_dic[abs(tem_lst[0])] = False
    return tep_dic


# 用于随机抽取变元
def choose_assign(lst):
    x = random.choice(lst)
    return x


# test
print(SAT(literal_dic, clause_list))
