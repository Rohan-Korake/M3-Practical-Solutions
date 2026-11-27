import numpy as np

P = np.array([[0.7,0.3],[0.4,0.6]])

n = 2

result = np.linalg.matrix_power(P,n)

print("Transition Probability Matrix : ")
print(P)

print(n,"-step Distribution Matrix : ")
print(result)