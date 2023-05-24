from tkinter import *
import time
import math
from queue import PriorityQueue

root = Tk()

windowWidth = 600
windowHeight = 600

blockSize = 0
outlineLength = 0

xOffset = 0
yOffset = 0

root.geometry(f'{windowWidth}x{windowHeight}')

canvas = Canvas(root, width=windowWidth, height=windowHeight, bg="black")
canvas.pack()


class ASTAR:

    def __init__(self, rows, cols, world, start, goal):
        self.reached = 0
        self.path = []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.rows = rows
        self.cost = 0
        self.cols = cols
        self.world = world
        self.start = start
        self.goal = goal
        self.covered = [[0 for x in range(0, cols)] for x in range(0, rows)]

        self.astar()

    def getResult(self):
        return (self.path, self.cost)

    # get all the possible adjacent nodes of the given coordinates
    def get_adjacent(self, X, Y):
        adjacent = []
        for k in range(0, 4):
            x = X + self.dx[k]
            y = Y + self.dy[k]

            if(x >= 0 and x < self.rows and y >= 0 and y < self.cols and world[x][y] != 2):
                adjacent.append([x, y])

        return adjacent

    def astar(self):

        que = PriorityQueue()
        [x, y] = self.start
        [X, Y] = self.goal
        hx = pow(abs(x-X), 2) + pow(abs(y-Y), 2)
        que.put([0 + hx, 0, hx, self.start, [self.start]])

        while(que.empty() == False):

            top = que.get()
            path = top[4]

            if self.covered[top[3][0]][top[3][1]] == 1:
                continue

            self.cost += 1
            self.covered[top[3][0]][top[3][1]] = 1

            if top[3] == self.goal:
                self.path = path
                return

            for [x, y] in self.get_adjacent(top[3][0], top[3][1]):
                hx = pow(abs(x-X), 2) + pow(abs(y-Y), 2)
                fx = top[1]
                newPath = path + [[x, y]]
                que.put([hx + fx, fx, hx, [x, y], newPath])


class Maze:

    def __init__(self, rows, cols, world, start, goals):
        self.path = []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.rows = rows
        self.cols = cols
        self.world = world
        self.start = start
        self.goals = goals
        self.cost = 0

        self.multigoalAstar()

        print(self.path)
        print(self.cost)

        self.updateCanvas()

        root.destroy()

    def updateCanvas(self):
        canvas.delete('all')

        for i in range(rows):
            for j in range(cols):
                canvas.create_rectangle(
                    i*blockSize, j*blockSize, (i+1)*blockSize, (j+1)*blockSize, fill="black")

        for i in range(rows):
            for j in range(cols):
                colorr = "black"
                if(world[i][j] == 2):
                    colorr = "red"
                elif world[i][j] == 3:
                    colorr = "yellow"
                canvas.create_rectangle(
                    i*blockSize + outlineLength, j*blockSize + outlineLength, (i+1)*blockSize, (j+1)*blockSize, fill=colorr)

        root.update()

        for [i, j] in self.path:

            canvas.create_rectangle(
                i*blockSize + outlineLength, j*blockSize + outlineLength, (i+1)*blockSize, (j+1)*blockSize, fill="#00B426", outline="#00B426")

            root.update()
            time.sleep(0.2)

            colorr = "grey"
            if(world[i][j] == 3):
                colorr = "blue"

            canvas.create_rectangle(
                i*blockSize + outlineLength, j*blockSize + outlineLength, (i+1)*blockSize, (j+1)*blockSize, fill=colorr, outline=colorr)

            root.update()

    def getManhattan(self, start, goal):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def multigoalAstar(self):
        cnt = 0
        vis = []
        start = self.start
        while cnt < len(self.goals):
            goal = []
            cost = math.inf

            for end in self.goals:
                if end not in vis and cost > self.getManhattan(start, end):
                    cost = self.getManhattan(start, end)
                    goal = end

            obj = ASTAR(self.rows, self.cols, self.world, start, goal)
            (path, cost) = obj.getResult()
            self.path += path[1:]
            start = goal
            self.cost += cost
            vis.append(goal)
            cnt += 1

        print(self.path)


if __name__ == "__main__":
    reached = 0

    rows, cols = map(int, input().split(","))

    blockSize = min(windowWidth/rows, windowHeight/cols)
    outlineLength = blockSize/30

    xOffset = (windowWidth - blockSize*rows)/2
    yOffset = (windowHeight - cols*blockSize)/2

    start = list(map(int, input().split(',')))
    start[0] -= 1
    start[1] -= 1

    end = list(input().split(";"))
    for j in range(len(end)):
        end[j] = list(map(int, end[j].split(',')))
        end[j][0] -= 1
        end[j][1] -= 1

    world = [[1 for x in range(0, cols)] for x in range(0, rows)]
    world[0][0] = 0
    for [x, y] in end:
        world[x][y] = 3

    obstacles = list(input().split(";"))
    for i in obstacles:
        x, y = map(int, i.split(','))
        world[x-1][y-1] = 2

    def runMaze():
        Maze(rows, cols, world, start, end)

    root.after(1, runMaze)
    root.mainloop()
