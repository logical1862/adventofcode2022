"""read the comm signal"""


def part_one(moves:list) -> int:
    ## reg starts at 1
    # noop : 1 cycle -> no effect
    # addx n : two cycles -> increment reg by n
    # prev cycle must finish before next in row can begin

    instructions = [0 if x[4:] == '' else int(x[5:]) for x in moves]

    # signal strength = cycle num * reg value
    cpu_reg = 1
    sum_signal_strength = 0
    cur_cycle = 1

    screen: list[str] =[]



    # [cycle[value], cycle2[value]]
    reg_history = [0]


    for count, instruction in enumerate(instructions):

        if instruction == 0:

            cpu_reg += 0

            signal_str = cpu_reg * cur_cycle

            reg_history.append(cpu_reg)

            if cur_cycle == 20 or cur_cycle % 40 == 20:
                sum_signal_strength += signal_str
                print(sum_signal_strength)

            cur_cycle += 1

        else:
            cur_cycle += 1

            cpu_reg += 0

            signal_str = cpu_reg * cur_cycle
            reg_history.append(cpu_reg)



            # if happens on an add instruction decrement one reg value( or index value?) back?
            if cur_cycle == 20 or cur_cycle % 40 == 20:
                signal_str = cur_cycle * reg_history[count]
                sum_signal_strength += signal_str
                print(sum_signal_strength)

            cur_cycle += 1
            cpu_reg += instruction
            reg_history.append(cpu_reg)
     

            if cur_cycle == 20 or cur_cycle % 40 == 20:
                signal_str = cur_cycle * cpu_reg
                sum_signal_strength += signal_str
                print(sum_signal_strength)
            # part two


    col = 0
    for cycle, val in enumerate(reg_history):

        if col == val + 1 or col == val or col == val - 1:
            screen.append('|')
        else:
            screen.append(' ')
        col += 1

        if col == 40:
            col = 0
            screen.append('\n')

    print(''.join(screen))

    return 1

if __name__ == "__main__":
    path = 'AdventOfCode2022\\Day10_input.txt'
    test_path = 'AdventOfCode2022\\Day10_test_input.txt'

    with open(path, 'rt', encoding='UTF-8') as inputfile:
        moves = [x.strip('\n') for x in inputfile.readlines()]
    # part one and two are combined
    part_one(moves)
