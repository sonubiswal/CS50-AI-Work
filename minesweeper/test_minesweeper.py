import minesweeper as ms

# Create a small 3x3 AI
ai = ms.MinesweeperAI(height=3, width=3)

# Simulate a move
ai.add_knowledge((0, 0), 0)
print("Safes after (0,0)=0:", ai.safes)
print("Mines after (0,0)=0:", ai.mines)

ai.add_knowledge((2, 2), 2)
print("Safes after (2,2)=2:", ai.safes)
print("Mines after (2,2)=2:", ai.mines)

print("Safe move:", ai.make_safe_move())
print("Random move:", ai.make_random_move())