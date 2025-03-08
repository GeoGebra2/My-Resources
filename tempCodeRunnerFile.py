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
        for j in range(1，n - i):
            print(" ",end = "")
        print()

Pascal_triangle(8)