import pytest
from mars_rover import Rover


# Feature: Moving the Mars Rover forward
# Scenario Outline: Moving forward changes position based on heading

@pytest.mark.parametrize("direction,expected_position", [
    ("North", (1, 2)),
    ("East",  (2, 1)),
    ("South", (1, 0)),
    ("West",  (0, 1)),
])
def test_move_forward(direction, expected_position):
    rover = Rover(x=1, y=1, heading=direction)
    rover.pass_command("F")
    assert rover.position == expected_position
