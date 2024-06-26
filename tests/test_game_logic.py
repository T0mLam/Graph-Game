import numpy as np
import unittest

from graph_game.game.game_logic import GraphGame
from graph_game.game.score_generation import RandomScoreGenerator


class TestGraphGame(unittest.TestCase):
    def setUp(self):
        """Setup for graph"""
        self.game = GraphGame.random_start()
        self.game.set_base_score(100)
        self.game.set_starting_node(1)
        self.game.set_ending_node(4)
        self.game.score_generator = RandomScoreGenerator(self.game.base_score)  # Ensure a generator is set

    def test_set_base_score(self):
        """Test the base score."""
        self.assertEqual(self.game.base_score, 100)
        with self.assertRaises(TypeError):
            self.game.set_base_score('one hundred')

    def test_nodes_existence(self):
        """Test if starting and ending nodes exist in the graph."""
        self.assertIn(self.game.starting_node, self.game.get_nodes())
        self.assertIn(self.game.ending_node, self.game.get_nodes())
        with self.assertRaises(ValueError):
            self.game.set_starting_node(100)  # Assuming node index 100 does not exist

    def test_game_outcome(self):
        """Test the game outcome method."""
        self.game.generate_cutoff()  # First generate the cutoff
        self.assertTrue(isinstance(self.game.check_player_wins(), bool))  # Check if the result is a boolean

    def test_player_score(self):
        """Test score calculation."""
        self.game.generate_cutoff()  # Ensure cutoff is generated
        score = self.game.get_player_score()
        self.assertIsInstance(score, int)  # The score should be an integer

    def test_random_start(self):
        """Test starting a random game."""
        random_game = GraphGame.random_start()
        self.assertIsInstance(random_game, GraphGame)

if __name__ == '__main__':
    unittest.main()




