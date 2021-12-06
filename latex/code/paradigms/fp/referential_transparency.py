def f1(x):
    return x**2


def f2(x):
    print(x)
    return x**2


y = 0


def f3(x):
    global y
    y += 1
    return x + y


def f4():
    return int(input()) + 1


def f5(lst: List):
    lst[0] = 3
    return lst
