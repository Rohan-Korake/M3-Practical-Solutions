import math

x = 5
n = 5
p = 0.4
q = 0.6

result = ( math.factorial(n) / (math.factorial(x) * math.factorial( n - x ))) * (( p ** x ) * ( q ** ( n - x )))

print("Binomial Distribution : ",result)