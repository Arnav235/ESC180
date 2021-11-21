'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random

#prints board and legend
def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

#makes new board        
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def setup():
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return(board)
    #print_board_and_legend(board) 

#Problem 2 Part(a)
def get_free_squares(board):
    sq = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                sq.append([i,j])
    return sq

#Problem 1 Part (a)
def place(square_num):
    coord = []
    #finds row
    r = int((square_num - 1) // 3)
    c = int((square_num - 1) % 3)
    coord = [r,c]
    return coord

    #test code for place()
    #for i in range (1,10):
    #print("\n",i, place(i))

#Problem 1 Part (b)
def put_in_board(board, mark, square_num, turn_no):
    
    coord = place(square_num)
    while board[coord[0]][coord[1]] != " ":
        square_num = input("That spot already has a mark, choose another space: ")
        coord = place(int(square_num))

    board[coord[0]][coord[1]] = mark
    #board = put_in_board(board, "X", 1)
    #print_board_and_legend(board)

def ask(turn_no, board):
    loc = input("Which coordinate would you like?: ")
    print(loc)
    loc = int(float(loc))
    if turn_no % 2 != 0:
        put_in_board(board, "X", loc, turn_no)
    else:
        put_in_board(board, "O", loc, turn_no)

def check_win():
    return False

def play():
    board = setup()
    game_over = False
    turn_no = 1
    while not game_over:
        ask(turn_no, board)
        print_board_and_legend(board)
        turn_no += 1
        game_over = check_win()
        print("\n ", get_free_squares(board))

if __name__ == '__main__':
    play()