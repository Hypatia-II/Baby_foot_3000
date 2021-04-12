import unittest
from baby_foot_3000 import *
from player import *
from bar import *
from terrain import *

class Player_test(unittest.TestCase):

    def setUp(self):
        self.blue_bar = Bar(2, 2, 1, 'blue')
        self.blue_player1 = Player('blue', self.blue_bar, 1, 2)
        self.blue_player2 = Player('blue', self.blue_bar, 1, 2)
        self.red_bar = Bar(1, 1, 1, 'red')
        self.red_player = Player('red', self.red_bar, 1, 1)


    def test_red_player_team_is_not_blue_player_team(self):
        self.assertIsNot(self.blue_player1.team, self.red_player.team) # Validé

    def test_blue_player_has_same_type_as_red_player(self):
        self.assertIs(type(self.blue_player1), type(self.red_player)) # Validé

    def test_blue_player_1_is_not_blue_player_2(self):
        self.assertIsNot(self.blue_player1, self.blue_player2)

    def test_blue_player1_team_is_blue_player1_team(self):
        self.assertIs(self.blue_player1.team, self.blue_player2.team)

    def test_red_player_in_red_bar(self):
        self.assertIs(type(self.red_player), type(self.red_bar[0]))
        self.assertTrue(type(self.red_bar[0]) is Player)

class Bar_test(unittest.TestCase):

    def setUp(self):
        self.blue_bar = Bar(2, 2, 1, 'blue')

    def test_bar_is_a_list(self):
        self.assertIsInstance(self.blue_bar, list) # Validé

class Ball_Terrain_test(unittest.TestCase):

    def setUp(self):
        self.terrain = Terrain()
        self.ball = Ball(self.terrain)

    def test_terrain(self):
        self.assertIsInstance(self.terrain, Terrain)

    def test_ball(self):
        self.assertIsInstance(self.ball, Ball)

    def test_terrain_is_in_ball(self):
        self.assertIs(self.terrain, self.ball.terrain)



if __name__ == '__main__':
    unittest.main()

