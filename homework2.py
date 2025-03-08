# 1. Brute Force
import time
def find_prime_1(n):
    time_start = time.time()
    number_pn = 0

    for i in range(1, n):
        if is_prime_1(i):
            number_pn += 1

    time_end = time.time()
    return time_end - time_start, number_pn

def is_prime_1(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 2. Optimize Brute Force
import time
def find_prime_2(n):
    time_start = time.time()
    number_pn = 0

    for i in range(1, n):
        if is_prime_2(i):
            number_pn += 1

    time_end = time.time()
    return time_end - time_start, number_pn

def is_prime_2(n):
    if n == 1:
        return False
    x = 2
    while x**2 <= n:
        if n % x == 0:
            return False
        x += 1
    return True


# 3. Optimize Factor
import time
def find_prime_3(n):
    time_start = time.time()
    number_pn = 0

    for i in range(1, n, 6):
        if is_prime_3(i):
            number_pn += 1
    for i in range(-1, n, 6):
        if is_prime_3(i):
            number_pn += 1

    time_end = time.time()
    return time_end - time_start, number_pn

def is_prime_3(n):
    if n <= 1:
        return False
    x = 2
    while x**2 <= n:
        if n % x == 0:
            return False
        x += 1
    return True


# 4. Sieve of Eratosthenes
import time
def find_prime_4(n):
    time_start = time.time()
    number_pn = 0
    num_lst = sieve(n)
    number_pn = [x for x in num_lst if x]
    time_end = time.time()
    return time_end - time_start, len(number_pn)

def sieve(n):
    if n <= 1:
        return []
    truth_lst = [True for x in range(n + 1)]
    truth_lst[0], truth_lst[1] = False, False
    for i in range(2, n + 1):
        if truth_lst[i] == False:
            continue
        for j in range(2 * i, n + 1, i):
            truth_lst[j] = False
    return truth_lst


# 5. Miller-Rabin
import time
def find_prime_5(n):
    time_start = time.time()
    number_pn = 0

    for i in range(1, n):
        if is_prime_5(i):
            number_pn += 1

    time_end = time.time()
    return time_end - time_start, number_pn

def is_prime_5(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    s = n - 1
    t = 0
    while s % 2 == 0:
        t += 1
        s //= 2

    for a in [2, 3]:
        x_1 = pow(a, s, n)
        for i in range(t):
            x_2 = pow(x_1, 2, n)
            if x_1 != 1 and x_1 != n - 1 and x_2 == 1:
                return False
            x_1 = x_2
        if x_2 != 1:
            return False

    return True
