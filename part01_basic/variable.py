a = 321
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # 整除
print(a % b)  # 模
print(a ** b)  # 指数


a = 100
b = 12.345
c = 1 + 5j  # 这个j是个啥意思
d = 'hello, world'
e = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'> 复数
print(type(d))  # <class 'str'>
print(type(e))  # <class 'bool'>

#  比较运算符 和 逻辑运算符
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False

# 获取输入 类型转换
a = int(input('a = '))
b = int(input('b = '))
# 格式化输入 第四个百分号表示呢容来源，对应相等
print('%d + %d = %d' % (a, b, a + b))

"""
输入年份 如果是闰年输出True 否则输出False
"""

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)