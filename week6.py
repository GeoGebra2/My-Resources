#第一题
def del_and_sort(lst):
    lset = set(lst)
    lst = list(lset)
    lst.sort(reverse = True)
    return lst




#第二题
str = """Hello world
Practice makes perfect."""
def trans(str):
    return str.upper()




#第三题
def merge(a,b):
    c = a + b
    c.sort()
    return c




#第四题
def count_number(a):
    a = set(a)
    even_number = 0
    odd_number = 0
    for x in a:
        if x % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    return even_number, odd_number




#第五题
def is_valid():
    low_alpha = {"a","b","c","d","e","f","g","h","i",\
                 "j","k","l","m","n","o","p","q","r",\
                 "s","t","u","v","w","x","y","z"}
    upp_alpha = {"A","B","C","D","E","F","G","H","I",\
                 "J","K","L","M","N","O","P","Q","R",\
                 "S","T","U","V","W","X","Y","Z"}
    num = {"0","1","2","3","4","5","6","7","8","9"}
    character = {"$","#","@"}
    code = input("Please enter a password: ")
    if len(code) < 6 or len(code) > 16:
        return False
    code = set(code)
    if (code & low_alpha == set()) or \
    (code & upp_alpha == set()) or \
    (code & num == set()) or \
    (code & character == set()):
        return False
    else:
        return True




#第六题
def check_alpha(a):
    a_ = a.lower()
    if a_ in "aeiou":
        return True
    else:
        return False




#第七题
def month_day(a):
    dic = {"January" :31, "Feburary" :28, \
           "March" :31, "April" :30, "May" :31, \
           "June" :30, "July" :31, "August" :31, \
           "September" :30, "October" :31, \
           "November" :30, "December" :31}
    return dic[a]




#第八题
def is_integer(str):
    return str.isdigit()




#第九题
def season(mon,day):
    mon1 = [1,3,5,7,8,10,12]
    mon2 = [4,6,9,11]
    if mon < 0 or \
    mon > 12 or \
    day < 0 or \
    (mon in mon1 and day > 31) or \
    (mon in mon2 and day > 30) or \
    (mon == 2 and day > 28):
        return "Error"
    elif (mon == 2 and day >= 4) or \
    (mon == 3) or \
    (mon == 4) or \
    (mon == 5 and day <= 5):
        return "Spring"
    elif (mon == 5 and day >= 6) or \
    (mon == 6) or \
    (mon == 7) or \
    (mon == 8 and day < 8):
        return "Summer"
    elif (mon == 8 and day >= 8) or \
    (mon == 9) or \
    (mon == 10) or \
    (mon == 11 and day < 6):
        return "Autumn"
    else :
        return "Winter"




#第十题
def zodiac(year):
    year %= 12
    dic = {0: "Monkey", 1: "Chicken", \
           2: "Dog", 3: "Pig", 4: "Mouse", \
           5: "Ox", 6: "Tiger", 7: "Rabbit", \
           8: "Dragon", 9: "Snake", 10: "Horse", \
           11: "Sheep"}
    return dic[year]
            



#第十一题
def is_leapyear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False

    
def next_day():
    mon1 = [1,3,5,7,8,10]
    mon2 = [4,6,9,11]
    year = int(input("Please enter a year: "))
    mon = int(input("Please enter a month[1-12]: "))
    day = int(input("Please enter a day[1-31]: "))
    if (mon in mon1 and day == 31) or \
    (mon in mon2 and day == 30) or \
    (is_leapyear(year) and mon == 2 and day == 29) or \
    (not is_leapyear(year) and mon == 2 and day == 28):
        mon += 1
        day = 1
    elif mon == 12 and day == 31:
        year += 1
        mon = 1
        day = 1
    else:
        day += 1
    print(f"The next date is [yyyy-mm-dd] {year}-{mon}-{day}")




#第十二题
article = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.

Abraham Lincoln
November 19, 1863"""

lst = list(article)
for i in range(len(lst)):
    if lst[i] == "," or lst[i] == ".":
        lst[i] = "-1"
    elif lst[i] == "-" and lst[i+1] == "-":
        lst[i] = "-1"
        lst[i+1] = "-1"
    elif lst[i] == "\n":
        lst[i] == " "
lst1 = list(x for x in lst if x != "-1")
article = "".join(lst1)
article = article.lower()
word_num = len(article.split()) - 1
letter_num = len(list(x for x in article if "a" <= x <= "z"))

print(article)
print(word_num,letter_num)