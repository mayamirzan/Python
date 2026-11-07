import matplotlib.pyplot as plt

file = open("weights.csv", "r")
y = []

for weight in file:
    y.append(float(weight))

file.close()

weight = float(input("Today's weight: "))
y.append(weight)

file = open("weights.csv", "a")
file.write(str(weight) + "\n")
file.close()

x = range(1, len(y) +1)

plt.plot(x, y, color = "black")
plt.xlabel("Day")
plt.ylabel("Weight (kg)")
plt.title("My weight change.")
plt.show()