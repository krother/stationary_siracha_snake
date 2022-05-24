
from spicy_snake.playground import Playground
import curses


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}

# prepare the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.curs_set(0)
curses.noecho()
curses.raw()
screen.keypad(False)

win = curses.newwin(40, 15, 0, 0)
win.nodelay(True)


def game_loop(screen):
    x, y = 5, 5

    pg = Playground(30, 14)

    # draw
    screen.clear()
    screen.addch(y, x, "O", curses.color_pair(1))
    for x in range(31):
        for y in range(15):
            if pg.is_obstacle((x, y)):
                screen.addch(y, x, "#", curses.color_pair(2))
    win.refresh()
    screen.refresh()

    while True:

        char = win.getch()
        direction = KEY_COMMANDS.get(char)
        if direction:
            dx, dy = direction
            x += dx
            y += dy

            # draw
            screen.clear()
            screen.addch(y, x, "O", curses.color_pair(1))
            win.refresh()
            screen.refresh()
            for x in range(31):
                for y in range(15):
                    if pg.is_obstacle((x, y)):
                        screen.addch(y, x, "#", curses.color_pair(2))




if __name__ == "__main__":

    curses.wrapper(game_loop)
    curses.endwin()
