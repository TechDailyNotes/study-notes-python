def gen(num):
    while num > 0:
        yield num
        num -= 1


g = gen(5)
for i in g:
    print(i)
