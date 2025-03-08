#第一题
print('1.')
x1 = input('Please enter the first number: ') #输入第一个数
x2 = input('Please enter the second number: ') #输入第二个数
x3 = input('Please enter the third number: ') #输入第三个数
print(int(x1),int(x2),int(x3)) #转换为int型输出
print(float(x1),float(x2),float(x3)) #转换为float型输出

print('\n')

#第二题
print('2.')
import math
#输入三条边的长度
a = int(input('Please enter the first number: ')) 
b = int(input('Please enter the second number: '))
c = int(input('Please enter the third number: '))
if (a + b > c) & (b + c > a) & (a + c > b): #判定能否形成三角形
    #计算三角形面积
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5 
    print(f"The area of the traingle is {s:.3f}.")
    #计算三个角的弧度
    cosa = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    cosb = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    cosc = (a ** 2 + b ** 2 - c ** 2) / (2 * a * c)
    print(f'Angle A = {math.acos(cosa):.3f}. Angle B = {math.acos(cosb):.3f}. Angle C = {math.acos(cosc):.3f}.')
    #计算外接圆的半径和面积
    R = a / (2 * ((1 - cosa ** 2) ** 0.5))
    S = math.pi * R ** 2
    print(f'The circumradius is {R:.3f},and the area of the circumcircle is {S:.3f}')
    #计算内切圆的半径和面积
    r = (2 * s) / (a + b + c)
    print(f'The radius of the incircle is {r:.3f}, and the area of the incircle is {math.pi * (r ** 2):.3f}')
else :
    print("The traingle doesn't exist.")

print('\n')

#第三题
print('3.')
exp = input("Please enter a mathematical expression: ") #输入一个数学表达式
print(f"{exp} = {eval(exp)}")

print('\n')

#第四题
print('4.')
#输入两个数
x = int(input('Please enter the first number: '))
y = int(input('Please enter the second number: '))
x, y = y, x #交换两个数的值
print(y-x) #求差

#第五题：见前面代码中注释
print('\n')

#第六题
print('6.')
import math
#输入三条边的长度
a = int(input('Please enter the first number: ')) 
b = int(input('Please enter the second number: '))
c = int(input('Please enter the third number: '))

def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5 
    return s

def angle(a, b, c):
    cosa = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    cosb = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    cosc = (a ** 2 + b ** 2 - c ** 2) / (2 * a * c)
    angle_a = math.acos(cosa)
    angle_b = math.acos(cosb)
    angle_c = math.acos(cosc)
    return angle_a, angle_b, angle_c

def circumcircle(a, b, c):
    cosa = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    R = a / (2 * ((1 - cosa ** 2) ** 0.5))
    S = math.pi * R ** 2
    return R, S

def incircle(a, b, c):
    s_traingle = area(a, b, c)
    r = (2 * s_traingle) / (a + b + c)
    s = math.pi * r ** 2
    return r, s

print('Test these functions: ')
s_traingle = area(a, b, c)
A, B, C = angle(a, b, c)
R, S = circumcircle(a, b, c)
r, s = incircle(a, b, c)
print(f'The area of the traingle is {s_traingle:.3f}.\nAngle A = {A:.3f}. Angle B = {B:.3f}. Angle C = {C:.3f}.\nThe circumradius is {R:.3f}, and the area of the circumcircle is {S:.3f}.\nThe radius of the incircle is {r:.3f}, and the area of the incircle is {s:.3f}.')

print('\n')

#第七题
print('7.')
def f(x1, y1, r1, x2, y2, r2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if (distance > r1 + r2) | (distance < abs(r1 - r2)):
        return 0
    elif (distance == r1 + r2) | (distance == abs(r1 - r2)):
        return 1
    else :
        return 2

print('Test f(): ')
num = f(1, 1, 1, 4, 5, 5)
print(f'The number of the crosspoint is {num}.')