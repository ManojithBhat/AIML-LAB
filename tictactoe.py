def initialise_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print('-----------')
    for row in board:
        print("|", " | ".join(row),"|")
        print("-------------")


def get_user_input(board):
    while True:
        row,col = map(int,input("Enter the row and column for O ( between 0 and 2)").split())
        if 0<=row <=2 and 0<=col<=2 and board[row][col] == ' ':
            board[row][col] = 'O'
            break
        else : print("Enter valid intput or unoccupied position")


def is_winner(board,player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(board,ai_turn):
    if is_winner(board,'X'):
        return 1
    if is_winner(board,'O'):
        return -1
    if is_draw(board):
        return 0
    
    best_score = float("-inf") if ai_turn else float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X' if ai_turn else 'O'
                score = minimax(board,not ai_turn)
                board[i][j] = ' '
                best_score = max(score,best_score) if ai_turn else min(score,best_score)
    return best_score


def find_best_turn(board):
    best_score,best_move = float("-inf"), None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board,False)
                board[i][j] = ' '
                if best_score < score:
                    best_score , best_move = score, (i,j)
    return best_move

def main():
    board = initialise_board()
    print_board(board)

    while True:
        #get user input
        get_user_input(board)
        if is_winner(board,'O'):
            print("User Wins the game !")
            break
        if is_draw(board):
            print("Game draws !")
            break

        ai_turn = find_best_turn(board)
        if ai_turn:
            board[ai_turn[0]][ai_turn[1]] = 'X'
        print_board(board)
        if is_winner(board,'X'):
            print("AI Wins the game !")
            break
        if is_draw(board):
            print("Game draws !")
            break


if __name__ == "__main__":
    main()