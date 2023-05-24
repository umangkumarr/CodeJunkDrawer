from tkinter import *
import time
from PIL import Image, ImageTk

root = Tk()

windowWidth = 600
windowHeight = 600

blockSize = 0
outlineLength = 0

root.geometry(f'{windowWidth}x{windowHeight}')

canvas = Canvas(root, width=windowWidth, height=windowHeight, bg="white")
canvas.pack()

img = Image.open('dirt.png')
vacuum = Image.open('vacuum.png')


class Cleaner_DFS:
    # if world[i][j] == 1 -> Dirt present
    # if world[i][j] == 0 -> noDirt present

    def __init__(self, world, vaccumClear_pos, rows, cols):
        self.world = world
        self.vaccumClear_pos = vaccumClear_pos
        self.covered = [[0 for x in range(0, cols)] for x in range(0, rows)]
        self.state = []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.rows = rows
        self.cols = cols
        self.path = []
        self.roomsCovered = 0

        self.dfs(vaccumClear_pos)
        for i in self.path:
            print(i)

        time.sleep(10)
        root.destroy()

    def isAllCovered(self):
        return self.roomsCovered == (self.rows*self.cols)

    def isDirt(self, room):
        return self.world[room[0]][room[1]] == 1

    def get_roomNo(self, cur):
        X = cur[0]
        Y = cur[1]

        room = (X)*self.rows + (Y+1)
        return room

    def get_adjacent(self, X, Y):
        for k in range(0, 4):
            x = X + self.dx[k]
            y = Y + self.dy[k]

            if(x >= 0 and x < self.rows and y >= 0 and y < self.cols and self.covered[x][y] == 0):
                direction = ''
                action = ''
                if k == 0:
                    direction = 'L'
                    action = "Moving Left"
                elif k == 1:
                    direction = 'R'
                    action = "Moving Right"
                elif k == 2:
                    direction = 'U'
                    action = "Moving Up"
                else:
                    direction = 'D'
                    action = "Moving Down"
                return [x, y, direction, action]

    def update(self, actions, cur_pos, next_pos):
        time.sleep(1)
        canvas.delete('all')

        for i in range(self.rows):
            for j in range(self.cols):
                canvas.create_rectangle(
                    i*blockSize, j*blockSize, (i+1)*blockSize, (j+1)*blockSize, fill="white", outline="black")

                if world[i][j] == 1:
                    canvas.create_image(
                        i*blockSize, j*blockSize, anchor=NW, image=img)

        if self.isDirt(cur_pos):
            world[cur_pos[0]][cur_pos[1]] = 0

        mess = ""
        for i in actions:
            mess += i
            mess += '\n'
        canvas.create_text((cur_pos[0]+0.2)*blockSize, (cur_pos[1]+0.2)*blockSize,
                           text=mess, fill="black", font=('Helvetica', '15', 'bold'))

        obj = canvas.create_image(
            (cur_pos[0]+0.4)*(int(blockSize)), (cur_pos[1]+0.4)*(int(blockSize)), anchor=NW, image=vacuum)
        # if next_pos != [-1, -1]:
        #     X = next_pos[0] - cur_pos[0]
        #     Y = next_pos[1] - cur_pos[1]
        #     k = 0
        #     while(k < 1):
        #         # time.sleep(1)
        #         canvas.move(obj, int((X*k)*blockSize), int((Y*k)*blockSize))
        #         k += 0.001

        root.update()

    def dfs(self, cur):
        self.roomsCovered += 1
        self.covered[cur[0]][cur[1]] = 1

        actions = []
        if self.isDirt(cur):
            actions.append("Dirt Found")
            actions.append("Suck Dirt")
            self.path.append([self.get_roomNo(cur), 'S'])
        else:
            actions.append("No Dirt found")
            self.path.append([self.get_roomNo(cur), 'N'])

        if self.isAllCovered():
            self.update(actions, cur, [-1, -1])
        else:
            x, y, direction, action = self.get_adjacent(cur[0], cur[1])
            actions.append(action)
            self.path.append([self.get_roomNo(cur), direction])
            self.update(actions, cur, [x, y])
            self.dfs([x, y])


class Cleaner_BFS:
    # if world[i][j] == 1 -> Dirt present
    # if world[i][j] == 0 -> noDirt present

    def __init__(self, world, vaccumClear_pos, rows, cols):
        self.world = world
        self.vaccumClear_pos = vaccumClear_pos
        self.covered = [[0 for x in range(0, cols)] for x in range(0, rows)]
        self.state = []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.rows = rows
        self.cols = cols
        self.path = []
        self.roomsCovered = 0

        self.bfs(vaccumClear_pos)
        for i in self.path:
            print(i)

    def isAllCovered(self):
        return self.roomsCovered == (self.rows*self.cols)

    def isDirt(self, room):
        return self.world[room[0]][room[1]] == 1

    def get_roomNo(self, cur):
        X = cur[0]
        Y = cur[1]

        room = (X)*self.rows + (Y+1)
        return room

    def get_adjacent(self, X, Y):
        adjacent = []
        for k in range(0, 4):
            x = X + self.dx[k]
            y = Y + self.dy[k]

            if(x >= 0 and x < self.rows and y >= 0 and y < self.cols and self.covered[x][y] == 0):
                direction = ''
                if k == 0:
                    direction = 'L'
                elif k == 1:
                    direction = 'R'
                elif k == 2:
                    direction = 'U'
                else:
                    direction = 'D'
                adjacent.append([x, y, direction])

        return adjacent

    def next_directions(self, cur, next):
        X = next[0] - cur[0]
        Y = next[1] - cur[1]

        if self.dx[0] == X and self.dy[0] == Y:
            return 'L'
        elif self.dx[1] == X and self.dy[1] == Y:
            return 'R'
        elif self.dx[2] == X and self.dy[2] == Y:
            return 'U'
        else:
            return 'D'

    def bfs(self, start):

        queue = []

        self.covered[start[0]][start[1]] = 1
        queue.append([start])
        pre = [start]

        while len(queue):
            top = queue[0]
            queue.pop(0)

            # indx = len(pre)-1
            # while pre[indx] not in top:
            #     indx-

            if self.isDirt(top[-1]):
                self.path.append([self.get_roomNo(top[-1]), 'S'])
            else:
                self.path.append([self.get_roomNo(top[-1]), 'N'])

            for [x, y, direction] in self.get_adjacent(top[-1][0], top[-1][1]):
                if(self.covered[x][y]):
                    continue
                self.covered[x][y] = 1
                self.path.append(
                    [self.get_roomNo(top[-1]), self.next_directions(top[-1], [x, y])])
                queue.append(top + [[x, y]])


if __name__ == "__main__":
    pos = int(input())
    rows = 2
    cols = 2

    pos -= 1
    pos = [pos//rows, pos % rows]

    blockSize = min(windowWidth/rows, windowHeight/cols)
    outlineLength = blockSize/15
    img = img.resize((int(blockSize), int(blockSize)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    vacuum = vacuum.resize(
        (int(blockSize/2), int(blockSize/2)), Image.ANTIALIAS)
    vacuum = ImageTk.PhotoImage(vacuum)

    world = [[0 for x in range(0, cols)] for x in range(0, rows)]

    dirts = list(map(int, input().split(',')))
    for i in range(len(dirts)):
        r = (i)//rows
        c = (i) % rows
        world[r][c] = dirts[i]

    algo = input()

    if algo == 'dfs':
        def runCleaner():
            Cleaner_DFS(world, pos, rows, cols)

        root.after(1, runCleaner)
        root.mainloop()
    else:
        Cleaner_BFS(world, pos, rows, cols)
