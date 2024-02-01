import os

def get_curr_player(board):
    return "X" if (len(board) - len(get_valid_moves(board))) % 2 == 0 else "O"


def get_valid_moves(board):
    moves = []
    for i, move in enumerate(board):
        if move == " ":
            moves.append(i)
    return moves


def board_is_full(board):
    for value in board:
        if value == " ":
            break
    else:
        return True
    return False


def minmax(board, depth, alpha, beta, isMaximaxing):
    if state(board) != None:
        return state(board)

    if isMaximaxing:
        score = -float("inf")
        moves = get_valid_moves(board)
        for move in moves:
            copyboard = board.copy()
            copyboard[move] = "X"
            score = max(score, minmax(copyboard, depth + 1, alpha, beta, False))
            alpha = max(score, alpha)
            if alpha >= beta:
                break
            copyboard[move] = " "
        return score
    else:
        score = float("inf")
        moves = get_valid_moves(board)
        for move in moves:
            copyboard = board.copy()
            copyboard[move] = "O"
            score = min(score, minmax(copyboard, depth + 1, alpha, beta, True))
            beta = min(score, beta)
            if alpha >= beta:
                break
            copyboard[move] = " "
        return score


def get_best_move(board, turn):
    moves = get_valid_moves(board)
    bestMove = 22
    if turn == "O":
        bestScore = float("inf")
        for move in moves:
            copyboard = board.copy()
            copyboard[move] = "O"
            score = minmax(copyboard, 0, -float("inf"), float("inf"), True)
            if int(score) < bestScore:
                bestScore = score
                bestMove = move
    else:
        bestScore = -float("inf")
        for move in moves:
            copyboard = board.copy()
            copyboard[move] = "X"
            score = minmax(copyboard, 0, -float("inf"), float("inf"), False)
            if int(score) > bestScore:
                bestScore = score
                bestMove = move

    return bestMove


def print_board(board):
    print(f" {board[0] if board[0] !=' ' else 0} ┃ {board[1] if board[1] !=' ' else 8} ┃ {board[2] if board[2] !=' ' else 2}")
    print(f"━━━╋━━━╋━━━")
    print(f" {board[3] if board[3] !=' ' else 3} ┃ {board[4] if board[4] !=' ' else 4} ┃ {board[5] if board[5] !=' ' else 5}")
    print(f"━━━╋━━━╋━━━")
    print(f" {board[6] if board[6] !=' ' else 6} ┃ {board[7] if board[7] !=' ' else 7} ┃ {board[8] if board[8] !=' ' else 8}")


def state(board):
    if get_curr_player(board) == "O":
        if (board[0] == board[1] == board[2]) and (board[0] != " "):
            return 1
        elif board[3] == board[4] == board[5] and (board[4] != " "):
            return 1
        elif board[6] == board[7] == board[8] and (board[7] != " "):
            return 1
        elif board[0] == board[3] == board[6] and (board[0] != " "):
            return 1
        elif board[1] == board[4] == board[7] and (board[4] != " "):
            return 1
        elif board[2] == board[5] == board[8] and (board[5] != " "):
            return 1
        elif board[0] == board[4] == board[8] and (board[0] != " "):
            return 1
        elif board[2] == board[4] == board[6] and (board[2] != " "):
            return 1
        elif board_is_full(board):
            return 0

    else:
        if (board[0] == board[1] == board[2]) and (board[0] != " "):
            return -1
        elif board[3] == board[4] == board[5] and (board[4] != " "):
            return -1
        elif board[6] == board[7] == board[8] and (board[7] != " "):
            return -1
        elif board[0] == board[3] == board[6] and (board[0] != " "):
            return -1
        elif board[1] == board[4] == board[7] and (board[4] != " "):
            return -1
        elif board[2] == board[5] == board[8] and (board[5] != " "):
            return -1
        elif board[0] == board[4] == board[8] and (board[0] != " "):
            return -1

        elif board[2] == board[4] == board[6] and (board[2] != " "):
            return -1

        elif board_is_full(board):
            return 0
    return None



def main():
    board = [" " for _ in range(9)]
    validMove = get_valid_moves(board)
    player1 = input("what do u wnat to play").upper()

    cpu = "O" if player1 == "X" else "X"
    turn = "X"

    while True:
        os.system('clear')
        print_board(board)
        validMove = get_valid_moves(board)

        if turn == player1:
            pos = int(input("player1 move:"))
            if pos in validMove:
                board[pos] = player1
            else:
                print("Invalid Move")
                continue
        else:
            print("cpu moved")
            pos = get_best_move(board, turn)
            board[pos] = cpu
        turn = get_curr_player(board)

        match state(board):
            case 1:
                print_board(board)
                print(" X has won the game")
                break
            case -1:
                print_board(board)
                print("O has won the game")
                break
            case 0:
                print_board(board)
                print("its a draw ")
                break


if __name__ == "__main__":
    main()

