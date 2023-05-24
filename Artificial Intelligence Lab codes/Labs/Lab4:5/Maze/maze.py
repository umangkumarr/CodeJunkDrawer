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
        self.goal = goal
        self.covered = [[0 for x in range(0, cols)] for x in range(0, rows)]

        self.dfs(start)
        print("DFS: ", self.path)
        if self.reached == 0:
            print("No path exist.")
            return

        self.bfs()
        print("BFS: ", self.path)

    # get all the possible adjacent nodes of the given coordinates
    def get_adjacent(self, X, Y):
        adjacent = []
        for k in range(0, 4):
            x = X + self.dx[k]
            y = Y + self.dy[k]

            if(x >= 0 and x < self.rows and y >= 0 and y < self.cols):
                adjacent.append([x, y])

        return adjacent

    def dfs(self, cur):
        # if already visited or have reached goal return
        if self.reached == 1 or self.covered[cur[0]][cur[1]] == 1:
            return

        # push the cur node in the path and mark this node visited
        self.path.append(cur)
        self.covered[cur[0]][cur[1]] = 1

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

    def bfs(self):
        self.covered = [[0 for x in range(0, self.cols)]
                        for x in range(0, self.rows)]

        # set parent of the node.. for backtracking from goal to start point
        parent = [[[-1, -1]
                   for x in range(0, self.cols)] for x in range(0, self.rows)]

        queue = [self.start]

        self.covered[start[0]][start[1]] = 1
        parent[start[0]][start[1]] = start

        while(queue):
            top = queue[0]
            queue.pop(0)

            for [x, y] in self.get_adjacent(top[0], top[1]):
                if self.covered[x][y] == 0 and self.world[x][y] != 2:
                    self.covered[x][y] = 1
                    parent[x][y] = top
                    queue.append([x, y])

        # backtracking
        cur = self.goal
        self.path = []
        while(cur != self.start):
            self.path.append(cur)
            cur = parent[cur[0]][cur[1]]
        self.path.append(cur)

        self.path = list(reversed(self.path))


if __name__ == "__main__":
    reached = 0

    rows, cols = map(int, input().split(","))

    start, end = input().split(";")
    start = list(map(int, start.split(',')))
    end = list(map(int, end.split(',')))

    start[0] -= 1
    start[1] -= 1
    end[0] -= 1
    end[1] -= 1

    world = [[1 for x in range(0, cols)] for x in range(0, rows)]
    world[0][0] = 0
    world[rows-1][cols-1] = 3

    obstacles = list(input().split(";"))
    for i in obstacles:
        x, y = map(int, i.split(','))
        world[x-1][y-1] = 2

    Maze(rows, cols, world, start, end)
