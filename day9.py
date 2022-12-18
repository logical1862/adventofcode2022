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

if __name__ == "__main__":
    path = 'AdventOfCode2022\\Day9_input.txt'
    test_path = 'AdventOfCode2022\\Day9_test_input.txt'

    with open(path, 'rt', encoding='UTF-8') as inputfile:
        moves = [x.strip('\n') for x in inputfile.readlines()]

    print(part_one(moves, True))