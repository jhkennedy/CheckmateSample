import pytest
import numpy as np
from generator import make_checkerboard

def test_checkerboard_shape():
    board_size = (8, 8)
    square_size = (1, 1)
    checkerboard = make_checkerboard(board_size, square_size)
    assert checkerboard.shape == board_size

def test_checkerboard_values():
    board_size = (4, 4)
    square_size = (1, 1)
    checkerboard = make_checkerboard(board_size, square_size)
    expected = np.array([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ], dtype='float32')
    np.testing.assert_array_equal(checkerboard, expected)

def test_checkerboard_larger_squares():
    board_size = (6, 6)
    square_size = (2, 2)
    checkerboard = make_checkerboard(board_size, square_size)
    expected = np.array([
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0]
    ], dtype='float32')
    np.testing.assert_array_equal(checkerboard, expected)

def test_checkerboard_rectangular():
    board_size = (6, 4)
    square_size = (2, 1)
    checkerboard = make_checkerboard(board_size, square_size)
    expected = np.array([
        [0, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 1, 0, 1]
    ], dtype='float32')
    np.testing.assert_array_equal(checkerboard, expected)

def test_checkerboard_dtype():
    board_size = (4, 4)
    square_size = (1, 1)
    checkerboard = make_checkerboard(board_size, square_size)
    assert checkerboard.dtype == np.float32

@pytest.mark.parametrize("board_size,square_size", [
    ((0, 0), (1, 1)),
    ((5, 5), (0, 0)),
    ((-1, 5), (1, 1)),
    ((5, 5), (-1, 1))
])
def test_invalid_inputs(board_size, square_size):
    with pytest.raises((ValueError, ZeroDivisionError)):
        make_checkerboard(board_size, square_size)