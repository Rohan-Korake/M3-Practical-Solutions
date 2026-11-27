import math

x1 = 86.7
x2 = 77.8
n1 = 50
n2 = 50
s1 = 6.28
s2 = 5.61
mean = 12

result = (( x1 - x2 ) - mean ) / math.sqrt(( s1**2 / n1 ) + ( s2**2 / n2 ))

print("Z Test Hypothesis:", result)
