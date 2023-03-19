"""This module is used to create data, manage data for sequential input.
"""
from enum import IntEnum
from typing import List, Union, Tuple
import numpy as np


class State(IntEnum):
    """Enum for Profile HMM.
    M stands for Match, I stands for insertion and D stands for deletion."""

    M = 0
    MATCH = 0
    I = 1
    INSERTION = 1
    D = 2
    DELETION = 2


class Transition(IntEnum):
    """Enum for State-to-State transition."""

    M2M = 0
    MATCH_TO_MATCH = 0
    M2I = 1
    MATCH_TO_INSERTION = 1
    M2D = 2
    MATCH_TO_DELETION = 2
    I2M = 3
    INSERTION_TO_MATCH = 3
    I2I = 4
    INSERTION_TO_INSERTION = 4
    D2M = 5
    DELETION_TO_MATCH = 5
    D2D = 6
    DELETION_TO_DELETION = 6


class Nucleotide(IntEnum):
    """Enum for nucleotide."""

    A = 0
    T = 1
    U = 1
    G = 2
    C = 3
    N = 4
    PAD = 4
    SOS = 5
    EOS = 6


class SNV(IntEnum):
    """Enum for Single Nucleotide Variant"""

    MUTATION = 0
    INSERTION = 1
    DELETION = 2


def one_hot_index(seq: str) -> List[int]:
    """create a list of int from nucleotide sequence.

    Args:
        seq (str): sequence using A, T(U), G, C

    Returns:
        List[int]: list of sequence converted into int
    """
    return [int(Nucleotide[char]) for char in seq]


def one_hot_encode(seq: str, padding: Union[int, Tuple[int, int]] = 0) -> np.array:
    """create one_hot encodes sequence from sequence string.

    Args:
        seq (str): sequence created using A, T(U), G, C.
        padding (Union[int, Tuple[int, int]], optional): length of the padding sequence.
        If tuple of int is provided, the first number used to pad the start,
        and the other used to pad the end. Defaults to 0.

    Returns:
        np.array: array of sequence. The first dim refers to the sequence length,
        and the second dim refers to the nucleotide index.
    """
    # inside array, index 0 to 3 is one_hot and index 4 is all 0.25
    arr = np.vstack((np.eye(4), np.ones(4)[None, :] * 0.25))

    # split padding into left and right
    if isinstance(padding, int):
        paddings = (padding, padding)
    else:
        paddings = padding
    left_pad, right_pad = paddings

    # return one hot array
    return arr[one_hot_index("N" * left_pad + seq + "N" * right_pad)]


def read_fasta(path) -> List[str]:
    pass
