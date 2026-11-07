import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x[0]**2-2*x[0]*x[1]+x[1]**2+4*x[0]+3*x[1]

def exp_move(b, h):
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    if f(b+h[0]*e1)<f(b):
        b = b+h[0]*e1
    elif f(b-h[0]*e1)<f(b):
        b = b-h[0]*e1

    if f(b+h[1]*e2)<f(b):
        b = b+h[1]*e2
    elif f(b-h[1]*e2)<f(b):
        b = b-h[1]*e2

    return b

def hjmethod(b1, h, epsilon):

    while max(h) >= epsilon:
        b2 = exp_move(b1, h)

        if f(b2)<f(b1):
            p1 = 2*b2 - b1
            p2 = exp_move(p1, h)

            if f(p2)<f(b2):
                b1 = p2
            else:
                b1 = exp_move(b2, h)

        else:
            h = h/2

    return b1


b1 = np.array([0, 0])
h = np.array([1, 1])

xsol = hjmethod(b1, h, epsilon = 0.25)
print(xsol)