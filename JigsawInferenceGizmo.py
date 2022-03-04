#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

# ======================================================================================================================
#
#       MIT License | Copyright (c) 2022 Stand-up Maths
#
#   JIG code from Stand-up Maths video "Why don't Jigsaw Puzzles have the correct number of pieces?"
# ======================================================================================================================


def low_factors(n: int) -> list:
    """
    all the factors which are the lower half of each factor pair
    :param n:
    :return:
    """
    return [i for i in range(1, int(n ** .5) + 1) if n % i == 0]


def jig(w: float, h: float, n: int, b=0) -> str:
    """

    :param w:
    :param h:
    :param n:
    :param b:
    :return: ok message ('DONE')
    """
    # percentage we'll check in either direction
    threshold = 0.1

    # the extra badness per piece
    penalty = 1.005

    ratio = max(w, h) / min(w, h)  # switched to be greater than 1

    print(f"\n{w} by {h} is picture ratio {round(ratio, 4)}\n")

    max_cap = int((1 + threshold) * n)
    min_cap = int((1 - threshold) * n)

    up_range = [i for i in range(n, max_cap + 1)]
    down_range = [i for i in range(min_cap, n)]  # do not want n included again
    down_range.reverse()

    # start at 100 which is silly high and then move down.
    up_best = 100
    up_best_deets = []
    down_best = 100
    down_best_deets = []

    # I am using the run marker so I know if looking above or below n
    run = 0

    for dis_range in [up_range, down_range]:
        best_n = False
        best_n_ratio = False
        best_n_sides = []

        if not run:
            print(f"Looking for >= {n} solutions:\n")
        else:
            print("\nJust out of interest, here are smaller options:\n")

        for i in dis_range:
            this_best = False
            for j in low_factors(i):
                j2 = int(i / j)  # must be a whole number anyway
                this_ratio = j2 / j
                if not this_best:
                    this_best = this_ratio
                    best_sides = [j, j2]
                else:
                    if abs(this_ratio / ratio - 1) < abs(this_best / ratio - 1):
                        this_best = this_ratio
                        best_sides = [j, j2]
            yes = False
            if not best_n:
                yes = True
            else:
                if abs(this_best / ratio - 1) < abs(best_n_ratio / ratio - 1):
                    yes = True
            if yes:
                best_n = i
                best_n_ratio = this_best
                best_n_sides = best_sides
                piece_ratio = max(ratio, this_best) / min(ratio, this_best)
                badness_score = (penalty ** (abs(i - n))) * piece_ratio
                if run == 0:
                    if badness_score < up_best:
                        up_best = badness_score
                        up_best_deets = [best_n, best_n_sides, best_n_ratio]
                else:
                    if badness_score < down_best:
                        down_best = badness_score
                        down_best_deets = [best_n, best_n_sides, best_n_ratio]
                print(f"{best_n} pieces in {best_n_sides} (grid ratio {round(best_n_ratio, 4)}) needs piece ratio {round(piece_ratio, 4)}")
                if b:
                    print(f"[badness = {round(badness_score, 5)}]")

        print(f"for {n} the best is {best_n} pieces with size {best_n_sides}")

        run += 1
    print(f"\nIf I had to guess: I think it's {up_best_deets[0]} pieces.\n")

    if down_best < up_best:
        print(f"BUT, fun fact, {down_best_deets[0]} would be even better.\n")

    return 'DONE'


# I duplicated jig_v0 to make is easier to show in the video
def jig_v0(w: float, h: float, n: int, b=0) -> str:
    """

    :param w:
    :param h:
    :param n:
    :param b:
    :return: ok message ('DONE')
    """
    # percentage we'll check in either direction
    threshold = 0.1

    penalty = 1.005

    ratio = max(w, h) / min(w, h)  # switched to be greater than 1

    print(f"\n{w} by {h} is picture ratio {round(ratio, 4)}\n")

    max_cap = int((1 + threshold) * n)
    min_cap = int((1 - threshold) * n)

    up_range = [i for i in range(n, max_cap + 1)]
    down_range = [i for i in range(min_cap, n)]  # do not want n included again
    down_range.reverse()

    # start at 100 which is silly high and then move down.
    up_best = 100
    up_best_deets = []
    down_best = 100
    down_best_deets = []

    run = 0

    for dis_range in [up_range, down_range]:
        best_n = 0
        best_n_ratio = 0
        best_n_sides = []

        if run == 0:
            print(f"Looking for >= {n} solutions:\n")
        else:
            print("\nJust out of interest, here are smaller options:\n")

        for i in dis_range:
            this_best = 0
            for j in low_factors(i):
                j2 = int(i / j)  # must be a whole number anyway
                this_ratio = j2 / j
                if this_best == 0:
                    this_best = this_ratio
                    best_sides = [j, j2]
                else:
                    if abs(this_ratio / ratio - 1) < abs(this_best / ratio - 1):
                        this_best = this_ratio
                        best_sides = [j, j2]
            yes = 0
            if best_n == 0:
                yes = 1
            else:
                if abs(this_best / ratio - 1) < abs(best_n_ratio / ratio - 1):
                    yes = 1
            if yes == 1:
                best_n = i
                best_n_ratio = this_best
                best_n_sides = best_sides
                piece_ratio = max(ratio, this_best) / min(ratio, this_best)
                badness_score = (penalty ** (abs(i - n))) * piece_ratio
                if run == 0:
                    if badness_score < up_best:
                        up_best = badness_score
                        up_best_deets = [best_n, best_n_sides, best_n_ratio]
                else:
                    if badness_score < down_best:
                        down_best = badness_score
                        down_best_deets = [best_n, best_n_sides, best_n_ratio]
                print(f"{best_n} pieces in {best_n_sides} (grid ratio {round(best_n_ratio, 4)}) needs piece ratio {round(piece_ratio, 4)}")
                if b == 1:
                    print(f"[badness = {round(badness_score, 5)}]")

        run += 1

    print("")
    return 'DONE'


if __name__ == '__main__':
    # TODO maybe change to an argument parser (import argparse)

    w = float(input("Width: "))
    h = float(input("Height: "))
    n = int(input("Number of pieces: "))
    b = False if input(r"Debug mode on (1) or off (0)? [0\1]") != '1' else True

    if input(r"Version 0 or newest? [0\N]").lower() != '0':
        jig(w, h, n, b)
    else:
        jig_v0(w, h, n, b)

