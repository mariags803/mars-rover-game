import unittest
from src.rover import Rover


class MarsRover(unittest.TestCase):
    def test_should_move(self):
        rover = Rover()
        commands = 'MMRMMLMLM'
        rover.execute(commands)
        final_position = rover.get_position()
        self.assertEqual((1, 3), final_position.cartesian)
        self.assertEqual('W', final_position.direction)


if __name__ == '__main__':
    unittest.main()
