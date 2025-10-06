from selection import selection
import numpy as np

def test_selection_zero():
    arr = []
    try:
        selection(arr, 0)
    except ValueError as e:
        assert str(e) == "Length of the array can't be zero."

def test_selection_small():
    for l in range(1, 10):
        arr = np.random.random(l)
        sorted_arr = sorted(arr)
        for k in range(l):
            assert selection(arr, k) == sorted_arr[k]