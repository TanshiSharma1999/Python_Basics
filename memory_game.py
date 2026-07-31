import turtle
import random

# Game setup

pairs="⭐🩷😀🦈👄🥎🌳📘"
pairs = list(pairs)  # Card symbols
pairs *= 2  # Duplicate symbols for pairs
random.shuffle(pairs)  # Shuffle the cards

# Constants
GRID_ROWS = 4
GRID_COLS = 4
CELL_SIZE = 100  # Size of each grid cell

# Initialize the board
board = [[pairs.pop() for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
visible_board = [["?" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates for smoother drawing

# Turtle setup
drawer = turtle.Turtle()
drawer.penup()
drawer.hideturtle()

# Draw the grid on the screen
def draw_grid():
    drawer.clear()
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = col * CELL_SIZE - (GRID_COLS * CELL_SIZE) // 2
            y = (GRID_ROWS * CELL_SIZE) // 2 - row * CELL_SIZE
            drawer.goto(x + CELL_SIZE // 2, y - CELL_SIZE // 2)
            drawer.write(visible_board[row][col], align="center", font=("Courier", 28, "normal") )
            drawer.goto(x, y)
            drawer.pendown()
            for _ in range(4):  # Draw a square
                drawer.forward(CELL_SIZE)
                drawer.right(90)
            drawer.penup()
    screen.update()

# Get the row and column from screen coordinates
def get_cell_from_click(x, y):
    col = int((x + (GRID_COLS * CELL_SIZE) // 2) // CELL_SIZE)
    row = int(((GRID_ROWS * CELL_SIZE) // 2 - y) // CELL_SIZE)
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        return row, col
    return None, None

# Check if all cards are matched
def is_game_won():
    return all(cell != "?" for row in visible_board for cell in row)

# Main game logic
first_pick = None
attempts = 0

def on_click(x, y):
    global first_pick, attempts

    row, col = get_cell_from_click(x, y)
    if row is None or col is None or visible_board[row][col] != "?":
        return  # Invalid click or already revealed cell

    # Reveal the selected card
    visible_board[row][col] = board[row][col]
    draw_grid()

    if first_pick is None:
        # First card picked
        first_pick = (row, col)
    else:
        # Second card picked
        r1, c1 = first_pick
        if board[r1][c1] == board[row][col]:
            # Match found
            print("Match found!")
        else:
            # No match, flip back
            screen.ontimer(lambda: hide_cards(r1, c1, row, col), 1000)
        first_pick = None
        attempts += 1

    if is_game_won():
        drawer.goto(0, -GRID_ROWS * CELL_SIZE // 2 - 40)
        drawer.write("You won in {} attempts!".format(attempts), align="center", ffont=("Courier", 28, "normal"))
        screen.update()

def hide_cards(r1, c1, r2, c2):
    visible_board[r1][c1] = "?"
    visible_board[r2][c2] = "?"
    draw_grid()

# Bind click events
screen.onclick(on_click)

# Initial draw
draw_grid()

# Start the game loop
screen.mainloop()
