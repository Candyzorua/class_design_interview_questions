from dataclasses import dataclass
from typing import List
import random

"""
In this interview question, we will implement a simplified version of Tetris.

########################
# Basic game mechanics #
########################
- On initialization, a new piece appears near the top center of the board. 
- On each tick, the game tries to move that piece down by 1 row.
 - If moving down is valid, it falls one step. 
 - If moving down would make it go out of bounds or overlap a locked cell, it locks onto the board.
   - After a piece locks, the game clears any full rows. The rows above shift downward, and the player’s score increases by the number of rows cleared. Then a new falling piece is spawned.

######################
# Player interaction #
######################

The player can control the falling piece in only 2 ways:

- move it left by 1
- move it right by 1

Any move is ignored if it would place part of the piece:

- out of bounds
- on top of a locked cell

############
# Game end #
############

The game ends when a new piece is spawned which overlaps a locked cell.
"""

############################################################################################################
# Implement the Board and TetrisController classes. You will need to add additional methods and attributes #
############################################################################################################


class Board:
    def __init__(self, rows: int, cols: int):
        """
        Initialize an empty board.

        Args:
            rows: Number of rows in the board.
            cols: Number of columns in the board.
        """
        pass


class TetrisController:
    def __init__(self, rows: int, cols: int):
        """
        Initialize a new Tetris game.

        Args:
            rows: Number of rows in the board.
            cols: Number of columns in the board.
        """
        pass

    def tick(self) -> None:
        pass

    def move_piece_sideways(self, dx: int) -> None:
        pass


#####################################################################
# These classes are provided to you. You do not need to modify them #
#####################################################################


@dataclass(frozen=True)
class Position:

    row: int
    col: int

    def translate(self, dr: int, dc: int) -> "Position":
        """Return a new position shifted by the given row and column offsets."""
        return Position(self.row + dr, self.col + dc)


class Piece:
    """Represents a Tetris piece using a square shape matrix and a display color."""

    DIMENSION = 4

    def __init__(self, shape: List[List[int]], color: str):
        """
        Initialize a piece.

        Args:
            shape: A matrix of 0/1 values where 1 means
                the piece occupies that cell.
            color: A string representing the piece color.
        """
        self.shape = shape
        self.color = color


class PieceFactory:
    """Creates randomized pieces with randomized colors."""

    PIECES = [
        [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [1, 1],
            [1, 1],
        ],
        [
            [1, 1, 1],
            [0, 1, 0],
            [0, 0, 0],
        ],
    ]

    COLORS = ["red", "blue", "green", "yellow"]

    @staticmethod
    def get_piece() -> Piece:
        """
        Return a random piece with a random color.

        The chosen shape is padded into a `Piece.DIMENSION x Piece.DIMENSION` matrix
        before constructing the piece.
        """
        shape = random.choice(PieceFactory.PIECES)
        color = random.choice(PieceFactory.COLORS)

        padded = [[0] * Piece.DIMENSION for _ in range(Piece.DIMENSION)]
        for r in range(len(shape)):
            for c in range(len(shape[r])):
                padded[r][c] = shape[r][c]

        return Piece(padded, color)
