from context import raptgen
from raptgen.data import one_hot_encode, one_hot_index
import torch
import numpy as np


def test_one_hot_index():
    # Test case 1
    seq = "ATGC"
    expected_output = [0, 1, 2, 3]
    assert one_hot_index(seq) == expected_output

    # Test case 2
    seq = "CTAG"
    expected_output = [3, 1, 0, 2]
    assert one_hot_index(seq) == expected_output

    # Test case 3
    seq = "AGCT"
    expected_output = [0, 2, 3, 1]
    assert one_hot_index(seq) == expected_output


def test_one_hot_encode():
    # Test case 1
    seq = "ATGC"
    expected_output = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    assert np.array_equal(one_hot_encode(seq), expected_output)

    # Test case 2
    seq = "CTAG"
    expected_output = np.array([[0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]])
    assert np.array_equal(one_hot_encode(seq), expected_output)

    # Test case 3
    seq = "AGCT"
    expected_output = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
    assert np.array_equal(one_hot_encode(seq), expected_output)

    # Test case 4
    seq = "ATGC"
    padding = 2
    expected_output = np.array(
        [
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
        ]
    )
    assert np.array_equal(one_hot_encode(seq, padding), expected_output)

    # Test case 5
    seq = "AGCT"
    padding = (2, 3)
    expected_output = np.array(
        [
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
        ]
    )
    assert np.array_equal(one_hot_encode(seq, padding), expected_output)

    # Test case 6
    seq = "AGCT"
    padding = (3, 2)
    expected_output = np.array(
        [
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
        ]
    )
