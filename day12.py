import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

sys.setrecursionlimit(5000)


# start node is 0, 20
# end at 20, 145

# for each step, check if can step
# if true step into square
# 
# for can step, must be within 1 number and not visited before and not an edge

#if end is found, return path_count

path = 'AdventOfCode2022\\Day12_input.txt'
test_path = 'AdventOfCode2022\\Day12_test_input.txt'

with open(path, 'rt', encoding='UTF-8') as inputfile:
    elev_map = inputfile.read().strip().split('\n')

visited = [[False for _ in line] for line in elev_map]

step_hist = []


edge_right = len(elev_map[0]) -1
edge_bottom = len(elev_map) -1 
global found 
found = False



def can_step(pos:int, next_step:tuple) -> bool:


    # reached an edge of map
    if next_step[0] < 0 or next_step[0] == edge_bottom or next_step[1] < 0 or next_step[1] == edge_right:
        return False



    ord_next_step = ord(elev_map[next_step[0]][next_step[1]])


    #if --- same height-------------one step higher------------------lower than 

    if (pos <= ord_next_step) or (pos == ord_next_step - 1) or ord_next_step == 69: #or (pos > ord_next_step)


        #check if been there before
        if not visited[next_step[0]][next_step[1]]:


            return True

    return False


def find_shortest_path(current_pos:tuple, end_pos:tuple, elav_map:list, path_count:int) -> int:
    global found

    print(f'step to {current_pos}')

    path_count = path_count + 1

    step_hist.append(current_pos)
    visited[current_pos[0]][current_pos[1]] = True

    pos_int = ord(elav_map[current_pos[0]][current_pos[1]])
    print(chr(pos_int))

    # starting pos is an S, this makes it an a to run the loop
    if pos_int == 83:
        pos_int = 97

    step_left = (current_pos[0], current_pos[1] - 1)
    step_right = (current_pos[0], current_pos[1] + 1)
    step_down = (current_pos[0] - 1, current_pos[1])
    step_up =  (current_pos[0] + 1, current_pos[1])

    data = [
        step_left,
        step_right,
        step_up,
        step_down
    ]


    if current_pos == end_pos:
    # base case, found end
        found = True
        print(f'found end\npath_count: {path_count}\nlast position: {current_pos}')
        return path_count

    
    
    
    else:
        blocked = False
        loop_count = 0

        while not blocked and not found:
            loop_count += 1


            for step in data:
                if can_step(pos_int, step) and not found:
                    path_count = find_shortest_path(step, end_pos, elev_map, path_count)
               
            
            if loop_count == 1:

                blocked = True
        return path_count

    


def plot_one(history):
    
    fig = plt.figure(figsize=(20,10))


    ax = fig.add_subplot()

    #ax.invert_yaxis()
    ax.invert_xaxis()

    max_x = max([x[0] for x in history]) + 5
    max_y = max([x[1] for x in history]) + 5

    ax.set_xlim((-5, max_y))
    ax.set_ylim((-5, max_x))
    frames = len(history)


    #for dot_row in range(-10, max_y):
        #for dot in range(-10, max_x):
            #ax.plot(dot, dot_row,'r+')

    def animate(i):
        # keep image or not
        #ax.clear()
        #ax.set_xlim((-5, max_y))
        #ax.set_ylim((-5, max_x))

        ax.set_title(i)

        ax.plot(history[i][1], history[i][0], 'b+')

    ani = animation.FuncAnimation(fig, animate, frames=frames, repeat=True, interval=20)

    print('made it past animation object creation')


    writergif = animation.PillowWriter(fps=45)

    ani.save('AdventOfCode2022\\day12_visual.gif', writergif)

    #plt.show()



def part_one() -> None:
    """returns fewest steps possible from start to end"""
    for index, row in enumerate(elev_map):

        for count, step in enumerate(row):
            if step == 'S' :
                start_pos = (index, count)
                continue
            elif step == 'E':
                end_pos = (index, count)
                print(end_pos)


    print(find_shortest_path(start_pos, end_pos, elev_map, 0))
    plot_one(step_hist)


if __name__ == "__main__":


    part_one()
