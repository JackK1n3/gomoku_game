BOARD_SIZE = 15

def create_board():
    return [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    print("   " + " ".join(f"{i:2}" for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(f"{i:2} " + "  ".join(row))

def is_valid_move(board, x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == '.'

def check_winner(board, x, y, player):
    def count(dx, dy):
        count = 1
        for d in [1, -1]:
            i = 1
            while True:
                nx, ny = x + dx * i * d, y + dy * i * d
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx][ny] == player:
                    count += 1
                    i += 1
                else:
                    break
        return count

    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        if count(dx, dy) >= 5:
            return True
    return False

def play():
    board = create_board()
    current_player = 'X'
    print(" Welcome to Terminal Gomoku (Five in a Row)!")
    print("Player X goes first.\n")
    print_board(board)

    while True:
        try:
            coords = input(f"Player {current_player}, enter move (row col): ").split()
            if len(coords) != 2:
                raise ValueError
            x, y = map(int, coords)
            if not is_valid_move(board, x, y):
                print(" Invalid move. Try again.")
                continue

            board[x][y] = current_player
            print_board(board)

            if check_winner(board, x, y, current_player):
                print(f" Player {current_player} wins!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print(" Please enter valid coordinates like: 7 8")

if __name__ == "__main__":
    play()
