"""Find a good tree"""


def part_one(trees: list) -> int:
    """Returns number of visible trees"""
    num_columns = len(trees[0])
    num_rows = 0

    # for each row
    blocked_trees = 0

    for row, row_sight in enumerate(trees):
        num_rows += 1
        if row == 0 or row == len(trees) - 1:
            continue
        
        # for each tree
        for count, tree in enumerate(row_sight):
            last_tree = len(row_sight) - 1

            if count == 0 :
                continue
            if count == last_tree:

                continue

            tree = int(tree)

            # rows first
            beg_row = [*row_sight[:count]]
            end_row = [*row_sight[count+1:]]


            blocked_to_the_left = [True for x in beg_row if int(x) >= tree]
            blocked_to_the_right = [True for x in end_row if int(x) >= tree]

            blocked_up = []
            blocked_down = []
            # now columns


            for i in range(row + 1, len(trees)):
                if int(trees[i][count]) >= tree:
                    blocked_down.append(True)

            for j in range(row - 1, -1, -1):
                if int(trees[j][count]) >= tree:
                    blocked_up.append(True)

            if blocked_down and blocked_up and blocked_to_the_left and blocked_to_the_right:
                print(f'row : {row} --- tree : {tree} is blocked')
                blocked_trees += 1
    return (num_columns * num_rows) - blocked_trees

def part_two(trees: list) -> int:
    """returns highest scenic score from tree map"""
    # gonna need some counters
    high_score = 0
    count_up = 0
    count_down = 0
    count_left = 0
    count_right = 0


    for row, row_sight in enumerate(trees):
        # edges will have a score of zero so well skip them
        if row in (0,len(trees) - 1):
            continue

        # for each tree
        for count, tree in enumerate(row_sight):
            tree = int(tree)
            # for each dir, increment each counter until blocked or edge
            # calc score, store it,  reset counters

            # skip edges
            last_tree = len(row_sight) - 1
            if count in (0, last_tree):
                continue

            # unpack rows first
            beg_row = [*row_sight[:count]]
            end_row = [*row_sight[count+1:]]

            # left
            for next_tree in range(count - 1, -1, -1):
                count_left += 1

                if int(beg_row[next_tree]) >= tree:
                    break

            # right
            for next_tree in end_row:
                count_right += 1
                if int(next_tree) >= tree:
                    break

            # columns going down
            for i in range(row + 1, len(trees)):
                count_down += 1
                if int(trees[i][count]) >= tree:
                    break

            # going up
            for j in range(row - 1, -1, -1):
                count_up += 1
                if int(trees[j][count]) >= tree:
                   break


            # now calc the scenic score
            score = count_left * count_right * count_up * count_down
            # reset counters
            count_up = 0
            count_down = 0
            count_left = 0
            count_right = 0

            if score > high_score:
                high_score = score
    return high_score

if __name__ == "__main__":
    path = 'AdventOfCode2022\\day8_input.txt'
    test_path = 'AdventOfCode2022\\day8testinput.txt'
    test_two_path = 'AdventOfCode2022\\day8test2.txt'

    with open(path, 'rt', encoding='UTF-8') as tree_map_input:
        tree_map = [x.strip('\n') for x in tree_map_input.readlines()]


    print(part_one(tree_map))
    print(part_two(tree_map))
    