from unittest import TestCase
from .helper import run_connectz


class TestsValidOutputCodes(TestCase):

    """
    Test valid codes returned by Connectz
    """

    def test_return_3_if_incomplete_game(self):

        """
        If game is incompleted neither won or draw, return 3
        """

        result = run_connectz("valid/incomplete_game.txt")

        self.assertEqual("3", result.strip())

    def test_return_1_if_player1_won(self):

        """
        If player 1 won, return 1
        """

        result = run_connectz("valid/player_won/player1_won.txt")

        self.assertEqual("1", result.strip())

    def test_return_1_if_player1_won_vertically(self):

        """
        If player 1 won, return 1
        """

        result = run_connectz("valid/player_won/player1_won_vertically.txt")

        self.assertEqual("1", result.strip())

    def test_return_1_if_player1_won_horizontally(self):

        """
        If player 1 won, return 1
        """

        result = run_connectz("valid/player_won/player1_won_horizontally.txt")

        self.assertEqual("1", result.strip())

    def test_return_1_if_player1_won_diagonally(self):

        """
        If player 1 won, return 1
        """

        result = run_connectz("valid/player_won/player1_won_diagonally.txt")

        self.assertEqual("1", result.strip())

    def test_return_2_if_player2_won(self):

        """
        If player 2 won, return 2
        """

        result = run_connectz("valid/player_won/player2_won.txt")

        self.assertEqual("2", result.strip())

    def test_return_2_if_player2_won_vertically(self):

        """
        If player 2 won, return 2
        """

        result = run_connectz("valid/player_won/player2_won_vertically.txt")

        self.assertEqual("2", result.strip())

    def test_return_2_if_player2_won_horizontally(self):

        """
        If player 2 won, return 2
        """

        result = run_connectz("valid/player_won/player2_won_horizontally.txt")

        self.assertEqual("2", result.strip())

    def test_return_2_if_player2_won_diagonally(self):

        """
        If player 2 won, return 2
        """

        result = run_connectz("valid/player_won/player2_won_diagonally.txt")

        self.assertEqual("2", result.strip())

    def test_return_0_if_draw(self):

        """
        If draw, return 0
        """

        result = run_connectz("valid/draw.txt")

        self.assertEqual("0", result.strip())


    def test_return_1_if_player1_won_vertically_game_100_x_100(self):

        """
        If player 1 won diagonally, return 1
        """

        result = run_connectz("valid/player_won/player1_won_vertically_100_x_100.txt")

        self.assertEqual("1", result.strip())




