# 삼각함수 계산


from math import sqrt
from math import acos
from math import degrees

AB = int(input())
BC = int(input())

AC = sqrt(AB ** 2 + BC ** 2)

angle = acos(BC / AC)

print("{}{}".format(round(degrees(angle)), chr(176)))