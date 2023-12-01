from src.position import Position


class State:
    def move_forward(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def get_position(self):
        pass


class NorthState(State):
    def __init__(self, cartesian):
        self.cartesian = cartesian

    def move_forward(self):
        return NorthState((self.cartesian[0], self.cartesian[1] + 1))

    def turn_left(self):
        return WestState(self.cartesian)

    def turn_right(self):
        return EastState(self.cartesian)

    def get_position(self):
        return Position(self.cartesian, 'N')


class EastState(State):
    def __init__(self, cartesian):
        self.cartesian = cartesian

    def move_forward(self):
        return EastState((self.cartesian[0] + 1, self.cartesian[1]))

    def turn_left(self):
        return NorthState(self.cartesian)

    def turn_right(self):
        return SouthState(self.cartesian)

    def get_position(self):
        return Position(self.cartesian, 'E')


class SouthState(State):
    def __init__(self, cartesian):
        self.cartesian = cartesian

    def move_forward(self):
        return SouthState((self.cartesian[0], self.cartesian[1] - 1))

    def turn_left(self):
        return EastState(self.cartesian)

    def turn_right(self):
        return WestState(self.cartesian)

    def get_position(self):
        return Position(self.cartesian, 'S')


class WestState(State):
    def __init__(self, cartesian):
        self.cartesian = cartesian

    def move_forward(self):
        return WestState((self.cartesian[0] - 1, self.cartesian[1]))

    def turn_left(self):
        return SouthState(self.cartesian)

    def turn_right(self):
        return NorthState(self.cartesian)

    def get_position(self):
        return Position(self.cartesian, 'W')
