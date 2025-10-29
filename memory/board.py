import random
from .simbols import *
def init_game(size: int, moves: int):
    return {
        "symbols": creat_matrix(size, "x"),    
        "revealed": creat_matrix(size, False),   
        "size": size,                   
        "moves": moves,                   
        "matches": 0 
    }

def check_matrix_size_pair(size : int):
    return size % 2 == 0


def creat_matrix(size: int, value):
    while True:
        if check_matrix_size_pair(size):
            matrix = []
            for row in range(size):
                vector = []
                for col in range(size):
                    vector.append(value)
                matrix.append(vector)
            return matrix
        else:
            print("The size of the matrix need to be even")
            size = int(input("Please enter valid matrix size "))


def get_random_cordinates(state: dict):
    x = random.randint(0, state["size"] -1)
    y = random.randint(0, state["size"] -1)
    return x, y


def insert_shuffel(state: dict):
    simbols_arr  = generate_symbols(state["size"])
    while len(simbols_arr) > 0:
        x, y = get_random_cordinates(state)
        if state["revealed"][x][y] == False:
            state["revealed"][x][y] = simbols_arr.pop()
        else:
            x, y = get_random_cordinates(state)

    return state["revealed"]

print(insert_shuffel(init_game(6, 15)))





















# import random
# def create_board(size: int, symbols: list[str],*, rng: random.Random | None = None):
#     return dict
# def reval_tile(board: dict, x: int, y: int):
#     return str | None

# def hide_tiles(board: dict, coords: list[tuple[int,int]]):
#     return None

# def render_board(board: dict, reveal_all: bool = False):
#     return str