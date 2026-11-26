import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
 
vals, vecs = np.linalg.eig(A)

P = vecs
D = np.diag(vals)
P_inv = np.linalg.inv(P)

reconstructed = P @ D @ P_inv

print("Diagonalization : \n",reconstructed)