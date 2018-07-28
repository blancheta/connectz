from unittest import TestCase
from models import Cell, Line, Game
from exceptions import InvalidDimensionError, FullColumnError


class TestsCellModel(TestCase):

    """
    Test Cell model and its methods
    """

    def setUp(self):
        self.cell = Cell(1, 1, 1)

    def test_can_create_a_valid_cell(self):
        self.assertIsInstance(self.cell, Cell)

    def test_can_return_a_formatted_repr_for_object(self):
        self.assertEqual(self.cell.__repr__(), "Cell (1 1 1)")

    def test_can_return_a_formatted_str_for_object(self):
        self.assertEqual(self.cell.__str__(), "Cell (1 1 1)")


class TestsLineModel(TestCase):

    """
    Test Line model and its methods
    """

    def setUp(self):

        self.cell1 = Cell(1, 1, 0)
        self.cell2 = Cell(1, 1, 1)

        self.line = Line([
            self.cell1,
            self.cell2
        ], 1)

    def test_can_create_a_valid_line(self):

        """
        Test can create a valid line
        """

        self.assertIsInstance(self.line, Line)

    def test_cannot_create_invalid_line(self):

        """
        Test cannot create an invalid line
        with an empty cell list and invalid player
        """

        with self.assertRaises(ValueError):
            self.line_no_cells = Line([], 3)

    def test_can_add_a_cell_to_a_line(self):

        """
        Test can add a cell to a line and increment count for line cells
        """

        cells_count = len(self.line.cells)

        self.line.add(Cell(1, 1, 2))

        self.assertEqual(cells_count + 1, len(self.line.cells))
        self.assertEqual(self.line.cells_count, len(self.line.cells))

    def test_can_check_if_cell_is_in_line(self):

        """
        Test can return True if cell in current line else False
        """

        self.assertTrue(
            self.line.contains_cell(self.cell1)
        )

    def test_can_increment_cells_count(self):

        """
        Test can increment the cell count for the line
        """

        initial_cells_count = self.line.cells_count

        self.line.increment_counter()
        self.assertEqual(initial_cells_count + 1, self.line.cells_count)

    def test_can_return_a_formatted_repr_for_object(self):
        self.assertEqual(self.line.__repr__(), "Line : {}".format(
            self.line.cells
        ))

    def test_can_return_a_formatted_str_for_object(self):
        self.assertEqual(self.line.__str__(), "Line : {}".format(
            self.line.cells
        ))


class TestsGameModel(TestCase):

    """
    Test Game model and its methods
    """

    def setUp(self):
        self.game = Game(3, 3, 3)

        self.cell1 = Cell(1, 3, 0)
        self.cell2 = Cell(2, 1, 0)
        self.cell3 = Cell(1, 1, 1)
        self.cell4 = Cell(2, 2, 0)

    def test_cannot_create_a_board_if_height_width_less_than_2(self):

        """
        Test can raise an exception if invalid dimensions
        """

        with self.assertRaises(InvalidDimensionError):
            self.invalid_game = Game(0, 0, 4)

    def test_can_create_a_game(self):

        """
        Test can create a valid game
        """

        self.assertIsInstance(self.game, Game)

    def test_stat_game_with_player_1(self):
        """
        Test can create a game
        """

        self.game.switch_player()

        self.assertEqual(self.game.current_player, 1)

    def test_can_switch_player(self):

        """
        Test can create a game
        """

        self.game.current_player = 1

        self.game.switch_player()

        self.assertEqual(self.game.current_player, 2)

        self.game.switch_player()

        self.assertEqual(self.game.current_player, 1)

    def test_can_increment_col_counters(self):

        """
        Test can increment col counters for a column
        """

        col = 1
        self.game.increment_col_counter(col)

        self.assertEqual(self.game.col_counters[col], 1)

    def test_can_return_matching_lines_for_cell(self):

        """
        Test can return a matching line for a cell
        """

        line = Line([
            self.cell1,
        ], 1)

        line2 = Line([
            self.cell3
        ], 1)

        self.game.lines = [line, line2]

        cell = Cell(1, 2, 1)

        matches = self.game.get_matching_lines_for_cell(cell)

        self.assertEqual(len(matches), 2)

    def test_can_create_a_new_line_for_cells_matching(self):

        line = Line([
            self.cell1,
        ], 1)

        self.game.lines.append(line)

        lines_count = len(self.game.lines)

        self.game.col_counters = {
            3: 1
        }

        self.game.add_move_to_the_board(3)

        self.assertEqual(lines_count + 2, len(self.game.lines))


    def test_raise_exception_if_move_in_full_column(self):

        self.game.col_counters = {
            1: 3
        }

        with self.assertRaises(FullColumnError):
            self.game.add_move_to_the_board(1)