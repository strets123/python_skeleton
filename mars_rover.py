_BACKWARD = {
    "North": (0, -1),
    "East":  (-1, 0),
    "South": (0,  1),
    "West":  (1,  0),
}


class Rover:
    def __init__(self, x, y, heading):
        self.position = (x, y)
        self.heading = heading

    def pass_command(self, command):
        if command == "B":
            dx, dy = _BACKWARD[self.heading]
            x, y = self.position
            self.position = (x + dx, y + dy)
