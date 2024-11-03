# FIB
import numpy as np
def fibonacci(n, k):
    if n == 1 or n == 2:
        return 1
    F = np.arange(0,n+1)
    F[1] = 1 
    F[2] = 1  
    for i in range(3, n + 1):
        F[i] = F[i - 1] + k * F[i - 2]
    return F[n]
print(fibonacci(29,3))
