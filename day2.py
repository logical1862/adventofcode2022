"""Can I trust the elf?"""

# A, X = rock
# B, Y = paper
# C, Z = sciscers

def shape_score(hand: str) -> int:
    """return score for each round, shape and results"""
    scores = {"Y": 2, "Z": 3, "X":1}
    return scores[hand]

def round_score(hand:list[str]) -> int:
    """return 6 if win, 3 if draw, 0 if loss"""
    #boolean flags
    opp_rock =  hand[0] =="A"
    opp_scisc = hand[0] =="C"
    opp_paper = hand[0] =="B"
    me_rock = hand[1] =="X"
    me_paper = hand[1] =="Y"
    me_scisc = hand[1] =="Z"

    # draw
    if (opp_rock and me_rock) or (opp_scisc and me_scisc) or (opp_paper and me_paper):
        return 3
    # win
    if (opp_rock and me_paper) or (opp_scisc and me_rock) or (opp_paper and me_scisc):
        return 6
    # loss
    if (opp_rock and me_scisc) or (opp_scisc and me_paper) or (opp_paper and me_rock):
        return 0

def part_one():
    """Displays score of elf cheat sheet"""
    total_score = 0

    # convert hand to number
    # get winner
    # pass to round_score to add all up

    with open("AdventOfCode2022\\Day2_input.txt", "rt", encoding="utf-8") as tournament:

        for hand in tournament.readlines():
            total_score += shape_score(hand.split()[1])
            total_score += round_score(hand.split())


    print(total_score)

def round_score_part_two(hand:list[str]) -> int:
    """return 6 if win, 3 if draw, 0 if loss"""

    elf_shape = hand[0]

    me_lose = hand[1] =="X"
    me_draw = hand[1] =="Y"
    me_win = hand[1] =="Z"

    #score dictionaries returns shape score

    win_combo = {"A":2,"B":3, "C":1}

    lose_combo = {"A":3,"B":1, "C":2}

    draw_combo = {"A":1,"B":2, "C":3}


    # draw
    if me_draw:
        return draw_combo[elf_shape] + 3
    # win
    if me_win:
        return win_combo[elf_shape] + 6
    # loss
    if me_lose:
        return lose_combo[elf_shape] + 0


def part_two():
    """part two with correct docs"""
    real_score = 0
    with open("AdventOfCode2022\\Day2_input.txt", "rt", encoding="utf-8") as tournament:

        for hand in tournament.readlines():
            real_score += round_score_part_two(hand.split())

    print(real_score)


if __name__ == "__main__":
    print('part one:')
    part_one()
    print('part two:')
    part_two()
