# from:

x = 1
y = 2
z = 3

f, g = 0, 1

q = "Hello, world!"
r = "Hello, \"world\"!"
s = 'Hello, \"world\"!'
t = 'Hello, \"world!'
u = 'Hello, \"\"\"world!'


def function_name(x, y, z):
    return x


def myfun(x, y):
    if x > y < 0:
        return x


def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

