## work in progess


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -1/(x-1)**2*(np.log(x)-2*((x-1)/(x+1)))


def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)

def fibalg(a, b, n):
    x1=(fib(n-2)/fib(n))*(b-a)+a
    x2 = (fin(n-1)/fib(n))*(b-a)+a

    while f(x2)>f(x1):
        b=x2
    else:
        a=x1

    plt.plot(x, f(x))


    return (b-a)/2
