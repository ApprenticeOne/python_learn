import random

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
