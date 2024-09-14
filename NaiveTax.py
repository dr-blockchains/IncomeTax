level = [0, 9700, 39_475, 84_200, 160_725, 204_100, 510_300]
rate = [.10, .12, .22, .24, .32, .35, .37]

income = float(input("\n Taxable income = $"))

if income <= level[1]:
    tax = income * rate[0]
elif income <= level[2]:
    t0 = level[1]*rate[0]
    tax = t0 + (income - level[1]) * rate[1]
elif income <= level[3]:
    t0 = level[1] * rate[0] + (level[2]-level[1]) * rate[1]
    tax = t0 + (income - level[2]) * rate[2]
elif income <= level[4]:
    t0 = level[1] * rate[0] + (level[2] - level[1]) * rate[1] \
         + (level[3] - level[2]) * rate[2]
    tax = t0 + (income - level[3]) * rate[3]
elif income <= level[5]:
    t0 = level[1] * rate[0] + (level[2] - level[1]) * rate[1] \
         + (level[3] - level[2]) * rate[2] + (level[4] - level[3]) * rate[3]
    tax = t0 + (income - level[4]) * rate[4]
elif income <= level[6]:
    t0 = level[1] * rate[0] + (level[2] - level[1]) * rate[1] \
         + (level[3] - level[2]) * rate[2] + (level[4] - level[3]) * rate[3] \
         + (level[5] - level[4]) * rate[4]
    tax = t0 + (income - level[5]) * rate[5]
else:
    t0 = level[1] * rate[0] + (level[2] - level[1]) * rate[1] \
         + (level[3] - level[2]) * rate[2] + (level[4] - level[3]) * rate[3] \
         + (level[5] - level[4]) * rate[4] + (level[6] - level[5]) * rate[5]
    tax = t0 + (income - level[6]) * rate[6]

print("\n You income tax = $", tax)
