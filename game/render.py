"""Frame rendering: build a character grid, write it to the terminal."""
from game.config import WIDTH, HEIGHT

HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"
CURSOR_HOME = "\x1b[H"

def new_grid():
    """A HEIGHT x WIDTH grid of spaces."""
    grid = []
    for _ in range(HEIGHT):
        row = []
        for _ in range(WIDTH):
            row.append(" ")
        grid.append(row)
    return grid

def put_text(grid, x, y, text):
    """Write text into the grid; out-of-bounds characters are dropped."""
    for i in range(len(text)):
        gx = x + i
        if 0 <= gx < WIDTH and 0 <= y < HEIGHT:
            grid[y][gx] = text[i]

def draw_border(grid):
    for x in range(WIDTH):
        grid[0][x] = "-"
        grid[HEIGHT - 1][x] = "-"
    for y in range(HEIGHT):
        grid[y][0] = "|"
        grid[y][WIDTH - 1] = "|"
    grid[0][0] = "+"
    grid[0][WIDTH - 1] = "+"
    grid[HEIGHT - 1][0] = "+"
    grid[HEIGHT - 1][WIDTH - 1] = "+"

def grid_to_text(grid):
    """Join the rows into one string, no trailing newline."""
    lines = []
    for row in grid:
        lines.append("".join(row))
    return "\n".join(lines)

if __name__ == "__main__":
    g = new_grid()
    draw_border(g)
    put_text(g, 2, 2, "SPACE INVADERS")
    put_text(g, 2, 4, "state: menu")
    print(grid_to_text(g))