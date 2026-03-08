

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6   

def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15                    # entire array is the answer

def test_all_negative():
    assert max_subarray_sum([-3, -1, -2]) == -1                       # least negative number wins

def test_single_positive():
    assert max_subarray_sum([5]) == 5                                  # single element

def test_single_negative():
    assert max_subarray_sum([-5]) == -5                                # single negative element

def test_single_zero():
    assert max_subarray_sum([0]) == 0                                  # single zero

def test_contains_zero():
    assert max_subarray_sum([0, -1, 2, 0, 3]) == 5                    # zeros in the middle

def test_large_negative_with_positive():
    assert max_subarray_sum([-100, 50, -1, 50]) == 99                 # big negative at start

def test_empty_list():
    with pytest.raises(ValueError, match="empty list"):
        max_subarray_sum([])                                           # empty list should raise

if __name__ == "__main__":
    pytest.main()