# Import Modules
import numpy as np

# Board Functions
EMPTY = 0
WP,WN,WB,WR,WQ,WK = 1,2,3,4,5,6
BP,BN,BB,BR,BQ,BK = -1,-2,-3,-4,-5,-6

def start_board_np() -> np.ndarray:
    b = np.zeros(64, dtype=np.int8) # -6~6은 int8로 충분

    b[0:8] = np.array([WR,WN,WB,WQ,WK,WB,WN,WR], dtype=np.int8)
    b[8:16] = WP
    b[48:56] = BP
    b[56:64] = np.array([BR,BN,BB,BQ,BK,BB,BN,BR], dtype=np.int8)

    return b

def as_8x8(board_1d: np.ndarray) -> np.ndarray:
    return board_1d.reshape(8,8)

def print_board(board_1d: np.ndarray) -> None:
    b2 = as_8x8(board_1d)
    print(np.flipud(b2))

FILES = "abcdefgh"
RANKS = "12345678"

def str_to_sq(s: str) -> int:
    f = FILES.index(s[0])
    r = RANKS.index(s[1])
    return r * 8 + f