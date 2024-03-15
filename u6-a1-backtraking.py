# Author: Jesus Emiliano Reyes Gomez
# Id: 4668974
# Maestria Big Data, UAG
# Date: 21/02/2024
# Description: Backtraking Sudoku


def print_board(board): #Funcion para imprimir el tablero
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def find_empty(board): #Funcion para encontrar un espacio vacio
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):  
    #Validamos si el numero ya esta en la fila
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Validamos si el numero ya esta en la columna
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #Validamos si en el grupo de 3x3 ya esta el numero
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        #No hay espacios vacios, el tablero esta resuelto
        return True
    else:
        row, col = find #Obtenemos la posicion del espacio vacio (fila, columna)
    for i in range(1, 10):
        #Validamos si el numero es valido en la posicion
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

board = [ [5, 0, 0, 9, 1, 3, 7, 2, 0], 
          [3, 0, 0, 0, 8, 0, 5, 0, 9], 
          [0, 9, 0, 2, 5, 0, 0, 8, 0], 
          [6, 8, 0, 4, 7, 0, 2, 3, 0], 
          [0, 0, 9, 5, 0, 0, 4, 6, 0], 
          [7, 0, 4, 0, 0, 0, 0, 0, 5], 
          [0, 2, 0, 0, 0, 0, 0, 0, 0], 
          [4, 0, 0, 8, 9, 1, 6, 0, 0], 
          [8, 5, 0, 7, 2, 0, 0, 0, 3] ]

board2 = [[6, 9, 0, 0, 0, 0, 7, 0, 0], 
          [0, 0, 0, 0, 9, 6, 0, 0, 0], 
          [0, 8, 0, 7, 5, 3, 0, 9, 0], 
          [0, 2, 0, 3, 7, 4, 5, 6, 1], 
          [3, 6, 0, 0, 0, 5, 0, 2, 0], 
          [0, 0, 0, 9, 6, 0, 3, 7, 8], 
          [0, 0, 6, 0, 3, 1, 0, 8, 4], 
          [0, 4, 5, 8, 0, 7, 6, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 5, 7] ]

print_board(board)
solve(board)
print("_____________")
print_board(board)

print("Second board")
print_board(board2)

solve(board2)
print("______________")
print_board(board2)
