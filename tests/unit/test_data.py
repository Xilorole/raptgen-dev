from context import raptgen
from raptgen import data
import torch


def test_one_hot_index():
    # Test case 1
    seq = "ATGC"
    expected_output = [0, 1, 2, 3]
    assert data.one_hot_index(seq) == expected_output

    # Test case 2
    seq = "CTAG"
    expected_output = [3, 1, 0, 2]
    assert data.one_hot_index(seq) == expected_output

    # Test case 3
    seq = "AGCT"
    expected_output = [0, 2, 3, 1]
    assert data.one_hot_index(seq) == expected_output
