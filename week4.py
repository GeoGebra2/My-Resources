#第一题
def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False
    

#第二题
def delta(a, b, c):
    if a == 0:
        num = 1
        x = -c / b
        return num, x
    else:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            num = 2
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            return num, x1, x2
        elif delta == 0:
            num = 1
            x = -b / (2 * a)
            return num, x
        else:
            num = 0
            print("There is no solution.")
            return num


#第三题
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


#第四题
def is_palindrome_year(year):
    year = str(year)
    lens = 0
    sum = 0
    for i in year:
        lens += 1
    year_ = int(year)
    year = int(year)
    for i in range(lens):
        sum += (year_ % 10) * 10 ** (lens - 1 - i)
        year_ = year_ // 10
    if sum == year:
        return True
    else:
        return False


#第五题
import math
def f(x):
    if x < -2:
        return x ** 4
    elif -2 <= x <= 2:
        return math.sin(x)
    else:
        return math.exp(x)


#第六题
x = int(input("Please enter a number: "))
while True:
    if x == 0:
        break
    elif x == -1:
        x = int(input("Please enter a number: "))
        continue
    else:
        x = str(x)
        lens = 0
        sum = 0
        for i in x:
            lens += 1
        x = int(x)
        if x > 0:
            for i in range(lens):
                sum += (x % 10) * 10 ** (lens - 1 - i)
                x //= 10
        else:
            lens -= 1
            x *= -1
            for i in range(lens):
                sum += (x % 10) * 10 ** (lens - 1 - i)
                x //= 10
            sum *= -1
        print(sum)
        x = int(input("Please enter a number: "))


#第七题
def zero_num(n):
    sum = 0
    while n % 10 == 0:
        sum += 1
        n //= 10
    return sum


#第八题
def Hamming(a, b):
    c = a ^ b
    distance = 0
    while c != 0:
        if c % 2 == 1:
            distance += 1
        c //= 2
    return distance


#第九题
def is_valid(n):
    if n == 1:
        return True
    else:
        while n != 1:
            if n %2 == 0:
                n //= 2
            else:
                n = 3*n + 1
            if n == 1:
                return True
    

flag = True
for i in range(1,10**6 + 1):
    if not is_valid(i):
        flag = False
print(flag)



#第十题
for i in range(100001):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(i)


#第十一题
def fractal(n):
    if n == 0:
        return 1
    else:
        multiple = 1
        for i in range(1,n+1):
            multiple *= i
        return multiple

def choose(n, k):
    combination = fractal(n) // ((fractal(k) * fractal(n-k)))
    return combination

def Pascal_triangle(n):
    for i in range(n+1):
        for j in range(n - i):
            print(" ", end = "")
        for j in range(0,i+1):
            print(choose(i, j), end = " ")
        for j in range(1,n - i):
            print(" ",end = "")
        print()

Pascal_triangle(8)