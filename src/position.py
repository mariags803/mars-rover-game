class Position:
    def __init__(self, cartesian, direction):
        self.cartesian = cartesian
        self.direction = direction

    def __eq__(self, other):
        return self.cartesian == other.cartesian and self.direction == other.direction

    def __str__(self):
        return f'({self.cartesian[0]}, {self.cartesian[1]}) {self.direction}'
