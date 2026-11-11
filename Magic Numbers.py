# Work in progress


def _142857():          # Magic Number: 142857 -> Multiplying by all numbers in [1, 6] gives the same dequence of numbers rotated.
    for i in range(1, 7):
        x = i * 142857
        print(f"{i} x 142857 = ", x)

    print("Magic Number: 142857, due to its rotated sequence of digits when multiplied by numbers from 1 to 6 (seen above).")
_142857()



def _1729():            # Magic Number: 1729 or 'Hardy- Ramanujan number' -> smallest number that can be expressed as the sum of two cubes in 2 different ways. (Hard one to code)
    n = 1

    while True:

        c = 0
        xsol = []
        limit = int((n ** (1/3)) + 1)

        for a in range(1, limit + 1):
            for b in range(a + 1, limit + 1):
                    if a ** 3 + b ** 3 == n:
                        c += 1
                        xsol.append((a, b))

        if c == 2:
            print(n)
            print(xsol)
            print("Magic Number: 1729, the smallest positive integer able to be expressed as two different sums of cubes (shown above).")

            return n
        else:
            n += 1


    
_1729()


def perfectnumbers():

    n = 1

    while n <= 1000:

        xsol = []

        for a in range(1, n):
            if n % a == 0:
                xsol.append(a)

        if sum(xsol) == n:
            print(xsol)
            print(n)
        
        
        n+=1

    print("Perfect Numbers: The sums of their divisive counterparts equal themselves! (shown above up till 1000).")

perfectnumbers()
                

print(9 + 99 + 999 + 9999 + 99999 + 999999)
print(123456 * 9)





