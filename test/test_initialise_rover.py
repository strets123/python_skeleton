# Feature: Initialising the Mars Rover
# Scenario: Initialise rover at a given position and direction

def test_initialise_rover_position_and_heading():
    from mars_rover import Rover

    rover = Rover(x=2, y=3, heading="North")

    assert rover.position == (2, 3)
    assert rover.heading == "North"
