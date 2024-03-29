import os


TURNS = ['x', 'o']

board = [
    [str(elem + row) for elem in range(3)] 
    for row in range(1, 8, 3)
]

change_turn = True

while True:
    os.system("clear")
    if change_turn:
        TURNS.reverse()
        turn = TURNS[-1]

    prev_turn = "x" if turn == "o" else "o"

    # check horizontals
    h1 = all(board[0][t] == prev_turn for t in range(3))
    h2 = all(board[1][t] == prev_turn for t in range(3))
    h3 = all(board[2][t] == prev_turn for t in range(3))

    # check verticals
    v1 = all(board[t][0] == prev_turn for t in range(3))
    v2 = all(board[t][1] == prev_turn for t in range(3))
    v3 = all(board[t][2] == prev_turn for t in range(3))

    # check diagonals
    d1 = all(board[t][t] == prev_turn for t in range(3))
    d2 = all(board[t][2-t] == prev_turn for t in range(3))

    # check win
    if (h1 or h2 or h3) or (v1 or v2 or v3) or (d1 or d2):
        for row in board:
            print("|".join(row))
        exit(f"Congratulations! '{prev_turn}' wins!")

    for row in board:
        print("|".join(row))
    print(f"\nWhere to put '{turn}'?")

    pos = input(">> ")
    if pos == "exit":
        exit()
    elif pos.isdigit():
        pos = int(pos)
    else:
        input("Wrong input.")
        change_turn = False
        continue

    if pos in (1, 2, 3):
        pos -= 1
        row = 0
    elif pos in (4, 5, 6):
        pos -= 4
        row = 1
    elif pos in (7, 8, 9):
        pos -= 7
        row = 2
    else:
        input("Invalid number.")
        change_turn = False
        continue

    value = board[row][pos]
    if value in TURNS:
        input("This cell is already being taken")
        change_turn = False
        continue
    else:
        board[row][pos] = turn
        change_turn = True