import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -1/(x-1)**2 *(np.log(x)-2*(x-1)/(x+1))

def fibseq(N):
    fib = np.zeros(N+1)
    fib[0]=1
    fib[1]=1

    for i in range(2, N+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib


def fibonacci(a, b, N):

    fib = fibseq(N)

    x1 = fib[N-2]/fib[N]*(b-a) + a
    x2 = fib[N-1]/fib[N]*(b-a) + a

    for i in range(2, N-1):
        if f(x2)>f(x1):
            b = x2
            x2 = x1
            x1 = fib[N-i-1]/fib[N-i+1]*(b-a) + a
        else:
            a = x1
            x1 = x2
            x2 = fib[N-i]/fib[N-i+1]*(b-a) + a


    plt.plot(x, f(x))
    plt.scatter([a, b], [f(a), f(b)], color = "black")
    plt.plot([x1, x2], [f(x1), f(x2)], color="red")
    plt.show()

    return (a+b)/2


a = 1.5
b = 4.5
x = np.arange(a, b, (b-a)/100)

fig = plt.plot(x, f(x))
plt.show()

xsol = fibonacci(a, b, N=7)
print(xsol)

