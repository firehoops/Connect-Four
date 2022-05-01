from src.model import Model
from pytest_mock import mocker
import pytest

model = Model()

def test_get_board() -> None:
    test_board = [[0] * 7 for r in range(6)]

    assert test_board == model.getBoard()


def test_check_row_valid() -> None:
    assert 0 == model.checkRow(1)


def test_check_row_invalid() -> None:
    model.board[0][1] = 1

    # Should move to row 1 since row 0 taken
    assert 1 == model.checkRow(1)


def test_make_to_many_moves() -> None:
    model.moveCount = 42

    assert model.makeMove(0) is False


def test_winner_exists_horizontal() -> None:
    model.board[0][0] = 1
    model.board[0][1] = 1
    model.board[0][2] = 1
    model.board[0][3] = 1

    assert model.winnerExists() is True

# Reset board
model.board = [[0] * 7 for r in range(6)]

def test_winner_exists_vertical() -> None:
    model.board[0][0] = 1
    model.board[1][0] = 1
    model.board[2][0] = 1
    model.board[3][0] = 1

    assert model.winnerExists() is True

model.board = [[0] * 7 for r in range(6)]

def test_winner_exists_diagonal() -> None:
    model.board[0][0] = 1
    model.board[1][1] = 1
    model.board[2][2] = 1
    model.board[3][3] = 1

    assert model.winnerExists() is True

model.board = [[0] * 7 for r in range(6)]

def test_winner_exists_diagonal() -> None:
    model.board[0][3] = 1
    model.board[1][2] = 1
    model.board[2][1] = 1
    model.board[3][0] = 1

    assert model.winnerExists() is True