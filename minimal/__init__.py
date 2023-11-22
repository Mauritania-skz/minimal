def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y
def multiplo(n):
    return n%5==0

def fibonacci(n):
    fibs = []
    a, b = 0, 1
    while a < n:
         if multiplo(a):
            fibs.append(a)
         a, b = b, a+b
    return fibs
