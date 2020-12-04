import numpy as np

m_list = [[1, 2, -1, 1], [2, 5, 1, 1], [1, 3, 2, 1], [3, 7, -1, 3]]
A = np.array(m_list)

inv_A = np.linalg.inv(A)

print(inv_A)

B = np.array([0, 4, 5, 2])
X = np.linalg.inv(A).dot(B)

print(X)

X2 = np.linalg.solve(A,B)

print(X2)
