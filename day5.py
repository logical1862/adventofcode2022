
import re


def part_one():
    path = r'AdventOfCode2022\Day5_input.txt'
    stacks = []


    with open(path, 'rt', encoding='UTF-8') as full_text:
        sections = full_text.read()
        crates, instructions = sections.split('\n\n')
        stacks_list = crates[-34:]
        crates = crates[:-34]

        # get columns
        stacks = [list() for x in stacks_list if x.isnumeric()]

        # get current crate arrangement, stack count is current related column
        for line in crates.split('\n')[:-1]: # last line is all whitespace
            stack_count = 0
            for i in line[1::4]:
                if i.isalpha():
                    stacks[stack_count].append(i)
                stack_count += 1


        for movement in instructions.split('\n'):
            if not movement:
                continue
            moved = []
            if len(movement) > 18:
                num_moved = int(movement[5:7])
            else:
                num_moved = int(movement[5])

            start_stack = int(movement[-6]) - 1
            end_stack = int(movement[-1]) - 1

            for i in range(num_moved):
                crates_moved = stacks[start_stack].pop(0)

                stacks[end_stack].insert(0, crates_moved)
        for stack in stacks:
            print(stack)





def part_two():
    path = r'AdventOfCode2022\Day5_input.txt'
    stacks = []


    with open(path, 'rt', encoding='UTF-8') as full_text:
        sections = full_text.read()
        crates, instructions = sections.split('\n\n')
        stacks_list = crates[-34:]
        crates = crates[:-34]

        # get columns
        stacks = [list() for x in stacks_list if x.isnumeric()]

        # get current crate arrangement, stack count is current related column
        for line in crates.split('\n')[:-1]: # last line is all whitespace
            stack_count = 0
            for i in line[1::4]:
                if i.isalpha():
                    stacks[stack_count].append(i)
                stack_count += 1


        for movement in instructions.split('\n'):
            if not movement:
                continue
            moved = []
            if len(movement) > 18:
                num_moved = int(movement[5:7])
            else:
                num_moved = int(movement[5])

            start_stack = int(movement[-6]) - 1
            end_stack = int(movement[-1]) - 1



            for i in range(num_moved):
                crates_moved = stacks[start_stack].pop(0)
                #moved.extend(crates_moved)
                moved.append(crates_moved)

            for j in range(len(moved)):
                stacks[end_stack].insert(j, moved[j])
            
            

        for stack in stacks:
            print(stack)

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
