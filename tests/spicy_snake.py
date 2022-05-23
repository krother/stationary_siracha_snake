
def move(current_position: tuple, direction: str) -> tuple:
    x, y = current_position
    if type(x) != int or type(y) != int:
        raise Exception("x and y have to be integers")
    if direction == 'right':
        new_position = x + 1, y
    elif direction == 'up':
        new_position = x, y + 1
    elif direction == 'down':
        new_position = x, y - 1
    else:
        new_position = x - 1, y
    return new_position
