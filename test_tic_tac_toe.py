def initialise_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("-----------")
    for row in board:
        print("|","| ".join(row),"|")
        print("------------")


def take_user_input(board,player):
    while True:
        row,col = map(int,input("Enter the row and column for player O between 0 and 2").split())
        if 0<=row<=2 and 0<=col<=2 and board[row][col] == ' ':
            board[row][col] = player
            break
        print("Please enter the valid or unoccupied position")

def is_winner(board,player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(board,is_ai):
    if is_winner(board,'X'):
        return 1
    if is_winner(board,'O'):
        return -1
    if is_draw(board):
        return 0

    best_score = float("-inf") if is_ai else float("inf")

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X' if is_ai else 'O'
                score = minimax(board,not is_ai)
                board[i][j] = ' '
                best_score = max(best_score,score) if is_ai else min(best_score,score)
    return best_score

def place_ai(board,player):
    best_score,best_pos = float("-inf"), None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                score = minimax(board,False)
                board[i][j] = ' '
                if score > best_score:
                    best_score,best_pos = score,(i,j)

    return best_pos

def main():

    board = initialise_board()
    print_board(board)

    while True:
        take_user_input(board,'O')
        print_board(board)

        if is_winner(board,'O'):
            print("User wins against AI")
            break

        if is_draw(board):
            print("The match has ended with the draw ")
            break

        #ai turn
        position = place_ai(board,'X')
        if position :
            board[position[0]][position[1]] = 'X'
        print_board(board)
        if is_winner(board,'X'):
            print("User wins against AI")
            break

        if is_draw(board):
            print("The match has ended with the draw ")
            break

if __name__ == "__main__":
    main()