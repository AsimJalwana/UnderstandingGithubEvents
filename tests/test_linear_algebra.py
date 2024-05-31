import numpy as np
from linearalgebraasimjalwana0123.la import find_inverse


def test_invalid_find_inverse():
    assert find_inverse(None) is None


def test_valid_find_inverse():
    matrix = [[1, 2], [3, 4]]
    expected = [[-2., 1.],
                [1.5, -0.5]]
    assert np.isclose(find_inverse(matrix), expected, atol=0.01).all()
