import random

X = 100
Y = 100
Z = 100

MODE = "RANDOM"

MODE = "PLAYER_1_VERT"

with open("{} x {}.txt".format(X, Y), 'wt') as f:

    f.write('{} {} {}\n'.format(X, Y, Z))

    if MODE == "RANDOM":

        for i in range(0, X * Y):
            f.write('{}\n'.format(random.randint(1, X)))

    elif MODE == "PLAYER_1_VERT":

        player = 1

        for i in range(0, Y * 2):

            if player == 1:
                f.write('{}\n'.format(X))
            else:
                f.write('{}\n'.format(random.randint(1, X - 1)))

            if player == 1:
                player = 2
            else:
                player = 1

