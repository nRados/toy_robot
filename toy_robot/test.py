import pytest
from robot import Robot

toy_robot = Robot(placed=False, x=None, y=None, facing=None)


@pytest.mark.parametrize(['x', 'y', 'f'], [(2, 8, 'NORTH'), (5, 1, 'EAST'), (0, 0, 'WEST')],)
def test_place(x, y, f):
    toy_robot.place(x, y, f)

    assert toy_robot.placed == False, "False"


def test_left():
    toy_robot = Robot(placed=True, x=3, y=3, facing='SOUTH')
    toy_robot.left()
    assert toy_robot.facing == 'EAST'


def test_right():
    toy_robot = Robot(placed=True, x=3, y=3, facing='WEST')
    toy_robot.right()
    assert toy_robot.facing == 'NORTH'


def test_move():
    toy_robot = Robot(placed=True, x=4, y=4, facing='EAST')
    toy_robot.move()

    assert toy_robot.x < 5, " x coordinate < 5"
    assert toy_robot.y < 5, "y coordinate < 5"
    print ("Your robot is moving")
