"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""
import copy

def is_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != " ":
                return False
    return True
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    x_start = x_end + (length-1) *-1*d_x
    y_start = y_end + (length-1) *-1*d_y
    x_last = x_start + -1*d_x
    y_last = y_start + -1*d_y
    x_next = x_end + d_x
    y_next = y_end + d_y
    #OPEN
    if x_last != -1 and y_last != -1:
        if board[y_last][x_last] == " ":
            if y_next != len(board) and x_next != len(board[0]):
                if board[y_next][x_next] == " ":
                    return "OPEN"
    
    # CLOSED
    if (x_last == -1 or y_last == -1) or board[y_last][x_last] != " ":
        if (x_next == len(board[0]) or y_next== len(board)) or board[y_next][x_next] != " ":
            return "CLOSED"

    #SEMI-OPEN
    return "SEMIOPEN"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    row_start_open = False
    counting = False
    count = 0
    while True:
        if board[y_start][x_start] == " ":
            if counting:
                if count == length:
                    if row_start_open:
                        open_seq_count += 1
                    else:
                        semi_open_seq_count += 1
                counting = False
            row_start_open = True
        elif board[y_start][x_start] == col:
            if counting:
                count += 1
            else:
                counting = True
                count = 1
        else:
            if counting:
                if count == length:
                    if row_start_open:
                        semi_open_seq_count += 1
                counting = False
            row_start_open = False

        y_start += d_y
        x_start += d_x
        if y_start > len(board) -1 or x_start > len(board[0]) -1 or x_start < 0:
            if counting and count == length:
                if row_start_open:
                    semi_open_seq_count += 1
            break

    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    # left edge
    for i in range(len(board)):
        open_seq, semi_open_seq = detect_row(board, col, i, 0, length, 0, 1)    
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

        # diagonal going downwards left to right
        if i < len(board) -1:
            open_seq, semi_open_seq = detect_row(board, col, i, 0, length, 1, 1) 
            open_seq_count += open_seq
            semi_open_seq_count += semi_open_seq
    
    # top edge
    for i in range(len(board[0])):
        open_seq, semi_open_seq = detect_row(board, col, 0, i, length, 1, 0)    
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

        # diagonal going downwards left to right and those going right to left
        if i < len(board) -1 and i > 0:
            # downwards left to right
            open_seq, semi_open_seq = detect_row(board, col, 0, i, length, 1, 1) 
            open_seq_count += open_seq
            semi_open_seq_count += semi_open_seq
            # downwards right to left
            open_seq, semi_open_seq = detect_row(board, col, 0, i, length, 1, -1) 
            open_seq_count += open_seq
            semi_open_seq_count += semi_open_seq
    # right edge only with diagonal from right to left
    for i in range(len(board) -1):
        open_seq, semi_open_seq = detect_row(board, col, i, 7, length, 1, -1) 
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    max_score = float("-inf")
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                copy_board = copy.deepcopy(board)
                copy_board[i][j] = "b"
                cur_score = score(copy_board)
                if cur_score > max_score:
                    max_score =  cur_score
                    move_y = i
                    move_x = j

    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

# the function checks if the board is full    
def check_if_board_full(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                return False
    return True

# function checks whether at the position (y, x) and going in the direction (d_y, d_x)
# the color 'col' makes a 5 in a row
def check_5_row(board, col, y, x, d_y, d_x):
    # checking if the piece before the starting piece is the same colour
    if y-d_y > -1 and x-d_x > -1 and x-d_x < len(board):
        if board[y-d_y][x-d_x] == col:
            return False
    for i in range(4):
        y += d_y
        x += d_x
        if y > len(board)-1 or x > len(board[0]) -1: return False
        if board[y][x] != col: return False
    if ( y + d_y < len(board) and x + d_x < len(board[0]) ) and board[y + d_y][x + d_x] == col: return False
    return True

def is_win(board):
    # checking for draw
    if check_if_board_full(board): return "Draw"

    for col in ["w", "b"]:
        win = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == col:
                    
                    # checking for vertical win
                    if i < len(board) -4:
                        if check_5_row(board, col, i, j, 1, 0): win = True

                    # checking for horozontal and diagonal left to right wins
                    if j < len(board) - 4:
                        if check_5_row(board, col, i, j, 0, 1): win = True
                        if check_5_row(board, col, i, j, 1, 1): win = True
                    
                    # checking for diagonal right to left win
                    if j > 3:
                        if check_5_row(board, col, i, j, 1, -1): win = True
        if win:
            if col == "w": return "White won"
            if col == "b": return "Black won"
       
    return "Continue playing"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board = [[' ', 'w', ' ', 'b', 'w', ' ', ' ', 'b'], ['w', 'b', ' ', ' ', ' ', 'b', 'b', 'b'], ['w', 'w', 'b', ' ', 'b', 'w', 'w', 'w'], ['w', 'w', ' ', 'b', ' ', ' ', ' ', 'w'], ['w', 'w', 'b', 'b', ' ', ' ', ' ', ' '], ['b', 'w', 'b', 'b', 'b', ' ', ' ', ' '], ['b', 'w', 'w', ' ', ' ', 'b', ' ', 'b'], [' ', 'w', 'w', 'w', 'w', 'w', 'w', 'b']]
    print(is_win(board))
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    play_gomoku(8)
    