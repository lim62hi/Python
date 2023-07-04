import numpy as np
mas1 = np.array([1, 2, 3])
mas2 = np.array([[1, 2, 3], [1, 2, 3]])
mas3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype='float32')

print(f'{mas1}\n\n\n{mas2}\n\n\n{mas3}\n')
print(mas1.ndim)
print(mas3.shape)
print(mas2.size)
print(mas2.itemsize)
print(mas2.nbytes)
print(mas3[:, 0])