#第一题
def sum_and_product(a):
    pro = 1
    for i in a:
        pro *= i
    return sum(a), pro



#第二题
def compare_list(lst1, lst2):
    ls1 = True
    ls2 = True
    for i in lst1:
        if i not in lst2:
            ls1 = False
            break
    for i in lst2:
        if i not in lst1:
            ls2 = False
            break
    if ls2 :
        return True, lst1
    elif (not lst2) and ls1 :
        return True, lst2
    else:
        return False



#第三题
def find_number(n = 1000, m = 3000):
    for i in range(n, m+1):
        even = True
        i = str(i)
        lst = list(i)
        for j in lst:
            j = int(j)
            if j % 2 != 0:
                even = False
        if even :
            i = int(i)
            print(i, end = ", ")
    print()



#第四题
def clear_list(lst):
    new_lst = [lst[0]]
    for i in range(1,len(lst)):
        if lst[i] not in lst[:i]:
            new_lst.append(lst[i])
    print(new_lst)



#第五题
def positive_number(n):
    n = str(n)
    lst1 = list(n)
    lst1.reverse()
    new_lst1 = [int(lst1[i]) * 10 ** (len(lst1)-1-i) for i in range(len(lst1))]
    return sum(new_lst1)

def negtive_number(n):
    n = abs(n)
    n_ = positive_number(n)
    return -1 * n_



#第六题
def split(lst1, lst2):
    conj_lst = []
    for i in lst1:
        if i in lst2:
            conj_lst.append(i)
    if conj_lst == []:
        print("no intersection.")
        return False
    else:
        return conj_lst



#第七题
def print_star(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end = " ")
        print()
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print("*", end = " ")
        print()



#第八题
def count_digits(n):
    n = str(n)
    lst_n = list(n)
    count_list = [0,0,0,0,0,0,0,0,0,0]
    count_list[int(lst_n[0])-1] = lst_n.count(lst_n[0])
    for i in range(1,len(lst_n)):
        if lst_n[i] not in lst_n[:i]:
            count_list[int(lst_n[i])-1] = lst_n.count(lst_n[i])
    final_list = [str(i+1) + ":" + str(count_list[i]) for i in range(10)]
    return final_list



#第九题
def sum_of_two(n):
    final_sum = 0
    single_sum = 0
    for i in range(0,n):
        single_sum += 2 * 10 ** i
        final_sum += single_sum
    return final_sum



#第十题
def creat_matrix():
    a = [i for i in range(1,11)]
    A = [a] * 10
    B = []
    for i in range(1,11):
        B.append([i for j in range(10)])
    for i in A:
        print(i)
    for i in B:
        print(i)



#第十一题
def find_min(lst):
    for i in range(1,len(lst)):
        if lst[i] < lst[i-1]:
            break
    if i == len(lst) - 1:
        for j in range(len(lst)-1,-1,-1):
            if lst[j] != lst[j-1]:
                break
    elif i > 1:
        for j in range(i-2,-1,-1):
            if lst[j] != lst[j-1]:
                break
    else:
        j = 0
    return j



#第十二题
def is_prime(n):
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def find_prime(n):
    lst = [i for i in range(1,n+1)]
    lst_prime = [i for i in range(2,n // 2 + 1) if is_prime(i)]
    for i in range(len(lst_prime)):
        j = lst_prime[i] * 2
        while j <= n:
            lst[j-1] = -1
            j += lst_prime[i]
    lst[0] = -1
    prime_list = [lst[i] for i in range(n) if lst[i] != -1]
    return prime_list

