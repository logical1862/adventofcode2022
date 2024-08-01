"""dont look down"""
import matplotlib.pyplot as plt
import matplotlib.animation


class node:
    """knot positions"""
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

def update_tail(head:node, tail:node) -> node:
    """returns new tail position, updated to head"""
    # possible arrangements that need moving
    # tail is more than one to the left (but at same y)
    # tail is more than one to the right (but at same y)
    # tail is more than one up (but on the same x)
    # tail is more than one down (but on the same x)
    # tail is +- 1 to left/right but more than one up/down
    # tail is +- 1 up / down but more than one left / rihgt


    ## if tail is more than one off right or left, same y
    if head.y == tail.y and ((head.x - tail.x == 2) or (tail.x - head.x == 2)):
        if head.x > tail.x:
            tail.x += 1
        else:
            tail.x -= 1

    ## if tail is more than one off up or down, same x
    elif head.x == tail.x and ((head.y - tail.y == 2) or (tail.y - head.y == 2)):
        if head.y > tail.y:
            tail.y += 1
        else:
            tail.y -= 1

    # one right but more than one up
    elif head.x > tail.x and (head.y > tail.y and head.y - tail.y > 1):
        # up one, right one
        tail.x += 1
        tail.y += 1

    # one left but more than one up
    elif head.x < tail.x and (head.y > tail.y and head.y - tail.y > 1):
        # go up one, left one
        tail.x -= 1
        tail.y += 1

    # one right but more than one down
    elif head.x > tail.x and (head.y < tail.y and tail.y - head.y > 1):
        # up one, right one
        tail.x += 1
        tail.y -= 1

    # one left but more than one down
    elif head.x < tail.x and (head.y < tail.y and tail.y - head.y > 1):
        # go up one, left one
        tail.x -= 1
        tail.y -= 1

    # one up but more than right
    elif head.y > tail.y and (head.x - tail.x > 1):
        tail.x += 1
        tail.y += 1
    # one up but more than left
    elif head.y > tail.y and (tail.x - head.x > 1):
        tail.x -= 1
        tail.y += 1


    # one down but more than right
    elif tail.y > head.y and (head.x - tail.x > 1):
        tail.x += 1
        tail.y -= 1
    # one down but more than left
    elif tail.y > head.y and (tail.x - head.x > 1):
        tail.x -= 1
        tail.y -= 1


    return tail


def show_plot(head_data: list, tail_data: list) -> None:
    # create two axis, wide view / close view
    # wide view has const x and y limit
    # close view does not
    head_x_data = [x[0] for x in head_data[:]]
    head_y_data = [y[1] for y in head_data[:]]

    head_x_max = max(head_x_data)
    head_y_max = max(head_y_data)

    head_x_min = min(head_x_data)
    head_y_min = min(head_y_data)

    tail_x_data = [x[0] for x in tail_data[:]]
    tail_y_data = [y[1] for y in tail_data[:]]


    ax_xticks = [x for x in range(head_x_min - 3, head_x_max + 3, 10)]
    ax_yticks = [x for x in range(head_y_min - 3, head_y_max + 3, 10)]

    def animate(i):
        # ax is wide
        ax.clear()
        plt.xticks(rotation= 45)
        plt.yticks(rotation= 45)
        ax.set(xlim=(head_x_min, head_x_max), ylim=(head_y_min, head_y_max))

        

        ax.plot((head_x_data[i], tail_x_data[i]), (head_y_data[i], tail_y_data[i]),'r+', linestyle="--")

        # ax2 is close
        ax2.clear()

        # view limits
        xlim = (tail_x_data[i] - 3, tail_x_data[i] + 3)
        ylim = (tail_y_data[i] - 3, tail_y_data[i] + 3)

        ax2.set(xlim=xlim , ylim=ylim)

        ax2.set_yticks(ticks=[x for x in range(head_y_data[i] - 3, head_y_data[i] + 3)])
        ax2.set_xticks(ticks=[x for x in range(head_x_data[i] - 3, head_x_data[i] + 3)])

        ax2.plot((head_x_data[i], tail_x_data[i]), (head_y_data[i], tail_y_data[i]),'r+', linestyle="dashed")

        return


    fig, (ax, ax2) = plt.subplots(1,2)


    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=2000, repeat=False, interval=50, cache_frame_data=False)

    save_path = 'AdventOfCode2022\\day9visual.gif'
    writergif = matplotlib.animation.PillowWriter(fps=30)


    ani.save(save_path, writer=writergif)
    print('saved gif')

    return

def show_plot_two(data: list[list[tuple[int,int]]]) -> None:
    # create two axis, wide view / close view
    # wide view has const x and y limit
    # close view does not

    # view limits for wide plot
    head_x_data = [x[0] for x in data[0][:]]
    head_y_data = [y[1] for y in data[0][:]]

    head_x_max = max(head_x_data)
    head_y_max = max(head_y_data)

    head_x_min = min(head_x_data)
    head_y_min = min(head_y_data)


    def animate(i):
        # ax is wide
        ax.clear()
        ax.set(xlim=(head_x_min - 5, head_x_max + 5), ylim=(head_y_min - 5, head_y_max + 5))

        for knot in range(len(data[:])):
            ax.plot(data[knot][i][0], data[knot][i][1], 'r+', linestyle="--")






        # ax2 is close
        ax2.clear()

        # view limits
        xlim = (data[-1][i][0] - 12, data[-1][i][0] + 12)
        ylim = (data[-1][i][1] - 12, data[-1][i][1] + 12)

        ax2.set(xlim=xlim , ylim=ylim)

        ax2.set_yticks(ticks=[x for x in range(ylim[0], ylim[1])])
        ax2.set_xticks(ticks=[x for x in range(xlim[0], xlim[1])])

        for knot in range(len(data[:])):
            ax2.plot(data[knot][i][0], data[knot][i][1], 'r+', linestyle="--")

        return

    fig, (ax, ax2) = plt.subplots(1,2)


    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(head_x_data), repeat=False, interval=50, cache_frame_data=False)

    # plt.show()
    save_path = 'AdventOfCode2022\\day9visual_parttwo.gif'
    writergif = matplotlib.animation.PillowWriter(fps=10)

    ani.save(save_path, writer=writergif)
    print('saved gif')

    return

def part_one(moves: list, plot_img: bool) -> int:
    """returns number of visited squares"""

    # initiate some stuff

    head_pos_table = [(0,0)]
    tail_pos_table = [(0,0)]
    head_knot = node(0,0)
    tail_knot = node(0,0)

    for count, move in enumerate(moves):
        # check tail after each head move, cant be further than one
        direction, distance = move.split()

        # new position for head
        if direction == 'R':
            for i in range(int(distance)):
                # move head 1
                head_knot.x = head_knot.x + 1

                tail_knot = update_tail(head_knot, tail_knot)

                head_pos_table.append((head_knot.x, head_knot.y))
                tail_pos_table.append((tail_knot.x, tail_knot.y))
        
        elif direction == 'L':
            for i in range(int(distance)):
                # move head 1
                head_knot.x = head_knot.x - 1

                tail_knot = update_tail(head_knot, tail_knot)

                head_pos_table.append((head_knot.x, head_knot.y))
                tail_pos_table.append((tail_knot.x, tail_knot.y))

        elif direction == 'U':
            for i in range(int(distance)):
                # move head 1
                head_knot.y = head_knot.y + 1

                tail_knot = update_tail(head_knot, tail_knot)

                head_pos_table.append((head_knot.x, head_knot.y))
                tail_pos_table.append((tail_knot.x, tail_knot.y))

        elif direction == 'D':
            for i in range(int(distance)):
                # move head 1
                head_knot.y = head_knot.y - 1

                tail_knot = update_tail(head_knot, tail_knot)

                head_pos_table.append((head_knot.x, head_knot.y))
                tail_pos_table.append((tail_knot.x, tail_knot.y))

        # next movement
    visited = len(set(tail_pos_table))

    if plot_img:
        show_plot(head_pos_table, tail_pos_table)

    return visited


def part_two(moves:list) -> int:
    """now theres more of these things"""
    # same thing but now ten knots, use update tail for each  knots position in order
        # initiate some stuff
    NUM_KNOTS = 10
    knot_pos_list = [node(0,0) for x in range(NUM_KNOTS)]
    
    # nested, each column represents one knot
    visited_pos_table = [[(0,0)] for x in range(NUM_KNOTS)]


    for count, move in enumerate(moves):
        # check tail after each head move, cant be further than one
        direction, distance = move.split()
        distance = int(distance)

        # new position for head
        if direction == 'R':
            #move head once, adjust each knot , move head once etc..
            for head_movement in range(distance):
                # move head 1
                knot_pos_list[0].x += 1
                # adjust knots down the line
                for i in range(1, NUM_KNOTS):
                    #adjust next knot
                    knot_pos_list[i] = update_tail(knot_pos_list[i - 1],  knot_pos_list[i])
                    for knot in range(NUM_KNOTS):
                        # update new positions chart
                        visited_pos_table[knot].append((knot_pos_list[knot].x, knot_pos_list[knot].y))
        
        elif direction == 'L':

           #move head once, adjust each knot , move head once etc..
            for head_movement in range(distance):
                # move head 1
                knot_pos_list[0].x -= 1
                # adjust knots down the line
                for i in range(1, NUM_KNOTS):
                    #adjust next knot
                    knot_pos_list[i] = update_tail(knot_pos_list[i - 1],  knot_pos_list[i])
                    for knot in range(NUM_KNOTS):
                        # update new positions chart
                        visited_pos_table[knot].append((knot_pos_list[knot].x, knot_pos_list[knot].y))



        elif direction == 'U':
            #move head once, adjust each knot , move head once etc..
            for head_movement in range(distance):
                # move head 1
                knot_pos_list[0].y += 1
                # adjust knots down the line
                for i in range(1, NUM_KNOTS):
                    #adjust next knot
                    knot_pos_list[i] = update_tail(knot_pos_list[i - 1],  knot_pos_list[i])
                    for knot in range(NUM_KNOTS):
                        # update new positions chart
                        visited_pos_table[knot].append((knot_pos_list[knot].x, knot_pos_list[knot].y))

                        # next knot until all checked
        elif direction == 'D':
        #move head once, adjust each knot , move head once etc..
            for head_movement in range(distance):
                # move head 1
                knot_pos_list[0].y -= 1
                # adjust knots down the line
                for i in range(1, NUM_KNOTS):
                    #adjust next knot
                    knot_pos_list[i] = update_tail(knot_pos_list[i - 1],  knot_pos_list[i])
                    for knot in range(NUM_KNOTS):
                        # update new positions chart
                        visited_pos_table[knot].append((knot_pos_list[knot].x, knot_pos_list[knot].y))

                    # next knot until all checked

        # next movement
    tail_knot_visited = visited_pos_table[-1][:]
    visited = len(set(tail_knot_visited))

    show_plot_two(data = visited_pos_table)
    
    return visited

if __name__ == "__main__":
    path = 'AdventOfCode2022\\Day9_input.txt'
    test_path = 'AdventOfCode2022\\Day9_test_input.txt'

    with open(test_path, 'rt', encoding='UTF-8') as inputfile:
        moves = [x.strip('\n') for x in inputfile.readlines()]

    #print(part_one(moves, True))
    print(part_two(moves))
