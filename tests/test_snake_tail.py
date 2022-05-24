
import pytest

@pytest.mark.skip
def test_snake():
    s = Snake(5, 6)
    assert s.head == (5, 6)
    s.forward()
    assert s.head == (6, 6)
    assert (6, 6) in s.tail
    s.grow()
    s.forward()
    assert s.head == (7, 6)
    assert (6, 6) in s.tail
    assert (7, 6) in s.tail


@pytest.mark.skip
def test_collision():
    p = Playground(10, 10)
    s = Snake(5, 5)
    for _ in range(3):
        s.forward()
        assert s.check_collision(p) is False
    s.forward()
    assert s.check_collision(p) is True


@pytest.mark.skip
def test_pickup_food():
    p = Playground(10, 10)
    s = Snake(5, 5)
    p.add_food((6, 5))
    # head counts as part of the tail
    assert len(s.tail) == 1
    assert s.growing == 0

    # picking up food increases growing by 1
    s.forward()
    assert s.growing == 1

    # moving one more step makes the tail longer
    s.forward()
    assert s.growing == 0
    assert len(s.tail) == 2

@pytest.mark.skip
def test_tail_collision():
    """The snake hits its own tail"""
    p = Playground(10, 10)
    s = Snake(5, 5)
    
    # make the snake super long
    for _ in range(100):
        s.grow()

    # these are harmelse
    for d in ['right', 'up', 'left']:
        s.set_direction(d)
        s.forward()
        assert s.check_collision(p) is False

    # now comes the move where the snake hits itself
    s.set_direction('down')
    s.foward()
    assert s.check_collision(p) is True
