import random

class Game:
    def __init__(self, world, row, col, posA, posB):
        self.world = world
        self.row = row
        self.col = col
        self.agentAPos = [posA, [-1, -1]]
        self.agentBPos = [posB, [-1, -1]]
        self.dx = [0, 0, 1, -1]
        self.dy = [-1, 1, 0, 0]
        self.agentActions = [[], []]

    def getLegalActions(self, agent):
        actions = []
        x = self.agentAPos[0][0]
        y = self.agentAPos[0][1]
        px = self.agentAPos[1][0]
        py = self.agentAPos[1][1]

        if agent == 1:
            x = self.agentBPos[0][0]
            y = self.agentBPos[0][1]
            px = self.agentBPos[1][0]
            py = self.agentBPos[1][1]

        for i in range(4):
            xx = x + self.dx[i]
            yy = y + self.dy[i]
            if xx >= 0 and xx < self.row and yy >= 0 and yy < self.col:
                if [xx, yy] != [px, py] and [xx, yy] != self.agentBPos and [xx, yy] != self.agentAPos and self.world[xx][yy] != 1:
                    actions.append(i)

        return actions

    def getMinDistanceFromGoal(self, agent):
        agentPos = self.agentAPos[0]
        if agent == 1:
            agentPos = self.agentBPos[0]

        distance = []
        for i in range(self.row):
            for j in range(self.col):
                if self.world[i][j] == 3:
                    dist = pow(agentPos[0] - i, 2) + pow(agentPos[1] - j, 2)
                    distance.append(dist)

        return distance

    def getGoals(self):
        goals = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.world[i][j] == 3:
                    goals += 1

        return goals

    def moveAgent(self, agent, action):
        if action == -1:
            return

        self.agentActions[agent].append(action)
        if agent == 0:
            self.world[self.agentAPos[0][0]][self.agentAPos[0][1]] = 0
            cur = [self.agentAPos[0][0], self.agentAPos[0][1]]
            self.agentAPos[0][1] = self.agentAPos[0][1] + self.dy[action]
            self.agentAPos[0][0] += self.dx[action]
            # print(self.agentAPos, self.getGoals())
            if self.world[self.agentAPos[0][0]][self.agentAPos[0][1]] == 3:
                self.world[self.agentAPos[0][0]][self.agentAPos[0][1]] = 0
            self.agentAPos[1] = cur
            self.world[self.agentAPos[0][0]][self.agentAPos[0][1]] = 2
            # print(self.agentAPos)/

        else:
            cur = [self.agentBPos[0][0], self.agentBPos[0][1]]
            self.world[self.agentBPos[0][0]][self.agentBPos[0][1]] = 0
            self.agentBPos[0][0] += self.dx[action]
            self.agentBPos[0][1] += self.dy[action]
            # print(self.agentBPos, self.getGoals())
            if self.world[self.agentBPos[0][0]][self.agentBPos[0][1]] == 3:
                self.world[self.agentBPos[0][0]][self.agentBPos[0][1]] = 0

            self.agentBPos[1] = cur
            self.world[self.agentBPos[0][0]][self.agentBPos[0][1]] = 2
            # print(self.agentBPos)

    def clone(self):
        worldd = []
        for i in range(self.row):
            worldd.append([])
            for j in range(self.col):
                worldd[i].append(self.world[i][j])

        agentPosA = [self.agentAPos[0][0], self.agentAPos[0][1]]
        agentPosB = [self.agentBPos[0][0], self.agentBPos[0][1]]

        objClone = Game(worldd, self.row, self.col,
                        agentPosA, agentPosB)

        objClone.agentAPos[1] = self.agentAPos[1]
        objClone.agentBPos[1] = self.agentBPos[1]

        actionss = []
        for i in self.agentActions:
            actionss.append(i)
        objClone.agentActions = actionss

        return objClone


class MinMax:

    def __init__(self, gameState, depth):
        self.depth = depth
        self.gameState = gameState
        self.simulate(gameState, 0)

    def simulate(self, gameState, agent):
        if gameState.getGoals() == 0:
            return

        result = self.minmax(gameState, agent, 1)
        gameState.moveAgent(agent, result[1])
        lst = gameState.world
        for i in lst:
            print(i)
        print()

        self.simulate(gameState, agent ^ 1)

    def minmax(self, gameState, agent, depth):
        if depth == self.depth:
            return [self.evaluationFunction(gameState, agent), -1]

        if gameState.getGoals == 0:
            return [self.evaluationFunction(gameState, agent), -1]

        if not gameState.getLegalActions(agent):
            return [self.evaluationFunction(gameState, agent), -1]

        result = []
        for action in gameState.getLegalActions(agent):
            tempGameState = gameState.clone()
            tempGameState.moveAgent(agent, action)

            if not result:
                result = self.minmax(tempGameState, agent ^ 1, depth + 1)
                result[1] = action
            else:
                nextValue = self.minmax(tempGameState, agent ^ 1, depth + 1)
                if agent:
                    if result[0] <= nextValue[0]:
                        result[1] = action
                        result[0] = nextValue[0]
                else:
                    if result[0] >= nextValue[0]:
                        result[0] = nextValue[0]
                        result[1] = action

    def evaluationFunction(self, gameState, agent):

        minA = gameState.getMinDistanceFromGoal(0)
        minB = gameState.getMinDistanceFromGoal(1)

        hueristic = []
        for i in range(len(minA)):
            hueristic.append(minA[i] - minB[i])

        if agent == 0:
            return min(minA)
        else:
            return -min(minB)


if __name__ == "__main__":
    row, col = map(int, input().split())

    world = []
    for i in range(row):
        world.append(list(map(int, input().split(','))))

    posA = []
    posB = []

    for i in range(row):
        for j in range(col):
            if world[i][j] == 2:
                if len(posA) == 0:
                    posA = [i, j]
                else:
                    posB = [i, j]

    gameState = Game(world, row, col, posA, posB)
    play = MinMax(gameState, 2)
