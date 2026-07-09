import pytest
from mars_rover import Rover


# Feature: Moving the Mars Rover backward
# Scenario Outline: Moving backward changes position opposite to heading

@pytest.mark.parametrize("direction,expected_position", [
    ("North", (1, 0)),
    ("East",  (0, 1)),
    ("South", (1, 2)),
    ("West",  (2, 1)),
])
def test_move_backward(direction, expected_position):
    rover = Rover(x=1, y=1, heading=direction)
    rover.pass_command("B")
    assert rover.position == expected_position
