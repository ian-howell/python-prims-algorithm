from random import randint
from time import sleep

SIZE = 50

RED = '\033[31m\033[41m'
YELLOW =  '\033[33m\033[43m'
ENDC = '\033[0m'

class Point:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p

    def get_opposite(self):
        if self.p.x - self.x == 0:
            if self.p.y - self.y == -1:
                return Point(self.x, self.y + 1, None)
            else:

                return Point(self.x, self.y - 1, None)
        elif self.p.x - self.x == -1:
            return Point(self.x + 1, self.y, None)
        else:
            return Point(self.x - 1, self.y, None)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    __repr__ = __str__

def isvalid(x, y):
    if x in range(0, SIZE) and y in range(0, SIZE):
        return True
    else:
        return False

def main():
    # Generate a grid of walls
    grid = []
    for i in range(SIZE):
        grid.append(['#'] * SIZE)

    # Randomly pick a start node
    st = Point(randint(0, SIZE - 1), randint(0, SIZE - 1), None)
    grid[st.x][st.y] = 'S'

    # Add the start node's neightbors to the frontier
    frontier = []
    for i in [-1, 1]:
        if isvalid(st.x + i, st.y):
            frontier.append(Point(st.x + i, st.y, st))
        if isvalid(st.x, st.y + i):
            frontier.append(Point(st.x, st.y + i, st))

    while (len(frontier) > 0):
        # print(frontier)
        ch = frontier.pop(randint(0, len(frontier)-1))
        op = ch.get_opposite()
        if isvalid(op.x, op.y) and grid[op.x][op.y] == '#':
            grid[ch.x][ch.y] = ' '
            grid[op.x][op.y] = '0'

            print('\n' * 10)

            for i in range(SIZE):
                for j in range(SIZE):
                    print(grid[i][j], end='')
                    # if grid[i][j] == ' ':
                    #     print(YELLOW + grid[i][j] + ENDC, end='')
                    # elif grid[i][j] == '0':
                    #     print(RED + 'S' + ENDC, end='')
                    # elif grid[i][j] == '#':
                    #     print('#', end='')
                    # elif grid[i][j] == 'S':
                    #     print(RED + 'S' + ENDC, end='')
                print()

            sleep(.10)


            grid[op.x][op.y] = ' '

            for i in [-1, 1]:
                if isvalid(op.x + i, op.y) and grid[op.x + i][op.y] == '#':
                    frontier.append(Point(op.x + i, op.y, op))
                if isvalid(op.x, op.y + i) and grid[op.x][op.y + i] == '#':
                    frontier.append(Point(op.x, op.y + i, op))
            print()

    for i in range(SIZE):
        for j in range(SIZE):
            print(grid[i][j], end='')
        print()


if __name__ == "__main__":
    main()
