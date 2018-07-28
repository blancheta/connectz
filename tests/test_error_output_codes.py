from unittest import TestCase, skip
from .helper import run_connectz


class TestErrorIncorrectArgs(TestCase):

    """
    Test error returned by Connectz
    """

    def test_display_error_message(self):

        """
        If none or more than one argument,
        return the message "Provide one input file"
        """

        result = run_connectz()

        self.assertEqual("Provide one input file", result.strip())


class TestErrorOutputCodes(TestCase):

    """
    Test error output codes returned by Connectz
    """

    def test_return_9_if_file_cannot_be_found(self):

        """
        If the file cannot be found, return 9
        """

        result = run_connectz("test_cases/no-file.txt")

        self.assertEqual("9", result.strip())

    @skip
    def test_return_9_if_file_cannot_be_opened(self):

        """
        If the file cannot be opened, return 9
        """

        result = run_connectz("error/cannot_be_read.txt")

        self.assertEqual("9", result.strip())

    @skip
    def test_return_9_if_file_cannot_be_read(self):

        """
        If the file cannot be opened, return 9
        """

        result = run_connectz("error/cannot_be_read.txt")

        self.assertEqual("9", result.strip())

    def test_return_8_if_invalid_file(self):

        """
        If the game is error, return 8
        """

        result = run_connectz("error/invalid_file.txt")

        self.assertEqual("8", result.strip())

    def test_return_7_if_incorrect_dimensions(self):

        """
        If dimensions are incorrect
        and the game cannot be won, return 7
        """

        result = run_connectz("error/illegal_game.txt")

        self.assertEqual("7", result.strip())

    def test_return_6_if_move_outside_the_board(self):

        """
        If move is outside the board, return 6
        """

        result = run_connectz("error/illegal_column.txt")

        self.assertEqual("6", result.strip())

    def test_return_5_if_move_into_a_full_column(self):

        """
        If move into a full column and none row are available, return 5
        """

        result = run_connectz("error/illegal_row.txt")

        self.assertEqual("5", result.strip())

    def test_return_4_if_game_has_already_been_won(self):

        """
        If move has already been won, return 4
        """

        result = run_connectz("error/illegal_continue.txt")
        self.assertEqual("4", result.strip())
