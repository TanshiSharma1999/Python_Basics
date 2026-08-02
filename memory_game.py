import turtle
import random
import time

# -------------------------
# Configuration / constants
# -------------------------
GRID_ROWS = 4
GRID_COLS = 4
CELL_SIZE = 100                 # pixel size of each cell
FONT_EMOJI = ("Arial", 36, "normal")
FONT_TEXT = ("Courier", 18, "normal")
HIDE_DELAY_MS = 900             # milliseconds to wait before hiding non-matching cards

# -------------------------
# Game state variables
# -------------------------
# 8 unique symbols duplicated to make 16 cards (4x4)
SYMBOLS = list("⭐🩷😀🦈👄🥎🌳📘")
SYMBOLS *= 2

board = []                      # actual symbols on the board (rows x cols)
visible_board = []              # what is currently shown to the player ("?" or symbol)
first_pick = None               # (row, col) of first selected card in a pair
attempts = 0
matches = 0
lock_input = False              # when True, ignore clicks (used while cards are being hidden)
start_time = None               # game start timestamp (for timer)

# -------------------------
# Turtle / screen setup
# -------------------------
screen = turtle.Screen()
screen.title("Memory Match Game")
screen.setup(width=600, height=700)   # extra vertical space for HUD
screen.tracer(0)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)

# -------------------------
# Utility / game functions
# -------------------------
def init_game():
    """Initialize or reset the game state and shuffle the board."""
    global board, visible_board, first_pick, attempts, matches, lock_input, start_time
    symbols = SYMBOLS[:]            # copy
    random.shuffle(symbols)
    # build 2D board
    board = [[symbols.pop() for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
    visible_board = [["?" for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
    first_pick = None
    attempts = 0
    matches = 0
    lock_input = False
    start_time = time.time()
    draw_grid()

def cell_top_left(row, col):
    """Return the (x, y) coordinates of the top-left corner of a cell."""
    total_w = GRID_COLS * CELL_SIZE
    total_h = GRID_ROWS * CELL_SIZE
    x0 = -total_w // 2
    y0 = total_h // 2
    x = x0 + col * CELL_SIZE
    y = y0 - row * CELL_SIZE
    return x, y

def draw_cell_background(row, col, color="white"):
    """Draw a filled rectangle behind a cell (used for reveal animation)."""
    x, y = cell_top_left(row, col)
    drawer.goto(x, y)
    drawer.fillcolor(color)
    drawer.pendown()
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(CELL_SIZE)
        drawer.right(90)
        drawer.forward(CELL_SIZE)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

def draw_grid():
    """Redraw the entire board and HUD (attempts, matches, timer)."""
    drawer.clear()
    # Draw cells
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x, y = cell_top_left(row, col)
            # draw border
            drawer.goto(x, y)
            drawer.pendown()
            drawer.pensize(2)
            drawer.pencolor("black")
            for _ in range(4):
                drawer.forward(CELL_SIZE)
                drawer.right(90)
            drawer.penup()
            # draw background (light color for revealed)
            if visible_board[row][col] != "?":
                draw_cell_background(row, col, color="#f7f7f7")
            # write symbol or placeholder centered in the cell
            cx = x + CELL_SIZE // 2
            cy = y - CELL_SIZE // 2 - 10  # small vertical tweak for visual centering
            drawer.goto(cx, cy)
            drawer.write(visible_board[row][col], align="center", font=FONT_EMOJI if visible_board[row][col] != "?" else FONT_TEXT)
    # Draw HUD below the grid
    hud_y = - (GRID_ROWS * CELL_SIZE) // 2 - 30
    drawer.goto(0, hud_y)
    elapsed = int(time.time() - start_time) if start_time else 0
    hud_text = f"Attempts: {attempts}    Matches: {matches}    Time: {elapsed}s    (Press 'r' to restart)"
    drawer.write(hud_text, align="center", font=FONT_TEXT)
    screen.update()

def get_cell_from_click(x, y):
    """Convert screen (x,y) to board (row,col). Return (None, None) if outside grid."""
    total_w = GRID_COLS * CELL_SIZE
    total_h = GRID_ROWS * CELL_SIZE
    x0 = -total_w // 2
    y0 = total_h // 2
    if x < x0 or x > x0 + total_w or y > y0 or y < y0 - total_h:
        return None, None
    col = int((x - x0) // CELL_SIZE)
    row = int((y0 - y) // CELL_SIZE)
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        return row, col
    return None, None

def is_game_won():
    """Return True if all cards are revealed (no '?' left)."""
    return all(cell != "?" for row in visible_board for cell in row)

# -------------------------
# Game interaction handlers
# -------------------------
def on_click(x, y):
    """Handle user clicks on the board."""
    global first_pick, attempts, matches, lock_input

    if lock_input:
        # ignore clicks while waiting to hide cards
        return

    row, col = get_cell_from_click(x, y)
    if row is None or col is None:
        return
    if visible_board[row][col] != "?":
        # already revealed or matched
        return

    # reveal the clicked card
    visible_board[row][col] = board[row][col]
    draw_grid()

    if first_pick is None:
        # store first pick and wait for second
        first_pick = (row, col)
    else:
        # second pick: compare with first
        r1, c1 = first_pick
        r2, c2 = row, col
        # increment attempts (one attempt = two picks)
        attempts += 1
        if board[r1][c1] == board[r2][c2]:
            # match found
            matches += 1
            first_pick = None
            draw_grid()
            # check win condition
            if is_game_won():
                on_win()
        else:
            # not a match: lock input and hide after a short delay
            lock_input = True
            # schedule hide_cards to run after HIDE_DELAY_MS
            screen.ontimer(lambda: hide_cards(r1, c1, r2, c2), HIDE_DELAY_MS)

def hide_cards(r1, c1, r2, c2):
    """Hide two non-matching cards and unlock input."""
    global first_pick, lock_input
    visible_board[r1][c1] = "?"
    visible_board[r2][c2] = "?"
    first_pick = None
    lock_input = False
    draw_grid()

def on_win():
    """Called when the player has matched all cards."""
    elapsed = int(time.time() - start_time) if start_time else 0
    drawer.goto(0, - (GRID_ROWS * CELL_SIZE) // 2 - 70)
    drawer.pencolor("green")
    drawer.write(f"🎉 You won in {attempts} attempts! Time: {elapsed}s", align="center", font=("Courier", 20, "bold"))
    drawer.pencolor("black")
    screen.update()

def restart_game():
    """Restart the game (bound to 'r' key)."""
    init_game()

# -------------------------
# Bindings and start
# -------------------------
screen.onclick(on_click)            # left-click handler
screen.listen()
screen.onkey(restart_game, "r")     # press 'r' to restart

# Initialize and run
init_game()
screen.mainloop()
