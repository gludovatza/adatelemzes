# https://www.w3schools.com/python/numpy/numpy_getting_started.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print([1, 2, 3, 4, 5])
print(type(arr))
print(type([1, 2, 3, 4, 5]))

print(np.__version__)

# https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp

print(np.array(42))

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) 

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

# https://www.w3schools.com/python/numpy/numpy_array_indexing.asp

arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2] + arr[3])

c = np.array([[1, 2, 3], [4, 5, 6]])
print(c[1,2])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
print('2nd element on 1st row: ', arr[0, 1]) 

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

arr = np.array([1, 2, 3, 4])
print(arr[-1])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) 

# https://www.w3schools.com/python/numpy/numpy_array_slicing.asp

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[4:]) 
print(arr[:4]) 

print(arr[-3:-1])

print(arr[1:5:2]) 

print(arr[::2]) 

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

print(arr[0:2, 2]) # kiadja a 3 és 8 elemeket
print(arr[3:9, 2]) # hibát jelezhetne, mert nincs ennyi sora az tömbnek, de a numpy nem jelez hibát, csak a létező sorokat adja vissza, ami itt most üres eredményt ad vissza

# https://www.w3schools.com/python/numpy/numpy_data_types.asp

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype) 

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

arr = np.array(['a', 2, 3, 4])

print(arr.dtype)

arr = np.array('2025-10-23', dtype='M') # datetime64[D] -t jelent. M => YYYY-MM-DD, például: 2025-10-23
print(arr.dtype)

arr = np.array('2025-10-23', dtype='datetime64[M]') # például: 2025-10
print(arr.dtype)

arr = np.array('2025-10-23', dtype='datetime64[s]') # például: 2025-10-23T15:10:00
print(arr.dtype)
print(arr)

start = np.datetime64('2025-01-01')
end   = np.datetime64('2025-10-23')
delta = end - start
print(delta)         # 295 days
# print(delta / np.timedelta64(1, 'M'))  # ≈ 9.7 hónap

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 666666666])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype) 

# slicing with 2D arrays
B = np.array([
    [12, 7, 3, 8],
    [4, 5, 6, 2],
    [9, 1, 11, 10],
    [14, 0, 13, 15]
])

print(B)

# B[:2, :2] = 100

# print(B)

A = B[::2]
print(A)
even_numbers = A[A % 2 == 0]

print("\nPáros számok:", even_numbers)