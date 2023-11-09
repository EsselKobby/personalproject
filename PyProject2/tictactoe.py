# this is a multiline string; it starts with three quotes
blank_board = """
  1   2   3
1   |   |  
--- --- ---
2   |   |  
--- --- ---
3   |   |  
"""

# start your code here
userName = input("What is your name?")
print("Welcome to Tic Tac Toe, " + userName + ". Here is your playing board: ")
print(blank_board)
print("Let's play!")
print(blank_board)
userPosition = input("Enter a position (i.e., 1,1): ")
print(userPosition)

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
position = input("Enter a position (i.e., 1,1): ")
print(position)

# TODO: Check the position is valid
# [your code here]
valid = position[0].isnumeric() and position[1] == "," and position[2].isnumeric()

if valid:
    row = int(position[0])
    col = int(position[2])
    print(row, col)

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

# TODO: Update the correct variable based on the position entered
# [your code here]
if row == 1:
    if col == 1:
        a = "X"
    elif col == 2:
        b = "X"
    elif col == 3:
        c = "X"
    elif row == 2:
        if col == 1:
            d = "X"
        elif col == 2:
            e = "X"
        elif col == 3:
            f = "X"
        elif row == 3:
            if col == 1:
                g = "X"
        elif col == 2:
            h = "X"
        elif col == 3:
            i = "X"
else:
    print("Invalid position")
    exit()
# print the updated board
board = f"""
  1   2   3
1 {a} | {b} | {c}
 --- --- ---
2 {d} | {e} | {f}
 --- --- ---
3 {g} | {h} | {i}
"""
print(board)
