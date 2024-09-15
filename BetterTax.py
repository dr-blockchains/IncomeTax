import math

# Federal tax brackets and rates 
brackets = [0, 9700, 39_475, 84_200, 160_725, 204_100, 510_300, math.inf]
rates = [.10, .12, .22, .24, .32, .35, .37]

# Get income from the user 
try:
    income = float(input("Enter your taxable income: $"))
except ValueError:
    print("Invalid input. Please enter a valid number for your income.")
    exit()

k = 0
FullBrackets = 0

while income > brackets[k + 1]:
  FullBrackets += rates[k] * (brackets[k + 1] - brackets[k])
  k += 1

tax = FullBrackets + rates[k] * (income - brackets[k])

print("Your tax bracket: ", brackets[k],'-', brackets[k+1])
print("Tax for Full Brackets = $", FullBrackets)
print("Your income tax = $", tax)
