import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
 
vals, vecs = np.linalg.eig(A)
print("Eigenvalues:", vals)
