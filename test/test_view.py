import pytest
import unittest
from unittest.mock import patch
from src.view import View

view = View()

@patch('builtins.input', return_value="text")
def test_get_user_input() -> None:
    userInput = "text"

    assert userInput == view.getUserInput("Type text or gui for your version of Connect Four\n")
