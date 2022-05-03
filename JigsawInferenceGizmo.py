# JIG code from Stand-up Maths video "Why don't Jigsaw Puzzles have the correct number of pieces?"
# Usage:
# from jig import *
# jig(PhysicalWidth, PhysicalHeight, NumberOfPieces, MoreVerboseOutput? (default = 1))
# jig_v0(a, b, c) is the same as jig(a, b, c, verbose = 0)

class JigClass:
    """
    Since the bulk of the code is heavily state reliant, this refactoring
    makes use of some basic encapsulation.
    """
    # percentage we'll check in either direction
    JIG_THRESHOLD = 0.1
    # the extra badness per piece
    PIECE_PENALTY = 1.005

    def __init__(self, w, h, n, verbose):
        self.w = w
        self.h = h
        self.n = n
        self.verbose = verbose
        self.ratio = max(w, h) / min(w, h)
        self.dir_best = [100, 100]
        self.dir_best_stats = [None, None]
        self.dir_range = (
            range(n,   int((1 + self.JIG_THRESHOLD) * n) + 1),
            range(n-1, int((1 - self.JIG_THRESHOLD) * n) - 1, -1)
        )

    def search_range(self, direction):
        best_n = 0
        best_n_ratio = 0
        best_n_sides = []
        best_stats_list = []

        for i in self.dir_range[direction]:
            this_best = 0

            for j in low_factors(i):
                j2 = int(i/j)
                this_ratio = j2/j

                if this_best == 0 or abs(this_ratio / self.ratio - 1) < abs(this_best / self.ratio - 1):
                    this_best = this_ratio
                    best_sides = [j, j2]

            if best_n == 0 or abs(this_best / self.ratio - 1) < abs(best_n_ratio / self.ratio - 1):
                best_n = i
                best_n_ratio = this_best
                best_n_sides = best_sides
                piece_ratio = max(self.ratio, this_best) / min(self.ratio, this_best)
                badness_score = (self.PIECE_PENALTY ** (abs(i - self.n))) * piece_ratio

                if badness_score < self.dir_best[direction]:
                    self.dir_best[direction] = badness_score
                    self.dir_best_stats[direction] = (best_n, best_n_sides, best_n_ratio)

                best_stats_list.append((
                    best_n,
                    dimstr(best_n_sides),
                    round(best_n_ratio, 4),
                    round(piece_ratio, 4),
                    round(badness_score, 5)
                ))

        # I changed the printout format to be a table and used the
        # extra space to include a badness score column
        # -Braden
        print("pieces  size        g. ratio  p. ratio  badness")

        for selstat in best_stats_list:
            print("%-6d  %-10s  %6.4f    %6.4f    %.5f" % selstat)

        if self.verbose:
            print(f"for {self.n} the best is {best_n} pieces with size {dimstr(best_n_sides)}")

    def report_pr(self):
        print(f"\n{self.w} by {self.h} is picture ratio {round(self.ratio, 4)}\n")

    def report_end(self):
        if not self.verbose:
            return

        print(f"\nIf I had to guess: I think it's {self.dir_best_stats[0][0]} pieces.")

        if self.dir_best[1] < self.dir_best[0]:
            print(f"\nBUT, fun fact, {self.dir_best_stats[1][0]} would be even better.")


def dimstr(dim):
    """Turns tuple or list (A, B) into string repr 'AxB'"""
    return f"{dim[0]}x{dim[1]}"

def low_factors(n):
    # all the factors which are the lower half of each factor pair
    lf = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            lf.append(i)
    return lf

def jig(w, h, n, verbose = 1):
    jc = JigClass(w, h, n, verbose)
    jc.report_pr()
    print(f"Looking for >= {n} solutions:\n")
    jc.search_range(0)
    print("\nJust out of interest, here are smaller options:\n")
    jc.search_range(1)
    jc.report_end()
    print("")
    return 'DONE'

# I duplicated jig_v0 to make is easier to show in the video
def jig_v0(w, h, n):
    return jig(w, h, n, 0)
