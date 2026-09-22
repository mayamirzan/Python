print("One day I will master this shit!")

prices = [100, 102, 101, 105, 107, 106, 110]

open = prices[0]
close = prices[-1]
high = max(prices)
low = min(prices)


print(open, close, high, low)

returns = ((close - open)/open)*100
print ("Return: ", returns)

for i in range(len(prices)):
    if i == 0:
        print (f"More information needed for day {i}'s daily return")
    else:
        daily_return =(prices[i]- prices[i-1])/prices[i-1] * 100
        daily_return = round(daily_return, 2)
        print (daily_return, '%')

daily_returns =[]
daily_returns.append(daily_return)
avg_dr = sum(daily_returns)/6
print("Average Daily Return: ", avg_dr)

for i in range(len(daily_returns)):
    square_diff = []
    square_diff.append((daily_returns[i] - avg_dr)**2)
sum_of_squares = sum(square_diff)
var_dv = sum_of_squares / 5
daily_volatility = round(var_dv ** (1/2), 3)

print(daily_volatility)