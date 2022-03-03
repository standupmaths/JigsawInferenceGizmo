# JIG code from Stand-up Maths video "Why don't Jigsaw Puzzles have the correct number of pieces?"

def low_factors(n):
    # all the factors which are the lower half of each factor pair
    lf = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            lf.append(i)
    return lf


def jig(w,h,n,b=0):
    
    # percentage we'll check in either direction
    threshold = 0.1

    # the extra badness per piece
    penalty = 1.005

    ratio = max(w,h)/min(w,h)   # switched to be greater than 1
    
    print("")
    print(f"{w} by {h} is picture ratio {round(ratio,4)}")
    print("")
    
    max_cap = int((1+threshold)*n)
    min_cap = int((1-threshold)*n)

    up_range = [i for i in range(n,max_cap+1)]
    down_range = [i for i in range(min_cap,n)]  # do not want n included again
    down_range.reverse()

    # start at 100 which is silly high and then move down.
    up_best = 100
    up_best_deets = []
    down_best = 100
    down_best_deets = []

    # I am using the run marker so I know if looking above or below n
    run = 0

    for dis_range in [up_range,down_range]:
        best_n = 0
        best_n_ratio = 0
        best_n_sides = []
        
        if run == 0:
            print(f"Looking for >= {n} solutions:")
            print("")
        else:
            print("")
            print("Just out of interest, here are smaller options:")
            print("")
        
        for i in dis_range:
            this_best = 0
            for j in low_factors(i):
                j2 = int(i/j)   # must be a whole number anyway
                this_ratio = j2/j
                if this_best == 0:
                    this_best =  this_ratio
                    best_sides = [j,j2]
                else:
                    if abs(this_ratio/ratio - 1) < abs(this_best/ratio - 1):
                        this_best = this_ratio
                        best_sides = [j,j2]
            yes = 0
            if best_n == 0:
                yes = 1
            else:
                if abs(this_best/ratio - 1) < abs(best_n_ratio/ratio - 1):
                    yes = 1
            if yes == 1:
                best_n = i
                best_n_ratio = this_best
                best_n_sides = best_sides
                piece_ratio = max(ratio,this_best)/min(ratio,this_best)
                badness_score = (penalty**(abs(i-n)))*piece_ratio
                if run == 0:
                    if badness_score < up_best:
                        up_best = badness_score
                        up_best_deets = [best_n,best_n_sides,best_n_ratio]
                else:
                    if badness_score < down_best:
                        down_best = badness_score
                        down_best_deets = [best_n,best_n_sides,best_n_ratio]
                print(f"{best_n} pieces in {best_n_sides} (grid ratio {round(best_n_ratio,4)}) needs piece ratio {round(piece_ratio,4)}")
                if b==1:
                    print(f"[badness = {round(badness_score,5)}]")
                

        print(f"for {n} the best is {best_n} pieces with size {best_n_sides}")
        
        run += 1
    print("")
    print(f"If I had to guess: I think it's {up_best_deets[0]} pieces.")

    if down_best < up_best:
        print("")
        print(f"BUT, fun fact, {down_best_deets[0]} would be even better.")

    print("")
    return 'DONE'

# I duplicated jig_v0 to make is easier to show in the video
def jig_v0(w,h,n,b=0):
    
    # percentage we'll check in either direction
    threshold = 0.1

    penalty = 1.005

    ratio = max(w,h)/min(w,h)   # switched to be greater than 1
    
    print("")
    print(f"{w} by {h} is picture ratio {round(ratio,4)}")
    print("")
    
    max_cap = int((1+threshold)*n)
    min_cap = int((1-threshold)*n)

    up_range = [i for i in range(n,max_cap+1)]
    down_range = [i for i in range(min_cap,n)]  # do not want n included again
    down_range.reverse()

    # start at 100 which is silly high and then move down.
    up_best = 100
    up_best_deets = []
    down_best = 100
    down_best_deets = []

    run = 0

    for dis_range in [up_range,down_range]:
        best_n = 0
        best_n_ratio = 0
        best_n_sides = []

        if run == 0:
            print(f"Looking for >= {n} solutions:")
            print("")
        else:
            print("")
            print("Just out of interest, here are smaller options:")
            print("")
        
        for i in dis_range:
            this_best = 0
            for j in low_factors(i):
                j2 = int(i/j)   # must be a whole number anyway
                this_ratio = j2/j
                if this_best == 0:
                    this_best =  this_ratio
                    best_sides = [j,j2]
                else:
                    if abs(this_ratio/ratio - 1) < abs(this_best/ratio - 1):
                        this_best = this_ratio
                        best_sides = [j,j2]
            yes = 0
            if best_n == 0:
                yes = 1
            else:
                if abs(this_best/ratio - 1) < abs(best_n_ratio/ratio - 1):
                    yes = 1
            if yes == 1:
                best_n = i
                best_n_ratio = this_best
                best_n_sides = best_sides
                piece_ratio = max(ratio,this_best)/min(ratio,this_best)
                badness_score = (penalty**(abs(i-n)))*piece_ratio
                if run == 0:
                    if badness_score < up_best:
                        up_best = badness_score
                        up_best_deets = [best_n,best_n_sides,best_n_ratio]
                else:
                    if badness_score < down_best:
                        down_best = badness_score
                        down_best_deets = [best_n,best_n_sides,best_n_ratio]
                print(f"{best_n} pieces in {best_n_sides} (grid ratio {round(best_n_ratio,4)}) needs piece ratio {round(piece_ratio,4)}")
                if b==1:
                    print(f"[badness = {round(badness_score,5)}]")
                

        
        run += 1


    print("")
    return 'DONE'


