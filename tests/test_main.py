from unittest import TestCase, skip
from .helper import TESTS_PATH
from exceptions import InvalidFileError, IllegalGameError
from connectz import file_validator, main, solver


class TestFileValidator(TestCase):

    """
    Test the file validator function
    """

    def test_can_return_lines_if_correct_file(self):

        """
        Test can return two values : (game_params, lines)
        """

        file_path = TESTS_PATH + "valid/player_won/player1_won.txt"
        game_params, lines = file_validator(file_path)

        self.assertTrue(game_params)
        self.assertEqual(3, len(game_params))

        self.assertTrue(lines)


    def test_can_raise_exception_if_invalid_file(self):

        """
        Raise an exception if invalid file
        """

        with self.assertRaises(InvalidFileError):
            file_path = TESTS_PATH + "/error/invalid_file.txt"
            file_validator(file_path)

    def test_can_raise_exception_if_invalid_game(self):

        """
        Raise an exception if invalid game
        """

        with self.assertRaises(IllegalGameError):
            file_path = TESTS_PATH + "error/illegal_game.txt"
            file_validator(file_path)


class TestsMain(TestCase):

    """
    Test the main procedure
    """

    def test_can_return_message_if_incorrect_args(self):
        output = main([])
        self.assertEqual("Provide one input file", output)

    def test_can_return_error_code_if_file_not_found(self):
        output = main([
            TESTS_PATH + "valid/player_won/player1_wo.txt"
        ])
        self.assertEqual("9", output)


@skip
class TestsSolver(TestCase):

    """
    Test the solver function
    """

    def test_can_return_8_if_invalid_file(self):
        output = solver(
            TESTS_PATH + "error/invalid_file.txt"
        )
        self.assertEqual("8", output)

    def test_can_return_7_if_illegal_game(self):
        output = solver(
            TESTS_PATH + "error/illegal_game.txt"
        )
        self.assertEqual("7", output)

    def test_can_return_6_if_illegal_column(self):
        output = solver(
            TESTS_PATH + "error/illegal_column.txt"
        )
        self.assertEqual("6", output)

    def test_can_return_5_if_illegal_continue(self):
        output = solver(
            TESTS_PATH + "error/illegal_row.txt"
        )
        self.assertEqual("5", output)

    def test_can_return_4_if_illegal_continue(self):
        output = solver(
            TESTS_PATH + "error/illegal_continue.txt"
        )
        self.assertEqual("4", output)

    def test_can_return_3_if_incomplete_game(self):
        output = solver(
            TESTS_PATH + "valid/incomplete_game.txt"
        )
        self.assertEqual("3", output)

    def test_can_return_2_if_player_2_won(self):
        output = solver(
            TESTS_PATH + "valid/player_won/player2_won.txt"
        )
        self.assertEqual("2", output)

    def test_can_return_1_if_player_1_won(self):
        output = solver(
            TESTS_PATH + "valid/player_won/player1_won.txt"
        )
        self.assertEqual("1", output)

    def test_can_return_0_if_game_drawn(self):
        output = solver(
            TESTS_PATH + "valid/draw.txt"
        )
        self.assertEqual("0", output)
