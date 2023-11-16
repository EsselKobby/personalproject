blank_board = """
  1   2   3
1   |   |  
 --- --- ---
2   |   | 
 --- --- ---
3   |   |  
"""

name = input("What is your name? ")
print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")
print(blank_board)

player = "X"
# tic-tac-toe positions
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
while True:
    print("It is " + player + "'s turn")
    position = input("Enter a position (i.e., 1,1): ")
    # Check the position is valid
    valid = position[0].isnumeric() and position[1] == "," and position[2].isnumeric()

    if valid:
        row = int(position[0])
        col = int(position[2])
    else:
        print("invalid position")
        exit(0)

    # Update the correct variable based on the position entered
    if row == 1:
        if col == 1:
            a = player
        elif col == 2:
            b = player
        elif col == 3:
            c = player
    elif row == 2:
        if col == 1:
            d = player
        elif col == 2:
            e = player
        elif col == 3:
            f = player
    elif row == 3:
        if col == 1:
            g = player
        elif col == 2:
            h = player
        elif col == 3:
            i = player

    board = f"""
    1   2   3
  1 {a} | {b} | {c}
   --- --- ---
  2 {d} | {e} | {f}
   --- --- ---
  3 {g} | {h} | {i}
  """

    print(board)

    if player == "X":
        player = "O"
    else:
        player = "X"
