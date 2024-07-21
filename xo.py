from prettytable import PrettyTable

# Function to print the game board using PrettyTable
def print_board(board):
    table = PrettyTable()
    for row in board:
        table.add_row(row)
    table.header = False
    table.hrules = True
    print(table)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn.")

        # Get valid input from the player
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as 0, 1, or 2.")

        # Check for a win or draw
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
