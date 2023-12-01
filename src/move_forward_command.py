from src.command import Command


class MoveForwardCommand(Command):

    def __init__(self, state):
        self.state = state

    def execute(self):
        return self.state.move_forward()
