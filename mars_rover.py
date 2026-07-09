_BACKWARD = {
    "North": (0, -1),
    "East":  (-1, 0),
    "South": (0,  1),
    "West":  (1,  0),
}

_FORWARD = {
    "North": (0,  1),
    "East":  (1,  0),
    "South": (0, -1),
    "West":  (-1, 0),
}


class Rover:
    def __init__(self, x, y, heading):
        self.position = (x, y)
        self.heading = heading

    def pass_command(self, command):
        deltas = {"B": _BACKWARD, "F": _FORWARD}
        if command in deltas:
            dx, dy = deltas[command][self.heading]
            x, y = self.position
            self.position = (x + dx, y + dy)
