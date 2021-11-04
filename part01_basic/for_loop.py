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

