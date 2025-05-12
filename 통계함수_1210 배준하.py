import math
lst = list(range(1,11))

mean = sum(lst) / len(lst)
print(f"평균 : {mean}")

vsum = 0
for x in lst:
    vsum += (x - mean)**2
    var = len(lst)
print(f"분산: {int(var)}")

std = math.sqrt(var)
print(f"표준편차: {std}")

gcd = math.gcd(*lst)