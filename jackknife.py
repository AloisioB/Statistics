import numpy as np


def jackknife(arr) -> float:
    n = len(arr)
    average = np.empty(n)
    for i in range(n):
        subsample = np.delete(arr, i)
        average[i] = subsample.mean()
    return np.mean(average)


data = np.random.random(1000)
j = jackknife(data)
