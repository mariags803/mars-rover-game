from src.move_forward_command import MoveForwardCommand
from src.state import NorthState
from src.turn_left_command import TurnLeftCommand
from src.turn_right_command import TurnRightCommand


class Rover:
    def __init__(self):
        self.state = NorthState((0, 0))

    def execute(self, commands):
        for command in commands:
            if command == 'M':
                self.state = MoveForwardCommand(self.state).execute()
            elif command == 'L':
                self.state = TurnLeftCommand(self.state).execute()
            elif command == 'R':
                self.state = TurnRightCommand(self.state).execute()

    def get_position(self):
        return self.state.get_position()
