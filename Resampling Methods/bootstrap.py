import numpy as np


def bootstrap(arr: np.ndarray, n_loops: int) -> np.ndarray:
    sample_size = len(arr)
    indices = np.random.randint(sample_size, size=(n_loops, sample_size))
    bootstrap_samples = arr[indices]
    return bootstrap_samples.mean()


sample = np.random.random(1000)
b_mean = bootstrap(sample, n_loops=100)
