"""dont do it twice"""


def is_overlap_one(section: str) -> bool:
    sections = section.split(sep=',')
    one = sections[0].split(sep='-')
    two = sections[1].strip('\n')
    two = two.split(sep='-')

    #first elf is  recleaning
    if (int(one[0]) <= int(two[0])) and (int(one[1]) >= int(two[1])) :
        return True

    #second elf is recleaning
    if (int(two[0]) <= int(one[0])) and (int(two[1]) >= int(one[1])):
        return True

    return False


def is_overlap_two(section: str) -> bool:
    sections = section.split(sep=',')
    one = sections[0].split(sep='-')
    two = sections[1].strip('\n')
    two = two.split(sep='-')

    #if start of first set is lower than beginning of 2nd set AND start of second set is lower than end of first set
    if int(one[1]) >= int(two[0]) and int(one[0]) <= int(two[1]):
        return True
    # reverse now yall
    if int(two[1]) >= int(one[0]) and int(two[0]) <= int(one[1]):
        return True

    return False


def part_one():
    total = 0
    path = r'AdventOfCode2022\Day4_input.txt'
    with open(path, 'rt', encoding='UTF-8') as sections:
        for pair in sections.readlines():
            if is_overlap_one(pair):
                total += 1
    print(f'part one total {total}')

def part_two():
    total = 0
    path = r'AdventOfCode2022\Day4_input.txt'
    with open(path, 'rt', encoding='UTF-8') as sections:
        for pair in sections.readlines():
            if is_overlap_two(pair):
                    total += 1
    print(f'part two total {total}')

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
