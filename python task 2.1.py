import numpy as np

m_list = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
A = np.array(m_list)

inv_A = np.linalg.inv(A)

print(inv_A)

B = np.array([11, 12, 13, 14])
X = np.linalg.inv(A).dot(B)

print(X)

X2 = np.linalg.solve(A,B)

print(X2)
