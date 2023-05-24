from tkinter import *
import time

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


class Maze:

    def __init__(self, rows, cols, world, start, goal):
        self.reached = 0
        self.path = []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.rows = rows
        self.cols = cols
        self.world = world
        self.start = start
        self.cost = 0
        self.goal = goal
        self.covered = [[0 for x in range(0, cols)] for x in range(0, rows)]

        self.dfs(start)
        if self.reached == 0:
            print("No path exist.")

        print("DFS: ", self.path)
        print("Search Cost :", self.cost)

        root.destroy()

    # get all the possible adjacent nodes of the given coordinates
    def get_adjacent(self, X, Y):
        adjacent = []
        for k in range(0, 4):
            x = X + self.dx[k]
            y = Y + self.dy[k]

            if(x >= 0 and x < self.rows and y >= 0 and y < self.cols):
                adjacent.append([x, y])

        return adjacent

    def updateCanvas(self):
        time.sleep(0.1)
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

        for [i, j] in self.path:
            canvas.create_rectangle(
                i*blockSize + outlineLength, j*blockSize + outlineLength, (i+1)*blockSize, (j+1)*blockSize, fill="#00B426", outline="#00B426")

        for x in range(1, len(self.path)):
            i = (self.path[x][0] + self.path[x-1][0])/2
            j = (self.path[x][1] + self.path[x-1][1])/2
            canvas.create_rectangle(
                i*blockSize + outlineLength, j*blockSize + outlineLength, (i+1)*blockSize, (j+1)*blockSize, fill="#00B426", outline="#00B426")

        root.update()

    def dfs(self, cur):
        # if already visited or have reached goal return
        if self.reached == 1 or self.covered[cur[0]][cur[1]] == 1:
            return

        # push the cur node in the path and mark this node visited
        self.cost += 1
        self.path.append(cur)
        self.covered[cur[0]][cur[1]] = 1

        self.updateCanvas()

        # if current node is goal, mark reached as true
        if self.goal[0] == cur[0] and self.goal[1] == cur[1]:
            self.reached = 1
            return

        # traverse all the possible adjacent node of the current node
        for [x, y] in self.get_adjacent(cur[0], cur[1]):
            if(self.world[x][y] != 2):
                self.dfs([x, y])

        # if cannot reach to the goal node through this node then pop this node
        if self.reached == 0:
            self.path.pop()

        self.updateCanvas()


if __name__ == "__main__":
    reached = 0

    rows, cols = map(int, input().split(","))

    blockSize = min(windowWidth/rows, windowHeight/cols)
    outlineLength = blockSize/15

    xOffset = (windowWidth - blockSize*rows)/2
    yOffset = (windowHeight - cols*blockSize)/2

    start, end = input().split(";")
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))

    start[0] -= 1
    start[1] -= 1
    end[0] -= 1
    end[1] -= 1

    world = [[1 for x in range(0, cols)] for x in range(0, rows)]
    world[0][0] = 0
    world[end[0]][end[1]] = 3

    obstacles = list(input().split(";"))
    for i in obstacles:
        x, y = map(int, i.split(','))
        world[y-1][x-1] = 2

    def runMaze():
        Maze(rows, cols, world, start, end)

    root.after(1, runMaze)
    root.mainloop()
