import numpy as np

def make_checkerboard(board_size: tuple[int, int], square_size: tuple[int, int]) -> np.ndarray:
    """
    Create a checkerboard pattern.

    Props to stackoverflow user Blubberguy22, posted March 17, 2020 at 19:00
    https://stackoverflow.com/questions/2169478/how-to-make-a-checkerboard-in-numpy

    Parameters:
        board_size (tuple[int, int]): Size of the board in rows and columns.
        square_size (tuple[int, int]): Size of each square in rows and columns.

    Returns:
        np.ndarray: Checkerboard pattern as a NumPy array.
    """
    rows, cols = board_size
    sq_rows, sq_cols = square_size

    # Calculate the checkerboard pattern efficiently
    row_indices = np.arange(rows) // sq_rows
    col_indices = np.arange(cols) // sq_cols
    checkerboard = (row_indices[:, np.newaxis] + col_indices) % 2

    return checkerboard.astype('float32')