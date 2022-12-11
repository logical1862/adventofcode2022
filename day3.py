"""Silly elf didnt pack right"""



def get_double_item(pack_list: str) :
    """returns character code for mispacked item"""
    num_items = len(pack_list)
    first_compartment_end = int(num_items / 2)
    second_compartment_end = first_compartment_end * 2
    for item in pack_list[:first_compartment_end]:
        for second_comp_item in pack_list[first_compartment_end:]:
            if item == second_comp_item:
                return item
    return 0

def get_priority(code:str) -> int:
    code_ord = ord(code)
    if code_ord > 91:
        return code_ord - 96

    return code_ord - 38

def part_one() -> None:
    with open("AdventOfCode2022\\Day3_input.txt", "rt", encoding="utf-8") as rucksacks:
        total = 0
        for pack in rucksacks.readlines():
            item_code = get_double_item(pack)
            priority_number = get_priority(item_code)
            total += priority_number
    print(total)

def get_group_id(group:list[str]) -> str:
    for item in group[0]:
        group_1 = group[1]
        group_2 = group[2]
        for item_two in group_1:
            if item == item_two:
                for another_one in group_2:
                    if another_one == item_two:
                        return item
    

def part_two():
    with open("AdventOfCode2022\\Day3_input.txt", "rt", encoding="utf-8") as rucksacks:
        complete_list = rucksacks.readlines()
        end_of_list = False
        start_group = 0
        end_group = 3
        increment = 3
        num_elves = len(complete_list)
        total = 0
        while not end_of_list:
            group = complete_list[start_group:end_group]

            group_id = get_group_id(group)
           
            total += get_priority(group_id)

            start_group += increment
            end_group += increment

            if end_group > num_elves:
                end_of_list = True
        print(total)

def main():
    # part_one()
    part_two()
if __name__ == "__main__":
    main()
