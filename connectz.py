#!/usr/bin/env python3.6
import sys
from exceptions import FullColumnError, InvalidFileError, IllegalGameError
from models import Game


def file_validator(file_path):

    """
    Check and return lines if digits found
    else raise an exception
    """

    with open(file_path, "r") as file:

        lines = file.readlines()

        first_line = lines[0].split(" ")

        for char in first_line + lines[1:]:
            if not char.strip().isdigit():
                raise InvalidFileError("File can contain only integers")

        file.close()

        # create a generator for looping on moves

        move_generator = (int(move.strip()) for move in lines[1:])

        game_params = tuple(map(
            lambda i: int(i), first_line
        ))

        # check game params, raise exception if incorrect
        # 0 : X , 1 : Y, 2 : Z

        if game_params[0] < game_params[2] or game_params[1] < game_params[2]:
            raise IllegalGameError("Game parameters are invalid")

    return game_params, move_generator


def solver(file_path):

    """
    Test game data and return an output code
    """

    try:
        game_params, lines = file_validator(file_path)

    except InvalidFileError:
        return "8"

    except IllegalGameError:
        return "7"

    # Init game
    X, Y, Z = game_params

    game = Game(X, Y, Z)

    # starting moves

    for col_move in lines:

        if col_move >= 1 and col_move <= X:

            # add move to the board

            try:
                game.add_move_to_the_board(col_move)
            except FullColumnError:
                # column already full
                return "5"

            if game.game_won:
                return "4"

            # search a winning line
            for line in game.lines:
                if line.cells_count == Z:
                    game.game_won = True
                    game.winner = str(line.player)

        else:
            # Incorrect move into column
            return "6"

    if game.winner:
        # We have a winner !
        return game.winner

    elif game.is_draw():
        return "0"
    else:
        # Incomplete game
        return "3"


def main(args):

    """

    Main method

    Check the input file and start the solver
    Return an output code
    """

    code = None

    if not args or len(args) != 1:
        # Incorrect parameters
        code = "Provide one input file"
    else:
        try:
            code = solver(args[0])
        except IOError:
            code = "9"

    return code


if __name__ == "__main__":
    output = main(sys.argv[1:])
    sys.stdout.write(output + "\r\n")
