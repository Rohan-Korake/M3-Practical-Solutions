import math

x = 5.0
mean = 5.0
std = 2

result = ( 1 / ( std * math.sqrt( 2 * 3.14 ))) * math.exp( - (( x - mean ) ** 2) / ( 2 * std ) ** 2)

print("Normal Distribution : ",result)