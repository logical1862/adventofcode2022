"""Find a good tree"""

def count_tree(current_count: int) ->int:
    return current_count + 1
    


def part_one(trees: list) -> int:
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

if __name__ == "__main__":
    path = 'AdventOfCode2022\\day8_input.txt'
    test_path = 'AdventOfCode2022\\day8testinput.txt'
    test_two_path = 'AdventOfCode2022\\day8test2.txt'

    with open(test_path, 'rt', encoding='UTF-8') as tree_map_input:
        tree_map = [x.strip('\n') for x in tree_map_input.readlines()]


    print(part_one(tree_map))
    