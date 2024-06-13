def constant(func):
    return 1


@constant
def double(x):
    return x * 2


print(double)
