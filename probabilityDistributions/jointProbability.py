import numpy as np

X = [ 0 , 1 ]
Y = [ 0 , 1 ]

P = np.array([[ 0.1 , 0.2 ],[ 0.3 , 0.4 ]])
print("Point Probability Mass Function : ")

for i in range(len(X)):
    for j in range(len(Y)):
        print("P(X = {}, Y ={}) = {}".format(X[i],Y[j],P[i][j]))

print("Total Probability : ",np.sum(P))
