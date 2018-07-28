from exceptions import InvalidDimensionError, FullColumnError


class Cell:

    """
    A Cell represents a cell in the board
    """

    def __init__(self, player, x, y):
        self.x = x
        self.y = y
        self.id = (self.x, self.y)

        self.player = player

    def __repr__(self):
        return "Cell ({} {} {})".format(self.player, self.x, self.y)


class Neighbour:

    """
    A neighbour is
    """

    def __init__(self, player, x, y):
        self.x = x
        self.y = y
        self.id = (self.x, self.y)
        self.player = player
        self.id = (self.x, self.y)

class Line:

    """
    A Line represents a line of cells in the board
    """

    cells = []
    cells_count = 0
    type = None

    def __init__(self, cells, player):
        if cells and player in [1,2]:
            self.cells = cells
            self.cells_count = len(cells)
            self.player = player
        else:
            raise ValueError("Cells list cannot be empty")

    def contains_cell(self, new_cell):

        """
        Check if cells already in lines
        """

        return new_cell in self.cells

    def add(self, cell):
        self.cells.append(cell)
        self.increment_counter()

    def increment_counter(self):
        self.cells_count = self.cells_count + 1

    def __repr__(self):
        return "Line : {}".format(self.cells)


class Game:

    col_counters = {}

    current_player = None

    lines = []

    game_won = False
    winner = None

    def __init__(self, X, Y, Z):

        if X >= 2 and Y >= 2:
            self.X = X
            self.Y = Y
            self.Z = Z
        else:
            raise InvalidDimensionError()

        self.col_counters = {col: 0 for col in range(1, self.X + 1)}

    def switch_player(self):
        if self.current_player is None or self.current_player == 2:
            self.current_player = 1
        else:
            self.current_player = 2

    def increment_col_counter(self, col):
        self.col_counters[col] += 1

    def is_draw(self):

        """
        Return True if game is dawn else False
        """

        return all([self.col_counters[col] == self.Z for col in self.col_counters])

    def add_move_to_the_board(self, col):

        self.switch_player()

        # does column have free rows left ?

        if self.col_counters[col] < self.Z:
            cell = Cell(self.current_player, col, self.col_counters[col])
        else:
            raise FullColumnError()

        matches = self.get_matching_lines_for_cell(cell)

        for index in matches:

            if self.lines[index].cells_count == 1:
                # create new line for the first cell
                self.lines.append(Line([self.lines[index].cells[0]], self.current_player))

            # add new cell to line
            self.lines[index].add(cell)

        else:
            self.lines.append(Line([cell], self.current_player))

        self.increment_col_counter(col)

    def match_horizontally(self, new_line):

        """
        Return True if match horizontally else False)

        X X
        O O O
        """

        return  all([
            (cell.x == new_line[pos - 1].x + 1 and cell.y == new_line[pos - 1].y) or pos == 0
            for pos, cell in enumerate(new_line)
        ])

    def match_vertically(self, new_line):

        """
        Return True if match vertically else False

        O
        O X
        O X
        """

        return all([
            (cell.y == new_line[pos - 1].y + 1 and cell.x == new_line[pos - 1].x) or pos == 0
            for pos, cell in enumerate(new_line)
        ])

    def match_diagonally_to_top(self, new_line):

        """
        Return True if match diagonally to top else False

            0
        X 0 X
        0 X O
        """

        return all([
            (cell.y == new_line[pos - 1].y + 1 and cell.x == new_line[pos - 1].x + 1) or pos == 0
            for pos, cell in enumerate(new_line)
        ])

    def match_diagonally_to_bottom(self, new_line):

        """
        Return True if match diagonally to bottom else False

        0
        X O
        X X O
        """

        return all([
            (cell.y == new_line[pos - 1].y - 1 and cell.x == new_line[pos - 1].x + 1) or pos == 0
            for pos, cell in enumerate(new_line)
        ])

    def get_matching_lines_for_cell(self, new_cell):

        """
        Return a list of index whose lines
        match with the new cell
        """

        matches = []

        for index, line in enumerate(self.lines):

            if not line.contains_cell(new_cell) and  line.player == new_cell.player:

                new_line = line.cells + [new_cell]
                new_line.sort(key=lambda x: x.id)

                if self.match_horizontally(new_line):
                    matches.append(index)

                if self.match_vertically(new_line):
                    matches.append(index)

                if self.match_diagonally_to_top(new_line):
                    matches.append(index)

                if self.match_diagonally_to_bottom(new_line):
                    matches.append(index)

        return matches
