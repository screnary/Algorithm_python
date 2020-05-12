""" 牛客网，输入输出练习 """

import sys

# 输入多行，输出每行两数和
while True:
    line = sys.stdin.readline()
    if not line:
        break
    a, b = map(int, line.strip().split())
    print(a+b)


# 输入第一行包括一个数据组数
# t = int(sys.stdin.readline().strip())
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)


# 链接：https://ac.nowcoder.com/acm/contest/320/C
# 输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入
while True:
    line = sys.stdin.readline().strip()
    if not line: break
    a, b = map(int, line.split())
    if a==0 and b==0: break
    print(a+b)


# 输入数据包括多组。
# 每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
# 接下来n个正整数,即需要求和的每个正整数。
while True:
    line = sys.stdin.readline().strip()
    nums = list(map(int,line.split()))
    if nums[0]==0: break
    print(sum(nums[1:]))


# 输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
# 接下来t行, 每行一组数据。
# 每行的第一个整数为整数的个数n(1 <= n <= 100)。
# 接下来n个正整数, 即需要求和的每个正整数。
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    print(sum(nums[1:]))


"""链接：https://ac.nowcoder.com/acm/contest/320/F
输入数据有多组, 每行表示一组输入数据。
每行的第一个整数为整数的个数n(1 <= n <= 100)。
接下来n个正整数, 即需要求和的每个正整数。"""
while True:
    line = sys.stdin.readline()
    if not line: break
    nums = list(map(int, line.strip().split()))
    print(sum(nums[1:]))

"""
输入数据有多组, 每行表示一组输入数据。
每行不定有n个整数，空格隔开。(1 <= n <= 100)。
"""
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    nums = list(map(int, line.split()))
    print(sum(nums))


""" 对输入的字符串进行排序后输出
输入有两行，第一行n
第二行是n个空格隔开的字符串

输出一行排序后的字符串，空格隔开，无结尾空格
"""
n = int(input())
str_list = list(input().split(' '))
str_list.sort()
res = ""
for s in str_list:
    res += s + " "
print(res.strip())

""" 多个测试用例，每个测试用例一行。

每行通过空格隔开，有n个字符，n＜100
"""
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    str_list = line.split()
    str_list.sort()
    res = ""
    for s in str_list:
        res += s+" "
    print(res.strip())

""" 多个测试用例，每个测试用例一行。
每行通过,隔开，有n个字符，n＜100
对于每组用例输出一行排序后的字符串，用','隔开，无结尾空格
"""
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    str_list = line.split(",")
    str_list.sort()
    res = ""
    for s in str_list:
        res += s+","
    print(res.rstrip(","))  # right strip