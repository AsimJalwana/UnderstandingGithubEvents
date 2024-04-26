import numpy as np


def find_inverse(matrix: np.ndarray) -> np.ndarray:
    if matrix is None:
        return None

    return np.linalg.inv(matrix)
