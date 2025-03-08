from typing import List
import math
from functools import reduce


# 1-20 cheng fan

# 001 Happy Number

def sumbits(n):
	ans =  0
	while n>0:
		ans += (n%10) ** 2
		n //= 10

	return ans

def is_happy(n):
	st = set()

	while n!=1:
		if n in st:
			break
		else:
			st.add(n)

		n = sumbits(n)


	return n==1

#print(is_happy(19))

# 204-Count Primes
def is_prime(p):
	i = 2
	while i*i<=p:
		if p%i==0:
			return False
		i += 1

	return True

def number_primes(n):
	ans = 0
	for x in range(2,n):
		if is_prime(x):
			ans += 1

	return ans

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))

print(number_primes(10))

#3. 205-isomorphic strings

# def create_dict(ps):
# 	dt = {}
# 	for x in ps:
# 		if x in dt:
# 			dt[x] += 1
# 		else:
# 			dt[x] = 1

# 	lst = []
# 	for x in dt:
# 		lst.append(dt[x])
	
# 	return lst

# print(create_dict("add"))
# print(create_dict("egg"))
# print(create_dict("foo"))
# print(create_dict("bar"))


# def is_iso(ps1, ps2):
# 	return create_dict(ps1) == create_dict(ps2)

def is_iso(ps1, ps2):
	if len(ps1) == 0:
		return True

	for i in range(len(ps1)):
		if ps1.find(ps1[i]) != ps2.find(ps2[i]):
			return False

	return True


def is_iso(ps1, ps2): # order preserving
	if len(ps1) == 0:
		return True
	dt1 = {}
	dt2 = {}

	for i in range(len(ps1)):
		if ps1[i] not in dt1:
			dt1[ps1[i]] = i
		if ps2[i] not in dt2:
			dt2[ps2[i]] = i
		if dt1[ps1[i]] != dt2[ps2[i]]:
			return False

	return True
print("205-isomorphic")
print(is_iso("egg", "add"))
print(is_iso("foo", "bar"))
print(is_iso("paper", "title"))
print(is_iso("aba", "baa"))
print(is_iso("abba", "abab"))
print(is_iso("via", "sow"))



# 4. 217
def is_dup(lst):
	st = set(lst)
	return len(st) != len(lst)

print(is_dup([1,2,3,1]))
print(is_dup([1,2,3,4]))
print(is_dup([1,1,1,3,3,4,3,2,4,2]))

# 5.219

def is_dup1(lst, k):
	
	st = set()

	for i in range(len(lst)):
		if i>=k+1:
			st.remove(lst[i-k-1])

		if lst[i] in st:
			return True

		st.add(lst[i])

	return False

print(is_dup1([1,2,3,1],3))
print(is_dup1([1,0,1,1],1))
print(is_dup1([1,2,3,1,2,3],2))

# 6.231 power of two

def is_power2(n):
	while n%2==0:
		n //= 2
	return n == 1

print(is_power2(1))
print(is_power2(16))
print(is_power2(218))

# 7.242



def count_anagram(ps):
	#You may assume the string contains only lowercase alphabets
	cnt = [0]*26
	for x in ps:
		cnt[ord(x)-ord('a')] += 1

	return cnt

def is_anagram(ps1, ps2):
	return count_anagram(ps1) == count_anagram(ps2)

s = "anagram"
t = "nagaram" 
print(is_anagram(s, t))
s = "rat"
t = "car" 
print(is_anagram(s, t))

#8. 258 add bits

def add_bits(n):
	if n == 0:
		return 0

	ans = 0
	while n>0:
		ans = (ans+n%10)%9
		n //= 10

	if ans == 0:
		ans = 9

	return ans

print(add_bits(38))
print(add_bits(72))
print(add_bits(0))
print(add_bits(126))

# 9 263-Ugly Number 

def is_ugly(n): # 2,3,5
	for p in (2,3,5):
		while n % p ==0:
			n //= p

	return n == 1

print(is_ugly(6))
print(is_ugly(8))
print(is_ugly(14))

# 10. 268-Missing Number 

def find_miss(lst):
	n = len(lst) - 1
	a = n*(n+1)//2
	
	for x in lst:
		if 1 <= x and x <= n:
			a -= x
	return a

print(find_miss([3,0,1] ))
print(find_miss([9,6,4,2,3,5,7,0,1] ))


# 11. 283 move zeros

def move0(lst):
	t = 0

	for i in range(len(lst)):
		if lst[i] != 0 and t != i:
			lst[t] = lst[i]
			t += 1
			lst[i] = 0

	return lst


print(move0([0,1,0,3,12]))
print(move0([0,1,1,1,0,3,0,0,0,12]))

# 12. 290 word pattern

def word_pattern(pattern, pstr):
	pss = pstr.split()

	if len(pattern) != len(pss):
		return False

	dt = {}

	for i in range(len(pattern)):
		if pattern[i] in dt: 
			if dt[pattern[i]] != pss[i]:
				return False
		else:
			if pss[i] in dt.values(): # 1-1
				return False

			dt[pattern[i]] = pss[i]

	return True

pattern = "abba" 
pstr = "dog cat cat dog" 
print(word_pattern(pattern, pstr))
pattern = "abba"
pstr = "dog cat cat fish" 
print(word_pattern(pattern, pstr))
pattern = "aaaa"
pstr = "dog cat cat dog" 
print(word_pattern(pattern, pstr))
pattern = "abba"
pstr = "dog dog dog dog" 
print(word_pattern(pattern, pstr))

# 13. 292 Nim Game

def nim(n):
	return n%4 != 0

print(nim(4))
print(nim(3))

# 14. power of three
# Could you do it without using any loop / recursion
def is_power3(n):

# soluiton 1:
#	while n % 3 == 0 and n != 0:
#		n /= 3
	
#	return n == 1

# solution without loop
	magic = 1162261467 # 1162261467= 3 ** 19
	return n>0 and magic%n == 0

print(is_power3(27))
print(is_power3(0))
print(is_power3(9))
print(is_power3(45))

# 15. 342 power of four
# Given an integer (signed 32 bits) 2**32

def is_power4(n):
	magic = 2**32
	# 2**(2x) mod 3 = 1
	return n>0 and magic%n == 0 and n%3 == 1 

print(is_power4(8))
print(is_power4(16))
print(is_power4(5))

# 16. 344-Reverse String

def reverse_str(ps):
	return ps[::-1]

print(reverse_str("hello"))
print(reverse_str("A man, a plan, a canal: Panama"))

# 17. 345-Reverse Vowels of a String 

def reverseV(ps):
	aeiou = "aeiou"

	lst = list(ps)

	i = 0
	j = len(ps) - 1
	
	while True:
		while (lst[i] not in aeiou)  and i<j:
			i += 1
		if i == j:
			break
		while (lst[j] not in aeiou) and j>i:
			j -= 1
		if i == j:
			break
		lst[i], lst[j] = lst[j], lst[i]
		i += 1
		j -= 1

	return "".join(lst)

print(reverseV("hello"))
print(reverseV("leetcode"))

# 18. intersection of two arrays

def array_intersection(lst1, lst2):
	st1, st2 = set(lst1), set(lst2)
	return list(st1 & st2)

print(array_intersection([1,2,2,1], [2,2] ))
print(array_intersection([4,9,5], [9,4,9,8,4]  ))

# 19. intersection of two arrays II

def construct_dict(lst1):
	dt = {}
	for x in lst1:
		if x in dt:
			dt[x] += 1
		else:
			dt[x] = 1

	return dt

def array_intersection(lst1, lst2):

	dt1 = construct_dict(lst1) 
	dt2 = construct_dict(lst2)

	ans = []
	for x in dt1:
		if x in dt2:
			ans += [x] * min(dt1[x], dt2[x])

	return ans

print(array_intersection([1,2,2,1],[2,2]))
print(array_intersection([4,9,5], [9,4,9,8,4]))

# 20. 
def is_perfect_square(x):
	# binary search
	l, r = 1, x

	while True:
		m = (l+r)//2
		if m*m <x and x < (m+1)**2:
			return False

		if m*m == x:
			return True
		elif m*m > x:
			r = m -1
		else:
			l = m + 1
	
	return ans

print(is_perfect_square(16))
print(is_perfect_square(14))
print(is_perfect_square(195))
print(is_perfect_square(196))
print(is_perfect_square(10000))
print(is_perfect_square(100000))
print(is_perfect_square(1000000))
print(is_perfect_square(10000000))


#21-20 LMC

#21.


def canConstruct(ransomNote, magazine):
	for i in ransomNote:
		if magazine.count(i)<ransomNote.count(i):
			return False
	return True
print(canConstruct("a","b"))
print(canConstruct("aaa","aaba"))
print(canConstruct("ransomear","mbdaaraegcrovscna"))

#22.
def firstUniqChar(s):
	dic={}
	for i in s:
		dic[i]=0
	for i in s:
		dic[i]+=1
	for t in dic.keys():
		if dic[t]==1:
			return s.find(t)
	return -1
print(firstUniqChar("abacb"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("leetcodeiscool"))


#23.

def findTheDifference(s, t):
    for i in t:
        if s.count(i)!=t.count(i):
            return i
    return ""
print(findTheDifference("abcd","abced"))
print(findTheDifference("ae","aea"))


#24.
#Medium
def findNthDigit(n):
        s=""
        for i in range(1,n+1):
            s+=str(i)
        return s[n-1]

# def findNthDigit(n:) -> int:
#         num=9
#         cnt=1
#         #0-9,10-99,100-999...
#         while n>num*cnt:
#             n-=num*cnt
#             cnt+=1
#             num*=10
#         realnum=num//9 + (n-1)//cnt
#         index=(n-1)%cnt
#         return str(realnum)[index]
print(findNthDigit(3))
print(findNthDigit(100))
print(findNthDigit(10010))


#25.
def longestPalindrome(s):
        dic={}
        num=[]
        ans=0
        for i in s:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        for t in dic.values():
            num.append(t)
        num.sort(reverse=True)
        for n in num:
            ans+=n//2*2
            if ans%2==0 and n%2==1:
                ans+=1
        return ans
print(longestPalindrome("abccccdd"))
print(longestPalindrome("abcccdd"))
print(longestPalindrome("adeadeade"))



#26.
def thirdMax(nums):
	#delete repeat numbers
    num = set(nums)
    if len(num) <= 2:
        return max(num)
    else:
        for i in range(3):
            ans = max(num)
            num.remove(ans)
        return ans
print(thirdMax([1,3]))
print(thirdMax([1,2,3,2]))
print(thirdMax([7,7,8,9,7,9,6,5,3,2]))



#27.
def countSegments(s):
    ans=0
    for i in range(len(s)):
        if s[i]==" " and i>=1 and s[i-1]!=" ":
            ans+=1
        if i==len(s)-1 and s[i]!=" ":
            ans+=1
    return ans
print(countSegments("I love leetcode!"))
print(countSegments(""))
print(countSegments("   "))



#28.
def findAnagrams(s, p):
    ans=[]
    for i in range(len(s)-len(p)+1):
        is_ana=True
        for t in range(len(p)):
            if s[i:i+len(p)].count(s[i+t])!=p.count(s[i+t]):
                is_ana=False
        if is_ana:
            ans.append(i)
    return ans
print(findAnagrams("cbaebabacd","abc"))
print(findAnagrams("abab","ab"))
print(findAnagrams("cabacba","abc"))


#29.
def arrangeCoins(n):
    ans=0
    for i in range(n):
        ans+=i
        if n-ans<i+1:
            return i
        elif n-ans==i+1:
            return i+1
    return 0
print(arrangeCoins(5))
print(arrangeCoins(8))
print(arrangeCoins(100))


#30.
#Medium
def compress(chars):
    cur=chars[0]
    cnt=0
    ans=[]
    for c in chars+[' ']:
        if c==cur:
            cnt+=1
        else:
            ans+=[cur]
            if cnt!=1:
                ans+=list(str(cnt))
            cnt=1
            cur=c
    chars[:]=ans
    return len(chars)
print(compress(["a","a","b","b","c","c","c"]))
print(compress(["l"]))
print(compress(["a","a","c","c","c","b","d","d","e","e","k","k"]))


# BXY

# 31.find all numbers disappeared in an array


def find_disappear(arr):
    n = len(arr)
    counter = [0] * (n + 1)
    for item in arr:
        counter[item] += 1
    res = []
    for i in range(1, n+1):
        if counter[i] == 0:
            res.append(i)
    return res


assert find_disappear([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
assert find_disappear([1, 2, 3, 3]) == [4]

# 32. Minimum Moves to Equal Array Elements

def minimum_moves(arr):
    moves = 0
    arr.sort()
    n = len(arr)
    while sum(arr) != arr[-1] * n:
        for i in range(n-1):
            arr[i] += 1
        arr.sort()
        moves += 1
    return moves

assert minimum_moves([1, 2, 3]) == 3
assert minimum_moves([3, 3]) == 0
assert minimum_moves([2, 3, 3]) == 2


# 33. assign cookies

def assign_cookies(greedy_factor, cookies):
    greedy_factor.sort()
    cookies.sort()

    child_index = 0
    coookies_index = 0

    while cookies_index < len(cookies) and child_index < len(greedy_factor): # cookie left
        if cookies[coookies_index] >= greedy_factor[child_index]:
            child_index += 1
        coookies_index += 1
    return child_index

# 34. Repeated Substring Patter

def has_repeated_pattern(s):
    n = len(s)
    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len == 0:
            repeat_time = n // pattern_len
            if s[:pattern_len] * repeat_time == s:
                return True
    return False

assert has_repeated_pattern("abab") == True
assert has_repeated_pattern("aba") == False
assert has_repeated_pattern("abcabcabcabc") == True

# 35. Hamming distance

def hamming_distance(num1, num2):
    bit_num1 = bin(num1)[2:]
    bit_num2 = bin(num2)[2:]
    len_bit1 = len(bit_num1)
    len_bit2 = len(bit_num2)
    # larger_bit = max(len_bit1, len_bit2)
    bit_num1 = max(0, len_bit2 - len_bit1) * "0" + bit_num1
    bit_num2 = max(0, len_bit1 - len_bit2) * "0" + bit_num2
    counter = 0
    for i in range(len(bit_num1)):
        if bit_num1[i] != bit_num2[i]:
            counter += 1
    return counter

assert hamming_distance(1, 4) == 2
assert hamming_distance(5, 9) == 2

# 36. heaters


def find_radius(houses, heaters):
    houses.sort()
    heaters.sort()
    pos = 0
    ans = 0
    heaters = [float("-inf")] + heaters + [float("inf")]
    for house in houses:
        while house > heaters[pos]:
            pos += 1
        temp_radius = min(house - heaters[pos-1], heaters[pos] - house)
        ans = max(ans, temp_radius)
    return ans

assert find_radius([1, 2, 3], [2]) == 1
assert find_radius([1, 2, 3, 4], [1, 4]) == 1
assert find_radius([1, 5], [2]) == 3


# 37 Number Complement

def number_complement(num):
    next_num = 2
    while next_num < num:
        next_num *= 2
    return next_num - num - 1


assert number_complement(5) == 2
assert number_complement(1) == 0

# 38 Largest Palindrome Product

def largest_palindrome_product(n):
    if n == 1:
        return 9
    high = 10 ** n - 1
    low = 10 ** (n - 1)
    left_max = high
    tmp = left_max
    while tmp >= low:
        result = int(str(tmp) + str(tmp)[::-1])
        for i in range(high, int(result ** (0.5)), -1):
            if result % i == 0:
                return result % 1337
        tmp = tmp - 1

assert largest_palindrome_product(2) == 987


# 39 License Key Formatting

def license_key_format(ori_key, k):
    key_without_dash = "".join(ori_key.split("-"))
    if k == 1:
        return key_without_dash
    if len(key_without_dash) % k == 0:
        group_num = len(key_without_dash) // k
        remain = 0
    else:
        remain = len(key_without_dash) % k
        group_num = (len(key_without_dash) - remain) // k
    res = key_without_dash[: remain] + "-"
    index = remain
    for i in range(group_num):
        res += key_without_dash[index: index + k] + "-"
        index += k
    res = res.strip("-")
    res = res.upper()
    return res


assert license_key_format("5F3Z-2e-9-w", 4) == "5F3Z-2E9W"
assert license_key_format("2-5g-3-J", 2) == "2-5G-3J"


# 40 max consecutive one

def max_consecutive_one(arr):
    max_len = 0
    temp_len = 0
    for i, ch in enumerate(arr):
        if ch == 1:
            temp_len += 1
        else:
            max_len = max(temp_len, max_len)
            temp_len = 0
    max_len = max(temp_len, max_len)
    return max_len

assert max_consecutive_one([1,1,0,1,1,1]) == 3




#41-50 ZYF

# 41. 496
def check(number, nums1, nums2):
    index = nums2.index(number)
    for i in range(index, len(nums2)):
        if (nums2[i] > number):
            return nums2[i]
    return -1


def nextGreaterElement(nums1, nums2):
    return [check(x, nums1, nums2) for x in nums1]


print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(nextGreaterElement([2, 4], [1, 2, 3, 4]))


# 42. 507
def checkPerfectNumber(num):
    import math
    divisors_sum = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if not num % i:
            if num // i == i:
                divisors_sum += i
            else:
                divisors_sum += i + num // i
    return num == divisors_sum - num


print(checkPerfectNumber(28))
print(checkPerfectNumber(6))
print(checkPerfectNumber(496))
print(checkPerfectNumber(8128))
print(checkPerfectNumber(2))


# 43. 628
def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


print(maximumProduct([1, 2, 3]))
print(maximumProduct([-1, -2, -3]))
print(maximumProduct([1, 2, 3, 4]))


# 44. 633(medium)
def judgeSquareSum(c):
    import math
    for i in range(int(math.sqrt(c // 2)) + 1):
        if math.sqrt(c - i * i) == int(math.sqrt(c - i * i)):
            return True
    return False


print(judgeSquareSum(5))
print(judgeSquareSum(3))
print(judgeSquareSum(4))
print(judgeSquareSum(2))


# 45. 672(medium)
def flipLights(n, m):
    if n == 0 or m == 0:
        return 1
    if n == 1:
        return 2
    if n == 2 and m == 1:
        return 3
    if n == 2 and m > 1:
        return 4
    if n >= 3:
        if m == 1:
            return 4
        if m == 2:
            return 7
        return 8


print(flipLights(1, 1))
print(flipLights(2, 1))
print(flipLights(3, 1))


# 46. 728
def selfDividingNumbers(left, right):
    i = left
    l = []
    while i <= right:
        judge = True
        l_s = list(str(i))
        if '0' in l_s:
            i += 1
        else:
            for j in l_s:
                if i % int(j) != 0:
                    judge = False
                    break
            if judge:
                l += [i]
                i += 1
            else:
                i += 1
    return l


print(selfDividingNumbers(1, 22))


# 47. 754(medium)
def reachNumber(target):
    target = abs(target)
    total = 0
    totalDistence = 0
    while totalDistence < target or (totalDistence - target) % 2 != 0:
        totalDistence += total + 1
        total += 1
    return total


print(reachNumber(3))
print(reachNumber(2))

# 48. 877(medium)
"""
Alex is first to pick pile.
piles.length is even, and this lead to an interesting fact:
Alex can always pick odd piles or always pick even piles!

For example,
If Alex wants to pick even indexed piles piles[0], piles[2], ....., piles[n-2],
he picks first piles[0], then Lee can pick either piles[1] or piles[n - 1].
Every turn, Alex can always pick even indexed piles and Lee can only pick odd indexed piles.

In the description, we know that sum(piles) is odd.
If sum(piles[even]) > sum(piles[odd]), Alex just picks all evens and wins.
If sum(piles[even]) < sum(piles[odd]), Alex just picks all odds and wins.

So, Alex always defeats Lee in this game.
"""


def stoneGame(piles):
    return True


print(stoneGame([5, 3, 4, 5]))

# 49. 914
import collections


def hasGroupsSizeX(deck):
    count = collections.Counter()
    for card in deck:
        count[card] += 1
    num = min([count[card] for card in count])
    x = 0
    for i in range(1, num + 1):
        t = 1
        for card in count:
            if count[card] % i != 0:
                t = 0
                break
        if t: x = i
    return x > 1


print(hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
print(hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
print(hasGroupsSizeX([1]))


# 50. 942
def diStringMatch(S):
    lo, hi = 0, len(S)
    ans = []
    for x in S:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1

    return ans + [lo]


print(diStringMatch("IDID"))
print(diStringMatch("III"))
print(diStringMatch("DDI"))

# LYM

# 51. 7-Reverse Integer
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s = str(x)
    ans = 0
    if s[0] == '-':
        ans = -int(s[:0:-1])
    else:
        ans = int(s[::-1])
    if ans > (2**31) - 1 or ans < -(2**31):
        return 0
    return ans

test_input = [123, 12345, -321, -120, 10086]
test_output = [321, 54321, -123, -21, 68001]
for i in range(len(test_input)):
    print(reverse(test_input[i]) == test_output[i])

# 52. 9-Palindrome Number
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    return x == x[::-1]

test_input = [10, 12321, 2333, 2332]
test_output = [False, True, False, True]
for i in range(len(test_input)):
    print(isPalindrome(test_input[i]) == test_output[i])

# 53. 11-Container With Most Water
#这道题有一点算法的意思
# O(n^2) 这种做法结果正确，但复杂度太高，leetcode上过不了会超时。现阶段能写这种就行。
def maxArea_1(height):
    ans = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            ans = max(ans, (j - i) * min(height[i], height[j]))
    return ans

# O(n) 在leetcode上能过的解法，原理：当前考虑区间为[a, b], 若 h[a] < h[b], 则所有形如 [a, *] 的区间都不必再考虑；若 h[a] > h[b]，则所有形如 [*, b] 的区间都不必再考虑，
# 故每次移动较小一边即可
def maxArea(height):
    head = 0
    tail = len(height) - 1
    ans = 0
    while head < tail:
        if height[head] < height[tail]:
            ans = max(ans, (tail - head) * height[head])
            head += 1
        else:
            ans = max(ans, (tail - head) * height[tail])
            tail -= 1
    return ans

test_input = [[1,8,6,2,5,4,8,3,7], [1,1], [4,3,2,1,4], [1,2,1]]
test_output = [49, 1, 16, 2]
for i in range(len(test_input)):
    print(maxArea(test_input[i]) == test_output[i])

# 54. 12-Integer to Roman
def intToRoman(num):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    mark = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    for i in range(len(value)):
        while num >= value[i]:
            num -= value[i]
            roman += mark[i]
    return roman

test_input = [3, 4, 9, 58, 1994]
test_output = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
for i in range(len(test_input)):
    print(intToRoman(test_input[i]) == test_output[i])
            
# 55. 14-Longest Common Prefix
def longestCommonPrefix(strs):
    if len(strs) < 1:
        return ""
    length = len(strs[0])
    for s in strs[1:]:
        i = 0
        while i < length and i < len(s) and s[i] == strs[0][i]:
            i += 1
        length = i 
    return strs[0][:length]

test_input = [["flower","flow","flight"], ["dog","racecar","car"]]
test_output = ["fl", ""]
for i in range(len(test_input)):
    print(longestCommonPrefix(test_input[i]) == test_output[i])

# 56. 26-Remove Duplicates from Sorted Array
def removeDuplicates(nums):
    i = 0
    for j in range(len(nums)):
        if j == 0 or nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
    return i 

#这道题的返回值比较特别，要求在原数组上原地修改（只开销O(1)的额外空间），并返回新数组的长度
Array = [0,0,1,1,1,2,2,3,3,4]
new_length = removeDuplicates(Array)
print(Array[:new_length])

# 57. 27-Remove Element
def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

#这道题的返回值比较特别，要求在原数组上原地修改（只开销O(1)的额外空间），并返回新数组的长度
nums = [0,1,2,2,3,0,4,2]
val = 2
length = removeElement(nums, val)
print(nums[:length])

# 58. 28-Implement strStr()
#这里只给出最好理解的解法。该问题存在线性时间复杂度解法，有兴趣的同学可自行了解kmp字符串匹配算法
def strStr(haystack, needle):
    if len(needle) < 1:
        return 0
    for i in range(len(haystack)-len(needle)+1):
        flag = True
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                flag = False
                break
        if flag:
            return i 
    return -1    

test_input = [("hello", "ll"), ("aaaaa", "bba"), ("", ""), ("aaa", "aaaa"), ("aaaa", "aaa")]
test_output = [2, -1, 0, -1, 0]
for i in range(len(test_input)):
    print(strStr(test_input[i][0], test_input[i][1]) == test_output[i])        

# 59. 34-Find First and Last Position of Element in Sorted Array
#这道题涉及二分查找
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    N = len(nums)
    L = 0
    R = N - 1
    while L <= R:
        M = (L + R) // 2
        if nums[M] >= target:
            R = M - 1
        else:
            L = M + 1
    A = L
    L = 0
    R = N - 1
    while L <= R:
        M = (L + R) // 2
        if nums[M] <= target:
            L = M + 1
        else:
            R = M - 1
    B = R
    if A >= 0 and A < N and nums[A] == target:
        return [A,B]
    return [-1,-1]

test_input = [([5,7,7,8,8,10], 8), ([5,7,7,8,8,10], 6)]
test_output = [[3,4], [-1,-1]]
for i in range(len(test_input)):
    print(searchRange(test_input[i][0], test_input[i][1]) == test_output[i])

# 60. 35-Search Insert Position
#这道题涉及二分查找
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    R = len(nums) - 1
    L = 0
    while L <= R:
        M = (L + R) // 2
        if nums[M] >= target:
            R = M - 1
        else:
            L = M + 1
    return L

test_input = [([1,3,5,6], 5), ([1,3,5,6], 2), ([1,3,5,6], 7), ([1,3,5,6], 0)]
test_output = [2, 1, 4, 0]
for i in range(len(test_input)):
    print(searchInsert(test_input[i][0], test_input[i][1]) == test_output[i])

#ZKP
# 61. Pow(x,n) (medium)

def myPow(x, n):
	if n < 0:
		x, n = 1 / x, - n
	ans = 1
	for i in range(n):
		ans *= x
	return ans

# faster
def myPow1(x, n):
	if n < 0:
		x, n = 1 / x, -n
	ans, bas = 1, x
	while n:
		if n & 1:
			ans *= bas
		bas *= bas
		n >>= 1
	return ans

print(myPow(2, 10), myPow1(2,10))
print(myPow(2.1, 3), myPow1(2.1, 3))
print(myPow(2, -2), myPow1(2, -2))


# 62. 58-Length of Last Word 

def lengthoflast(s):
	s = s.split()
	return 0 if len(s) == 0 else len(s[-1])

print(lengthoflast("Hello World"))
print(lengthoflast(" "))

# 63. 63-Unique Paths II (medium)
def Pathes(Grid):
	n, m = len(Grid), len(Grid[0])
	F = []
	for i in range(n):
		F.append([])
		for j in range(m):
			F[i].append(0)
	F[0][0] = 1
	for i in range(n):
		for j in range(m):
			if Grid[i][j] == 1:
				F[i][j] = 0
			elif (i, j) == (0, 0):
				continue
			elif j == 0:
				F[i][j] = F[i - 1][j]
			else:
				F[i][j] = F[i - 1][j] + F[i][j - 1]
	return F[n - 1][m - 1]

print(Pathes([[0,0,0],[0,1,0],[0,0,0]]))
print(Pathes([[0,1],[0,0]]))

# 64. 64-Minimum Path Sum (medium)
def MinPathSum(grid):
	Minsum = []
	n, m = len(grid), len(grid[0])
	for i in range(n):
		Minsum.append([])
		for j in range(m):
			Minsum[i].append(0)
	Minsum[0][0] = grid[0][0]
	for i in range(1, m):
		Minsum[0][i] = Minsum[0][i - 1] + grid[0][i]
	for i in range(1, n):
		for j in range(m):
			if j == 0:
				Minsum[i][j] = Minsum[i - 1][j] + grid[i][j]
			else:
				Minsum[i][j] = min(
					Minsum[i - 1][j], Minsum[i][j - 1]
				) + grid[i][j]
	return Minsum[n - 1][m - 1]

print(MinPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(MinPathSum([[1,2,3],[4,5,6]]))

# 65. 66-Plus One
def plusOne(digits):
	digits[-1] += 1
	index, n = -2, len(digits)
	res, digits[-1] = divmod(digits[-1], 10)
	while index >= -n and res > 0:
		digits[index] += res
		res, digits[index] = divmod(digits[index], 10)
		index -= 1
	if index < -n and res > 0:
		return [res] + digits
	else:
		return digits

print(plusOne([1,2,3,4]))
print(plusOne([9,9,9]))

# 66. 67-Add Binary

def addBinary(a, b):
	index, lena, lenb = -1, len(a), len(b)
	if lena < lenb:
		a, b, lena, lenb = b, a, lenb, lena
	b = (lena - lenb) * "0" + b
	lenb = lena
	res, ans = 0, ""
	while index >= -lena:
		res = int(a[index]) + int(b[index]) + res
		x, res = res % 2, res // 2
		ans += str(x)
		index -= 1
	if res > 0:
		ans += str(res)
	return ans[::-1]

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))

# 67. 69-Sqrt(x)

def mySqrt(x):
	ans = 0
	while ans * ans <= x:
		ans += 1
	return ans - 1

print(mySqrt(8))

# 68. 70-Climbing Stairs

def climbStairs(n):
	TwoStepsForward, OneStepForward, ans = 1, 1, 1
	for i in range(2, n + 1):
		ans = TwoStepsForward + OneStepForward
		TwoStepsForward = OneStepForward
		OneStepForward = ans
	return ans

print(climbStairs(5))
print(climbStairs(3))

# 69. 88-Merge Sorted Array
def merge(nums1, m, nums2, n):
	"""
	Do not return anything, modify nums1 in-place instead.
	"""
	ans = []
	index1, index2 = 0, 0
	while index1 < m and index2 < n:
		if nums1[index1] < nums2[index2]:
			ans.append(nums1[index1])
			index1 += 1
		else:
			ans.append(nums2[index2])
			index2 += 1
	while index1 < m:
		ans.append(nums1[index1])
		index1 += 1
	while index2 < n:
		ans.append(nums2[index2])
		index2 += 1
	for i in range(m + n):
		nums1[i] = ans[i]

templist = [1,2,3,0,0,0]
merge(
	nums1 = templist, m = 3,
	nums2 = [2,5,6],  n = 3
)
print(templist)

# 70. 121-Best Time to Buy and Sell Stock 
def maxProfit(prices):
	if len(prices) == 0:
		return 0
	ans, current_min = 0, prices[0]
	for i in range(1, len(prices)):
		ans = max(ans, prices[i] - current_min)
		current_min = min(current_min, prices[i])
	return ans

print(maxProfit([7,1,5,3,6,4]))


# LYM
# 71 125-Valid Palindrome

def isPalindrome(s):
	left = 0
	right = len(s) - 1
	while left < right:
		if not s[left].isalnum():
			left += 1
			continue
		if not s[right].isalnum():
			right -= 1
			continue
		if s[left].lower() != s[right].lower():
			return False
		left += 1
		right -= 1
	return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))

# 72 136-Single Number

# method 1
def singleNumber(nums):
	s = set()
	for num in nums:
		if num in s:
			s.remove(num)
		else:
			s.add(num)
	return s.pop()

# method 2
def singleNumber(nums):
	ans = 0
	for num in nums:
		ans ^= num
	return ans

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))

# 73 137-Single Number II

def singleNumber(nums):
	d = dict()
	for num in nums:
		if num not in d:
			d[num] = True
		elif d[num]:
			d[num] = False
		else:
			d.pop(num)
	return d.popitem()[0]

print(singleNumber([2,2,3,2]))
print(singleNumber([0,1,0,1,0,1,99]))

# 74 167-Two Sum II - Input array is sorted

def twoSum(numbers, target):
	left = 0
	right = len(numbers) - 1
	while left < right:
		if numbers[left] + numbers[right] == target:
			return [left+1, right+1]
		if numbers[left] + numbers[right] > target:
			right -= 1
		else:
			left += 1

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))

# 75 169-Majority Element

def majorityElement(nums):
	count = 0
	ans = 0
	for num in nums:
		if count == 0:
			ans = num
			count += 1
		elif ans != num:
			count -= 1
		else:
			count += 1
	return ans

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))

# 76 172-Factorial Trailing Zeroes

def trailingZeroes(n):
	# 2 * 5 = 10, 5 is more than 2.
	ans = 0
	while n > 0:
		n //= 5
		ans += n
	return ans
	
print(trailingZeroes(3))
print(trailingZeroes(5))

# 77 189-Rotate Array (Medium)


def reverse(nums, begin, end):
	while begin < end:
		nums[begin], nums[end] = nums[end], nums[begin]
		begin += 1
		end -= 1

def rotate(nums, k):
	"""
	Do not return anything, modify nums in-place instead.
	"""
	k %= len(nums)
	reverse(nums, 0, len(nums) - 1)
	reverse(nums, 0, k - 1)
	reverse(nums, k, len(nums) - 1)

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)

# 78 190-Reverse Bits

def reverseBits(n):
	nb = bin(n)[2:]
	nb = '0' * (32 - len(nb)) + nb
	ansb = nb[::-1]
	return int(ansb, 2)

print(reverseBits(0b00000010100101000001111010011100))
print(reverseBits(0b11111111111111111111111111111101))

# 79 191-Number of 1 Bits

def hammingWeight(n):
	nb = bin(n)
	return nb.count('1')

print(hammingWeight(0b00000000000000000000000000001011))
print(hammingWeight(0b00000000000000000000000010000000))

# 80 746-Min Cost Climbing Stairs

def minCostClimbingStairs(cost):
	for i in range(2, len(cost)):
		cost[i] += min(cost[i-1], cost[i-2])
	return min(cost[-1], cost[-2])

print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


# Li Sen

# 81
def transpose(A: List[List[int]]) -> List[List[int]]:
    r, c = len(A), len(A[0])
    res = [[None]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][i] = A[i][j]
    return res

# 82
def binaryGap(n: int) -> int:
    zerosNum = [len(i) for i in bin(n)[2:].split('1')]
    if len(zerosNum) == 2:
        return 0
    return max(zerosNum[:-1]) + 1

# 83
def uncommonFromSentences(A: str, B: str) -> List[str]:
    count = {}
    for word in A.split():
        count[word] = count.get(word, 0) + 1
    for word in B.split():
        count[word] = count.get(word, 0) + 1
    return [word for word in count if count[word] == 1]

# 84
def fairCandySwap(A: List[int], B: List[int]) -> List[int]:
    for x in A:
        if (x + ((sum(B) - sum(A))//2)) in B:
            return [x, x + ((sum(B) - sum(A))//2)]

# 85
def numSpecialEquivGroups(A: List[str]) -> int:
    def convert(s):
        ans = [0] * 52
        for i in range(len(s)):
            if i%2==0:
                ans[ord(s[i]) - ord('a')] += 1
            else:
                ans[ord(s[i]) - ord('a') + 26] += 1
        return str(ans)

    c = {}
    p = [convert(x) for x in A]
    for i in p:
        c[i] = c.get(i,0) + 1
    return len(c.values())

# 86
def isMonotonic(A: List[int]) -> bool:
    def isMonotonic(A: List[int]) -> bool:
        return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

# 87
def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    return sorted(A, key=lambda x: x % 2)

# 88
def smallestRangeI(A, K):
    return max(0, max(A) - min(A) - 2 * K)

# 89
def hasGroupsSizeX(deck: List[int]) -> bool:
    count = {}
    for i in deck:
        count[i] = count.get(i, 0 ) + 1
    return reduce(math.gcd, count.values())>=2

# 90
def reverseOnlyLetters(S: str) -> str:
    letters = [c for c in S if c.isalpha()]
    ans = []
    for c in S:
        if c.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(c)
    return "".join(ans)


print(transpose([[1,2],[3,4]]))
print(binaryGap(3))
print(uncommonFromSentences("nice to meet you","how are you"))
print(fairCandySwap([1,2,5], [2,4]))
print(numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
print(hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))

#91-100 JLH

#91. 921(Medium)
def minAddToMakeValid(S: str) -> int:
    res = 0
    bal = 0
    for symbol in S:
        if symbol == '(':
            bal += 1
        else:
            bal -= 1
        if bal == -1:
            res += 1
            bal += 1
    return res + bal

print(minAddToMakeValid("())"))
print(minAddToMakeValid("((("))
print(minAddToMakeValid("()"))
print(minAddToMakeValid("()))(("))



#92. 922
def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    res = [0] * len(A)
    pos_odd = 1
    pos_even = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            res[pos_even] = A[i]
            pos_even += 2
        else:
            res[pos_odd] = A[i]
            pos_odd += 2
    return res

print(sortArrayByParityII([4,2,5,7]))




#93. 925
def isLongPressedName(name, typed):
    """
    :type name: str
    :type typed: str
    :rtype: bool
    """
    pos_n = 1
    pos_t = 1
    while pos_n < len(name) and pos_t < len(typed):
        if name[pos_n] == typed[pos_t]:
            pos_n += 1
            pos_t += 1
        else:
            if pos_t > 0 and typed[pos_t] == typed[pos_t-1]:
                pos_t += 1
            else:
                return False
    return pos_n == len(name) and len(set(typed[pos_t-1:])) == 1
print(isLongPressedName("alex","aaleex"))
print(isLongPressedName("saeed","ssaaedd"))
print(isLongPressedName("leelee","lleeelee"))
print(isLongPressedName("laiden","laiden"))




#94. 932(Medium)
def beautifulArray(N: int):
    memo = {1: [1]}
    def f(N):
        if N not in memo:
            odds = f((N + 1) // 2)
            evens = f(N // 2)
            memo[N] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
        return memo[N]
    return f(N)

print(beautifulArray(4))
print(beautifulArray(5))



#95. 933
class RecentCounter:
    def __init__(self):
        self.cnt = 0
        self.l = []

    def ping(self, t: int) -> int:
        self.l.append(t)
        while t and self.l[0] + 3000 < t:
            self.l.pop(0)
        return len(self.l)

obj = RecentCounter()
res = []
for t in [1,100,3001,3002]:
    res.append(obj.ping(t))
print(res)



#96. 937
def reorderLogFiles(logs):
    def f(log):
        id_, rest = log.split(" ", 1)
        if rest[0].isalpha():
            return (0, rest, id_)
        else:
            return (1,)

    return sorted(logs, key = f)

print(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))




#97. 939(Medium)
def minAreaRect(points) -> int:
    columns = {}

    for x, y in points:
        if x in columns:
            columns[x].append(y)
        else:
            columns[x] = [y]

    lastx = {}
    res = float('inf')

    for x in sorted(columns):
        column = columns[x]
        column.sort()
        for j, y2 in enumerate(column):
            for i in range(j):
                y1 = column[i]
                if (y1, y2) in lastx:
                    res = min(res, (x - lastx[y1,y2]) * (y2 - y1))
                lastx[y1, y2] = x

    if res < float('inf'):
        return res
    else:
        return 0

print(minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))



#98. 941
def validMountainArray(A) -> bool:
    if len(A) < 3:
        return False
    i = 0
    while i < len(A) - 1:
        if A[i] == A[i + 1]:
            return False
        elif A[i] > A[i + 1]:             
            break
        i += 1
    if i == len(A) - 1 or i == 0:
        return False
    i += 1
    while i < len(A) - 1:
        if A[i] <= A[i + 1]:
            return False
        i += 1
    return True
print(validMountainArray([2,1]))
print(validMountainArray([3,5,5]))
print(validMountainArray([0,3,2,1]))




#99. 942
def diStringMatch(S: str):
    low = 0 
    high = len(S)
    res = []
    for x in S:
        if x == 'I':
            res.append(low)
            low += 1
        else:
            res.append(high)
            high -= 1

    return res + [low]

print(diStringMatch("IDID"))
print(diStringMatch("III"))
print(diStringMatch("DDI"))




#100. 944
def minDeletionSize(A) -> int:
    res = 0
    for j in range(len(A[0])):
        for i in range(1,len(A)):
            if A[i][j] < A[i-1][j]:
                res += 1
                break
    return res

print(minDeletionSize(["cba", "daf", "ghi"]))
print(minDeletionSize(["a", "b"]))
print(minDeletionSize(["zyx", "wvu", "tsr"]))