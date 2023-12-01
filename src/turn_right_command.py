from src.command import Command


class TurnRightCommand(Command):

    def __init__(self, state):
        self.state = state

    def execute(self):
        return self.state.turn_right()
