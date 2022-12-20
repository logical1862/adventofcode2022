"""gotta get my stuff back"""
from matplotlib import pyplot as plt
import sys # needed for bignum config

sys.set_int_max_str_digits(100000000)

modulo = 1

class Create_Monkey():
    """returns an instance of a monkey playing catch with my stuff
        Ex input -> :
Monkey 2:
  Starting items: 52, 95
  Operation: new = old * 5 < supports '[+, -, /, *] old' as operation on previous value during inspection 
  Test: divisible by 3
    If true: throw to monkey 5
    If false: throw to monkey 4

    """
    def __init__(self, data:list[str], part_one_true:bool):
        self.items:list[int] = [int(x) for x in data[1].split('items: ')[1][:].split(',')]
        self.operation = data[2].split('old ')[1]
        self.if_test_val = int(data[3].split('by ')[1])
        self.true_val = int(data[4].split('monkey ')[1])
        self.false_val = int(data[5].split('monkey ')[1])
        self.num_inspections= 0
        self.part_one_true:bool = part_one_true


    def inspect_item(self, item:int):
        """returns worry value of item after operation"""
        self.num_inspections += 1

        if self.operation[1:] == ' old':

            combined_express = f'{str(item)}{self.operation[0]}{str(item)}'
        else:

            combined_express = f'{str(item)}{self.operation}'

        if self.part_one_true:
            return (eval(combined_express)) // 3

        else:

            return eval(combined_express) % modulo



    def test_item(self, item:int):
        """returns monkey to throw item to"""
        if int(item) % self.if_test_val == 0:
            return self.true_val
        return self.false_val

    def throw_items(self):
        """pops items in list after inspecting each"""
        try:
            inspected = self.items.pop(0)
            return self.inspect_item(inspected)

        except IndexError:
            return 0

    def catch_item(self, item: int):
        """adds caught item to end of list"""

        self.items.append(item)


def plot_one(history):
    ax = plt.figure().add_subplot(projection='3d')
    for x in history[0]:
        y = [0 for _ in x]
        x = [int(x) for x in x]
        print(x)
        ax.plot(x, y)
    plt.show()

def part_one(data: list) -> int:
    """returns level of monkey business after 20 rounds"""
    # monkey business is two active monkeys sum inspections, multiplied
    # ex: money 3 and 4 are most active with a sum of 10 and 10
    # monkey busniess = 10 * 10

   
    
    # one object for each monkey
    troop = [Create_Monkey(x.split('\n'), True) for x in data]
    history = [[] for _ in troop]
    # 20 rounds
    for i in range(20):
        # each monkey in the troop
        for monkey in troop:

            for j in range (len(monkey.items)):

                item_to_throw = monkey.throw_items()
                catcher = monkey.test_item(item_to_throw)
                troop[catcher].catch_item(item_to_throw)

                for x in range(len(troop)):
                    history[x].append(monkey.items[:])




        print(f'round: {i} complete')

    activity_levels = sorted([x.num_inspections for x in troop], reverse=True)

    assistant_reg_manager = activity_levels.pop(0)
    assistant_to_reg_manager = activity_levels.pop(0)

    plot_one(history)

    return assistant_reg_manager * assistant_to_reg_manager

def part_two(data: list) -> int:
    """returns level of monkey business after 10000 rounds"""
    # monkey business is two active monkeys sum inspections, multiplied
    # ex: money 3 and 4 are most active with a sum of 10 and 10
    # monkey busniess = 10 * 10

    # one object for each monkey
    troop = [Create_Monkey(x.split('\n'), False) for x in data]

    
    for monkey in troop:
       global modulo
       modulo *= monkey.if_test_val

    # 10000 rounds
    for i in range(1, 10001):
        # each monkey in the troop
        for monkey in troop:
            num_items = len(monkey.items)

            for j in range(num_items):

                item_to_throw = monkey.throw_items()
                catcher = monkey.test_item(item_to_throw)
                troop[catcher].catch_item(item_to_throw)



        if i == 1 or i % 1000 == 0 or i == 10000 or i == 20:
            print(f'round: {i} complete')
            for monkey in troop:
                print(monkey.num_inspections)


    activity_levels = sorted([x.num_inspections for x in troop], reverse=True)

    assistant_reg_manager = activity_levels.pop(0)
    assistant_to_reg_manager = activity_levels.pop(0)

    with open('AdventOfCode2022\\Day11_part_two_result', 'a') as save_file:
        save_file.write(str(assistant_reg_manager * assistant_to_reg_manager) + '\n')

    return (assistant_reg_manager * assistant_to_reg_manager)





if __name__ == "__main__":
    path = 'AdventOfCode2022\\Day11_input.txt'
    test_path = 'AdventOfCode2022\\Day11_test_input.txt'

    with open(path, 'rt', encoding='UTF-8') as inputfile:
        monkeys = inputfile.read().split('\n\n')

    # print(part_one(monkeys))
    print(part_two(monkeys))
