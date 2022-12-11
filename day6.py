"""somehow i always get the broken comms"""

def part_one():
    path = r'AdventOfCode2022\Day6_input.txt'
    with open(path, 'rt', encoding='UTF-8') as signal:
        char_list = signal.read()
        for count, char in enumerate(char_list):
            sub_string = char_list[count:count + 4]

            sub_set = set(sub_string)

            if len(sub_set) == 4:
                print(count + 4)
                return
    print('signal not found')
    return

def part_two():
    """same as part one but read the message at 14 instead of marker at 4"""
    path = r'AdventOfCode2022\Day6_input.txt'
    with open(path, 'rt', encoding='UTF-8') as signal:
        char_list = signal.read()
        for count, char in enumerate(char_list):
            sub_string = char_list[count:count + 14]

            sub_set = set(sub_string)

            if len(sub_set) == 14:
                print(count + 14)
                return
    print('signal not found')
    return

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()