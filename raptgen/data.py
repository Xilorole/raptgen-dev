from enum import IntEnum
from typing import List

class State(IntEnum):
    """Enum for Profile HMM. M stands for Match, I stands for insertion and D stands for deletion."""

    M = 0
    Match = 0
    I = 1
    Insertion = 1
    D = 2
    Deletion = 2


class Transition(IntEnum):
    """Enum for State-to-State transition."""

    M2M = 0
    Match_to_Match = 0
    M2I = 1
    Match_to_Insertion = 1
    M2D = 2
    Match_to_Deletion = 2
    I2M = 3
    Insertion_to_Match = 3
    I2I = 4
    Insertion_to_Insertion = 4
    D2M = 5
    Deletion_to_Match = 5
    D2D = 6
    Deletion_to_Deletion = 6


class Nucleotide(IntEnum):
    """Enum for nucleotide."""

    A = 0
    T = 1
    U = 1
    G = 2
    C = 3
    PAD = 4
    SOS = 5
    EOS = 6


def one_hot_index(seq: str) -> List[int]:
    """create a list of int from nucleotide sequence.

    Args:
        seq (str): sequence using A, T(U), G, C

    Returns:
        List[int]: list of sequence converted into int
    """
    return [int(Nucleotide[char]) for char in seq]