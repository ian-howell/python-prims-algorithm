from collections import deque
from random import randint

SIZE = 20

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


def main():
    grid = []
    for i in range(SIZE):
        grid.append(['#'] * SIZE)

    st = Point(randint(0, SIZE), randint(0, SIZE), None)

    print(st)

    grid[st.x][st.y] = 'S'

    for i in range(SIZE):
        for j in range(SIZE):
            print(grid[i][j], end='')
        print()



if __name__ == "__main__":
    main()
