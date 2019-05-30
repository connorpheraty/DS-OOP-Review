import unittest
from players import Player, Quarterback
from possible_values import *
from game import Game
from season import generate_rand_games
import random
# TODO - some things you can add...

# import the `season` file and make sure qgenerate_random_games only
# makes games with appropriate team names (and never has a team playing itself)

# Complete the FootballGameTest


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        teams = random.sample(team_names, 2)
        game = Game(teams=teams)
        game.field_goal(teams[0])
        self.assertEqual(game.score[teams[0]], 3)
        
    def test_get_winnerr(self):
        teams = random.sample(team_names, 2)
        game = Game(teams=teams)
        game.touchdown(teams[0])
        winner, loser =game.get_winning_team()
        self.assertEqual(winner, teams[0])


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb.passing_score())


if __name__ == '__main__':
    unittest.main()
