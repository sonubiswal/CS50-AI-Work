import tictactoe as ttt

# Create an empty board
board = ttt.initial_state()

# Play a few moves to test the AI
while not ttt.terminal(board):
    print("Current Board:")
    for row in board:
        print(row)
    
    # If it's X's turn (human), make a random move
    if ttt.player(board) == ttt.X:
        # Just take the first available action
        action = list(ttt.actions(board))[0]
        print(f"Human plays: {action}")
    else:
        # AI makes a move
        action = ttt.minimax(board)
        print(f"AI plays: {action}")
    
    board = ttt.result(board, action)

# Game Over
print("\nFinal Board:")
for row in board:
    print(row)
print(f"Winner: {ttt.winner(board)}")