import mpmath as mp
import matplotlib.pyplot as plt
from collections import Counter


mp.mp.dps = 100000

p = str(mp.pi)
p = p.replace(".","")

def pirw():     #to think about: remove the last group of each i as not full set so fucks up distribution

    for i in range(1, 16):
        groups = []

        for n in range(0, len(p), i):
            groups.append(p[n : n + i])

        # print(groups)
        sums = []

        for group in groups[0: -1]:     #now time to remove the last group for each set("groups") made by i

            total = 0

            for digit in group:     #main confusion is getting my head around the 3 different groups we consider (sums in groups for each i)
                total += int(digit)

            sums.append(total)

        freq = Counter(sums)
        plt.bar(freq.keys(), freq.values(), color = "darkcyan")
        plt.xlabel("Sums of Digits")
        plt.ylabel("Frequency")
        plt.title(f"Distribution of Digit Sums for {i}-Digit Groups of π")

        #plt.grid(axis="y", alpha = 0.15)    #Copilot used for a lot of the distribution plotting code
        plt.show()

pirw()