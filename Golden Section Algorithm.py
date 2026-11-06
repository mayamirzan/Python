import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return -1/(x-1)**2*(np.log(x)-2*((x-1)/(x+1)))

def gsection(a, b, epsilon):
    gr = 0.618

    x1 = b-gr*(b-a)
    x2 = a+gr*(b-a)

    while (b-a)>epsilon:
        if f(x2)>f(x1):
            b=x2
            x2=x1
            x1=b-gr*(b-a)
        else:
            a=x1
            x1=x2
            x2=a+gr*(b-a)
        

        plt.plot(x, f(x))
        plt.scatter([a, b], [f(a), f(b)], color = "black")
        plt.plot([x1, x2], [f(x1), f(x2)], color="red")
        plt.show()
        
    return (a+b)/2



a=1.5
b=4.5
x=np.arange(a, b, (b-a)/100)

fig=plt.plot(x, f(x))
plt.show()

xsol=gsection(a, b, epsilon=0.2)
print(xsol)