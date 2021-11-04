import random
from math import sqrt

sum = 0
for x in range(101):
    sum += x
print(sum)
'''
range(101)  0-100 一共101个数

range(1,101) 1-100

range(1,101,2)  1-100间的奇数 步长为2

range(100,0,-2) 100-0间的偶数 步长为-2

'''
sum = 0
for x in range(100, 0, -2):
    sum += x
print(sum)

# while
# 0-100间的随机数
answer = random.randint(0, 100)
count = 0

while True:
    count += 1
    number = int(input("Please enter the number: "))
    if number < answer:
        print("more larger")
    elif number > answer:
        print("more smaller")
    else:
        print("right")
print('you got d% times to get right answer' % count)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

# 输入一个正整数判断是不是素数

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
# 为什么要放一个end 如果这个数有一个小于sqrt的因数
# 就一定会有一个大于sqrt的因数与之对应
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

