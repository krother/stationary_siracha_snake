
from spicy_snake.playground import Playground
import curses


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)  #FIXME: is this correct?
DOWN = (0, 1)

# ASCII codes of characters on the keyboard
KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}
#TODO: use arrow keys instead

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
    x, y = 5, 5  # player position

    pg = Playground(30, 14)  #FIXME: should this be initialized before?

    # draw
    #FIXME: redundant with paragraph below
    screen.clear()
    # draw the player:
    screen.addch(y, x, "O", curses.color_pair(1))
    # draw the playground:
    for pgx in range(31):
        for pgy in range(15):
            if pg.is_obstacle((pgx, pgy)):
                screen.addch(pgy, pgx, "#", curses.color_pair(2))
    win.refresh()
    screen.refresh()

    while True:

        # move the player
        char = win.getch() # returns the code of a pressed key
        direction = KEY_COMMANDS.get(char)  # direction is a tuple or None
        if direction:
            dx, dy = direction
            x += dx
            y += dy

            # draw
            screen.clear()  #FIXME: this removes the frame
            screen.addch(y, x, "O", curses.color_pair(1))
            #FIXME: move playground drawing code somewhere else
            for pgx in range(31):
                for pgy in range(15):
                    if pg.is_obstacle((pgx, pgy)):
                        screen.addch(pgy, pgx, "#", curses.color_pair(2))
            win.refresh()
            screen.refresh()




if __name__ == "__main__":

    curses.wrapper(game_loop)
    curses.endwin()
