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


def comp_Num(cte, ast):
    val = ast.x  # literal value
    def code(rte, cont):
        return step_end(rte, cont, ast, val)
    return code


def byte_at(x, i):
    # returns an integer between 0 and 255
    if type(x) is str:
        return ord(x[i])
    else:
        return x[i]

x[i] = 2
p[k]
byte_at(r, s)
