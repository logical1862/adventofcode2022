"""delete it all!(kinda)"""

import re

path = r'AdventOfCode2022\Day7_input.txt'

cd_up = r'\$ cd \.\.'
cd_into = r'\S cd [a-z]'
ls = r'\$ ls'


def part_one():
    listing = False
    visited_dir = {'/':0}
    seen_files = {}
    file_sum = 0
    current_dir = '/'
    all_dir_in_path = ['/']

    with open(path, 'rt', encoding="UTF-8") as file:
        commands = file.read()
        for command in commands.split(sep='\n'):
            # end of input
            if not command:
                continue

            # listing -> next series will be files/dirs in current dir
            if re.match(ls, command):
                listing = True
                continue

            # change dir into
            if re.match(cd_into, command) is not None:
                if file_sum <= 100000:
                    visited_dir[current_dir] += file_sum

                current_dir = command[5:]
                all_dir_in_path.insert(0, current_dir)
                
                file_sum = 0
                listing = False

                if current_dir not in visited_dir:
                    visited_dir[current_dir] = 0
                else:
                    current_dir = current_dir + '-1'
                    visited_dir[current_dir] = 0
                print(f'changing directory to: {command[5:]}')
                continue

            # change dir up one level
            if re.match(cd_up, command) is not None:
                listing = False
                if file_sum <= 100000:
                    visited_dir[current_dir] = file_sum
                
                
                print(f'going back up to: {all_dir_in_path.pop(0)}')

                for folder in all_dir_in_path:
                    visited_dir[folder] += file_sum

                current_dir = all_dir_in_path[0]
                continue
            
            # get values
            if listing:
                if command.startswith('dir'):
                    # print(f'dir: {command[4:]} in: {current_dir}')
                    continue

                file_size, name = command.split(' ')
                file_size = int(file_size)

                print(f'file: {name} in dir: {current_dir}')

                if file_size <= 100000:

                    file_sum += file_size



        print('sum: ', sum(visited_dir.values()))



def part_two():
    pass



def main():
    part_one()


if __name__ == "__main__":
    main()