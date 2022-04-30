import pytest
import unittest
import mocker
from unittest.mock import patch
from src.model import Model

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


def test_make_moves_winner() -> None:
    model.moveCount = 0
    mocker.patch("model.winnerExists", return_value=True)
    end = mocker.patch("model.endGame")

    assert model.makeMove(0) is False
    end.assert_called_once()