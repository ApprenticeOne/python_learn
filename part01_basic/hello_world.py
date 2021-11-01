import sys

print('hello, world!')
print("你好,世界！")
print('你好', '世界')

'''
help(print)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        Prints the values to a stream, or to sys.stdout by default.
        输出对象到流，多个对象需要分隔符
        
        Optional keyword arguments:
            file:  a file-like object (stream); defaults to the current sys.stdout. 写入文件对象???
            sep:   string inserted between values, default a space. 分隔符 默认空格
            end:   string appended after the last value, default a newline. 结尾 默认'\n'
            flush: whether to forcibly flush the stream. 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。我不理解
'''
open('test.txt', 'w')  # 只能写
print('hello', file=sys.stdout)  # 我不理解
print('hello', 'world', sep=', ', end='!')  # 不存在'\n' 结尾不换行
print('goodbye, world', end='!\n')
