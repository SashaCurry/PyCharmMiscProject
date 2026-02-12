import numpy as np

array = np.zeros(100, dtype=bool)
simples = np.empty(0, dtype=int)
for i in range (2, 101):
    is_simple = True
    for simple in simples:
        if i % simple == 0:
            is_simple = False
            break
    if is_simple:
        array[i - 1] = True
        simples = np.append(simples, i)
print(array)