print('hello, world!')
print("你好,世界！")
print('你好', '世界')

'''
help(print)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
            file:  a file-like object (stream); defaults to the current sys.stdout.
            sep:   string inserted between values, default a space. 分隔符 默认空格
            end:   string appended after the last value, default a newline.
            flush: whether to forcibly flush the stream.
        
'''
print('hello', 'world', sep=', ', end='!')

print('goodbye, world', end='!\n')
